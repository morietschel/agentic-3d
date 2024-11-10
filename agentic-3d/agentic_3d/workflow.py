# TODO: this file is the workflow for the agents.
import autogen as ag
from autogen import AssistantAgent, ConversableAgent, UserProxyAgent
from autogen.agentchat.contrib.multimodal_conversable_agent import (
    MultimodalConversableAgent,
)

from ._constants import (
    DEFAULT_FEEDBACK_AGENT_SYSTEM_MESSAGE,
    DEFAULT_OPENSCAD_GENERATOR_AGENT_SYSTEM_MESSAGE,
    LLM_CONFIG,
    MAX_ITERATIONS,
)
from .agents import AgentBuilder
from .utils import render_scene


# TODO: could add tqdm for progress bar per iteration
class Workflow:
    def __init__(self, prompt: str):
        self.initial_prompt = prompt

    def run(
        self,
        openscad_generator_system_message: str = DEFAULT_OPENSCAD_GENERATOR_AGENT_SYSTEM_MESSAGE,
        feedback_system_message: str = DEFAULT_FEEDBACK_AGENT_SYSTEM_MESSAGE,
    ):
        ab = AgentBuilder(openscad_generator_system_message, feedback_system_message)

        designerAgent = ab.all_agents[0]
        openSCAD_generatorAgent = ab.all_agents[1]
        feedbackAgent = ab.all_agents[2]

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
            print(f"--------Iteration {iteration}---------")

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
        return chat_history
