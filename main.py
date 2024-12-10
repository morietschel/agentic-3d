from dotenv import load_dotenv
import os
from autogen_utils import get_prompt_critics, get_prompt_coder, get_prompt_commander, get_prompt_prompt_improver
from scad_utils import save_scad_code, render_model
from autogen import Agent, AssistantAgent, ConversableAgent, UserProxyAgent
from autogen.agentchat.contrib.multimodal_conversable_agent import MultimodalConversableAgent
from config import SCENE_DESCRIPTION, MAX_ITERATIONS
from api_utils import remove_cache
import matplotlib.pyplot as plt
from PIL import Image
import autogen

# Load environment variables from .env file
load_dotenv()

# LLM configuration
llm_config = {"config_list": [{"model": "gpt-4o-mini", "api_key": os.getenv('OPENAI_API_KEY')}]}
llm_config_critics = {"config_list": [{"model": "gpt-4o-mini", "api_key": os.getenv('OPENAI_API_KEY')}], "max_tokens": 500}


# Other helper functions
def get_permanent_model_code():
    """
    Returns the OpenSCAD code for the permanent model.
    """
    permanent_model_code = '''
    // Permanent Model (Black)
    color([0, 0, 0]) {
        // Your permanent model code here
        cube([100,0.1,0.1], center = false);
        cube([0.1,100,0.1], center = false);
        cube([0.1,0.1,100], center = false);
    }
    '''
    return permanent_model_code

def combine_scad_code(permanent_code, dynamic_code):
    """
    Combines permanent and dynamic OpenSCAD code into a single script.
    Returns the combined code.
    """
    combined_code = f'''
    // Combined Scene

    // Permanent Model
    {permanent_code}

    // Dynamic Model
    {dynamic_code}
    '''
    return combined_code

def render_scene(scad_code, scad_filename='scene.scad', output_image='scene.png'):
    """
    Saves the SCAD code to a file and renders it to an image. 
    Returns the output path.
    """
    scad_filepath = save_scad_code(scad_code, scad_filename)
    output_path = render_model(scad_filepath, output_image)

    print("[DEBUG] Rendering process completed")
    return output_path

# TOOL CALL
def tool_call(dynamic_model_code: str) -> str:
    """
    Renders OpenSCAD code to generate a 3D scene image.
    This function combines a dynamic model's SCAD code with a permanent base model, renders the resulting 3D scene, 
    and returns the output image's file path. It also generates a feedback prompt for further refinements.

    Args:
        dynamic_model_code (str): The OpenSCAD code for the dynamic part of the 3D model.
        iteration_count (int): The current iteration number, used for naming the output files.

    Returns:
        str: str: A completion message containing with the file path to the rendered image.
    """
    permanent_model_code = get_permanent_model_code()
    combined_scad_code = combine_scad_code(permanent_model_code, dynamic_model_code)
    output_path = render_scene(combined_scad_code, scad_filename=f'scene{""}.scad', output_image=f'scene{""}.png')

    message = f"Rendering completed, image saved at: <img {output_path}>."
    return message

# Set working directory. Use "" to set to pwd
working_dir = ""

class Creator(ConversableAgent):
    def __init__(self, tool, n_iters=2, **kwargs):
        """
        Initializes a Creator instance.
        This agent facilitates the creation of 3D models through a collaborative effort among its child agents: commander, coder, and critics.

        Parameters:
            - n_iters (int, optional): The number of "improvement" iterations to run. Defaults to 2.
            - **kwargs: keyword arguments for the parent AssistantAgent.
        """

        super().__init__(**kwargs)
        self.register_reply([Agent, None], reply_func=Creator._reply_user, position=0)
        self._n_iters = n_iters
        self.tool = tool
        
    def _reply_user(self, messages=None, sender=None, config=None):
        if all((messages is None, sender is None)):
            error_msg = f"Either {messages=} or {sender=} must be provided."
            logger.error(error_msg) # What is this, I have a squiggly line under 'logger'
            raise AssertionError(error_msg)
        
        if messages is None:
            messages = self._oai_messages[sender]

        user_question = messages[-1]["content"]
        
        # Define the agents
        commander = AssistantAgent(
            name="Commander",
            human_input_mode="NEVER",
            max_consecutive_auto_reply=10,
            system_message=get_prompt_commander(),
            #is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
            llm_config=self.llm_config,
        )
        # Register tool use
        commander.register_for_llm(name="render_code", description="Renders openSCAD code and generates an image from it.")(self.tool)
        
        prompt_improver = ConversableAgent(
            name="Prompt_Improver",
            system_message=get_prompt_prompt_improver(),
            llm_config=llm_config,
            human_input_mode="NEVER",
            max_consecutive_auto_reply=1,
        )
        
        coder = AssistantAgent(
            name="Coder",
            system_message=get_prompt_coder(),
            llm_config=self.llm_config,
        )
        # Register tool use
        coder.register_for_execution(name="render_code")(self.tool)
        
        critics = MultimodalConversableAgent(
            name="Critics",
            system_message=get_prompt_critics(),
            llm_config=llm_config_critics,
            human_input_mode="NEVER",
            max_consecutive_auto_reply=self._n_iters,
        )
        
        # Data flow defintion
        iteration_count = 0
        print(f"Iteration {iteration_count}...") 
        
        # ADD PROMPT IMPROVER
        print("Phase 1: Improving Prompt...")
        commander.send(
                message=f"Improve this user description: {user_question}.",
                recipient=prompt_improver,
                request_reply=True,
            )
        
        description = commander._oai_messages[prompt_improver][-1]["content"] # This is the point to include the strategies?
        
        commander.initiate_chat(coder, message=f"Please create OpenSCAD code for the following object description: {description}")
        img = Image.open(os.path.join(working_dir, "renders/scene.png"))
        plt.imshow(img)
        plt.axis("off") # Hide the axes
        # Save the image
        save_path = os.path.join(working_dir, f"renders/scene{iteration_count}.png")
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0)

        print(f"Starting feedback loop...") 
        for __ in range(self._n_iters):
            iteration_count += 1
            print(f"Iteration {iteration_count}...") 

            commander.send(
                message=f"Here is the image of the current render <img {os.path.join(working_dir, 'renders/scene.png')}>. Here is the intended image description: {description} Please provide actionable feedback.",
                recipient=critics,
                request_reply=True,
            )
            
            feedback = commander._oai_messages[critics][-1]["content"]

            commander.send(
                message="Here is the feedback for the image rendered from your code. Please improve the previous code! \n" + feedback,
                recipient=coder,
                request_reply=True,
            )

            img = Image.open(os.path.join(working_dir, "renders/scene.png"))
            plt.imshow(img)
            plt.axis("off")  # Hide the axes
            save_path = os.path.join(working_dir, f"renders/scene{iteration_count}.png")
            plt.savefig(save_path, bbox_inches='tight', pad_inches=0)

        # Is this from ConversableAgent documentation? Because I can't change it without causing an error.
        remove_cache()
        return True, os.path.join(working_dir, "renders/scene.png")

def main(scene_description):
    creator = Creator(name="3D Creator~", tool=tool_call, n_iters=MAX_ITERATIONS, llm_config=llm_config)
    
    user_proxy = autogen.UserProxyAgent(
        name="User", 
        human_input_mode="NEVER", 
        max_consecutive_auto_reply=0, 
        code_execution_config={"use_docker": False}
    )

    user_proxy.initiate_chat(
        creator,
        message=scene_description,
    )
    
if __name__ == "__main__":
    main(SCENE_DESCRIPTION)