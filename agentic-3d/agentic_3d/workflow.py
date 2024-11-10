from ._constants import (
    DEFAULT_FEEDBACK_AGENT_SYSTEM_MESSAGE,
    DEFAULT_OPENSCAD_GENERATOR_AGENT_SYSTEM_MESSAGE,
    MAX_ITERATIONS,
)
from .agents import AgentBuilder
from .utils import remove_cache, render_scene


# TODO: could add tqdm for progress bar per iteration
class Workflow:
    """
    Workflow class to manage the iterative process of generating and refining OpenSCAD code
    based on user feedback.
    """

    def __init__(
        self,
        prompt: str,
        openscad_generator_system_message: str = DEFAULT_OPENSCAD_GENERATOR_AGENT_SYSTEM_MESSAGE,
        feedback_system_message: str = DEFAULT_FEEDBACK_AGENT_SYSTEM_MESSAGE,
    ):
        """
        Initialize the Workflow with the given prompt and system messages.

        Args:
            prompt (str): The initial prompt to start the workflow.
            openscad_generator_system_message (str, optional): System message for the OpenSCAD generator agent. Defaults to DEFAULT_OPENSCAD_GENERATOR_AGENT_SYSTEM_MESSAGE.
            feedback_system_message (str, optional): System message for the feedback agent. Defaults to DEFAULT_FEEDBACK_AGENT_SYSTEM_MESSAGE.
        """
        self.initial_prompt = prompt
        self.openscad_generator_system_message = openscad_generator_system_message
        self.feedback_system_message = feedback_system_message

        self.all_agents = self.build_agents()

    def build_agents(self):
        """
        Build the agents required for the workflow.

        Returns:
            list: A list of agents built by the AgentBuilder.

        Raises:
            ValueError: If no agents are retrieved.
        """
        ab = AgentBuilder(
            self.openscad_generator_system_message, self.feedback_system_message
        )
        if ab.all_agents is None:
            raise ValueError(
                "Retrieved No Agents. Check if Agents were built correctly."
            )
        return ab.all_agents

    # TODO: can change all_agents to dictionary with keys as agent names for more clarity
    def run(self, clear_cache: bool = False):
        """
        Executes the workflow for generating and iterating on OpenSCAD code with feedback loops.
        Args:
            clear_cache (bool): If True, clears the cache before starting the workflow so that
            Autogen calls OpenAI API again. Default is False.
        Returns:
            list: A list of chat history objects containing summaries of the interactions between agents.
        Workflow:
            1. Optionally clears the cache if `clear_cache` is True.
            2. Initializes the designer agent, OpenSCAD generator agent, and feedback agent.
            3. Starts the first iteration by initiating a chat between the designer agent and OpenSCAD generator agent.
            4. Renders the initial scene based on the generated OpenSCAD code.
            5. Iteratively:
            a. Sends the current render and description to the feedback agent for feedback.
            b. Sends the feedback and current OpenSCAD code to the OpenSCAD generator agent for improvements.
            c. Updates the feedback, OpenSCAD code, and rendered image.
            d. Continues until the maximum number of iterations is reached.
            6. Returns the chat history of all interactions.
        """

        if clear_cache:
            remove_cache()

        designerAgent = self.all_agents[0]
        openSCAD_generatorAgent = self.all_agents[1]
        feedbackAgent = self.all_agents[2]

        iteration = 0

        dynamic_code_all = designerAgent.initiate_chat(
            openSCAD_generatorAgent,
            message=self.initial_prompt,
            max_turns=1,
            summary="last_msg",
        )
        dynamic_code = dynamic_code_all.summary
        img_filepath = render_scene(
            dynamic_code_all.summary,
            f"workflow_scene_{iteration}.scad",
            f"workflow_scene_{iteration}.png",
        )

        feedback = self.initial_prompt

        while iteration < MAX_ITERATIONS:
            print(f"---------ITERATION {iteration}---------")

            chat_history = openSCAD_generatorAgent.initiate_chats(
                [
                    {
                        "recipient": feedbackAgent,
                        "message": f"""
                        Here is the image of the current render <img {img_filepath}>. 
                        Here is the description: {feedback}.
                        Please provide more feedback.
                        """,
                        "max_turns": 1,
                        "summary_method": "last_msg",
                    },
                    {
                        "recipient": openSCAD_generatorAgent,
                        "message": f"""
                        The user has provided the following description:
                        {self.initial_prompt}
                        This is the current executable OpenSCAD code: 
                        {dynamic_code}. Improve this code and generate new OpenSCAD code based on feedback.
                        """,
                        "max_turns": 1,
                        "summary_method": "last_msg",
                    },
                ]
            )

            iteration += 1
            feedback = chat_history[0].summary
            dynamic_code = chat_history[1].summary
            img_filepath = render_scene(
                dynamic_code,
                f"workflow_scene_{iteration}.scad",
                f"workflow_scene_{iteration}.png",
            )
            print(f"All {iteration} iterations completed.")
        return chat_history
