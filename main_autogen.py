from dotenv import load_dotenv
import os
from autogen_utils import get_prompt_code, get_msg_initial_code, get_prompt_feedback, get_prompt_feedback_code
from scad_utils import save_scad_code, render_model
from autogen import ConversableAgent
from autogen.agentchat.contrib.multimodal_conversable_agent import MultimodalConversableAgent
from config import SCENE_DESCRIPTION, MAX_ITERATIONS

# Load environment variables from .env file
load_dotenv()

# LLM configuration
llm_config = {"config_list": [{"model": "gpt-4o-mini", "api_key": os.getenv('OPENAI_API_KEY')}]}

# AGENTS
code_agent = ConversableAgent(
    name="code_agent",
    system_message=get_prompt_code(),
    max_consecutive_auto_reply=1,
    llm_config=llm_config,
)

feedback_agent = MultimodalConversableAgent(
    name="feedback_agent",
    system_message=get_prompt_feedback(),
    llm_config=llm_config,
)

feedback_code_agent = ConversableAgent(
    name="feedback_code_agent",
    system_message=get_prompt_feedback_code(),
    llm_config=llm_config,
    is_termination_msg=lambda msg: "terminate_match" in msg["content"].lower(),
)


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

def main():
    iteration_count = 0
    print(f"Iteration {iteration_count}...")
    
    ## INITIAL CODE
    # Get permanent model code
    permanent_model_code = get_permanent_model_code()
    
    # Get initial dynamic model code from OpenAI using only user input
    dynamic_model_code = code_agent.generate_reply(messages=[{"content": get_msg_initial_code(SCENE_DESCRIPTION), "role": "user"}])
    if not dynamic_model_code:
        print("[ERROR] Initial API call failed. Exiting.")
        return  # Exit if API call failed
    
    # Combine both codes
    combined_scad_code = combine_scad_code(permanent_model_code, dynamic_model_code)
    
    # Render the scene and return the output path
    output_path = render_scene(combined_scad_code, scad_filename=f'scene{iteration_count}.scad', output_image=f'scene{iteration_count}.png')
    
    ## FEEDBACK
    
    while iteration_count < MAX_ITERATIONS:
        print(f"Iteration {iteration_count}...") 
    
        chat_results = feedback_code_agent.initiate_chats(
                [
                    {
                        "recipient": feedback_agent,
                        "message": f"""
                        Here is the image of the current render <img {output_path}>. 
                        Here is the intended image description: A {SCENE_DESCRIPTION}.
                        Please provide feedback.
                        """,
                        "max_turns": 1,
                        "summary_method": "last_msg",
                    },     
                    {
                        "recipient": feedback_code_agent,
                        "message": f"""
                        The user has provided the following description:
                        {SCENE_DESCRIPTION}
                        Please incorporate the feedback into the current version of the executable OpenSCAD code: 
                        {dynamic_model_code}.
                        """,
                        "max_turns": 1,
                        "summary_method": "last_msg",
                    },
                ]
            )
    
        iteration_count += 1

        dynamic_model_code = chat_results[-1].summary
        combined_scad_code = combine_scad_code(permanent_model_code, dynamic_model_code)
        output_path = render_scene(combined_scad_code, scad_filename=f'scene{iteration_count}.scad', output_image=f'scene{iteration_count}.png')

if __name__ == "__main__":
    main()