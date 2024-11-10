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

        # assistantAgent = ag.ConversableAgent(
        #     name="assistant",
        #     llm_config=LLM_CONFIG,
        #     system_message="""You are a supervisor AI assistant.
        #     "You help suggest tool calls or arguments for functions.""",
        #     max_consecutive_auto_reply=2,
        #     human_input_mode="NEVER",
        #     is_termination_msg=lambda msg: msg.get("content") is not None
        #     and "TERMINATE" in msg["content"],
        # )

        # designerAgent = ag.UserProxyAgent(
        #     name="designer",
        #     human_input_mode="NEVER",
        #     llm_config=LLM_CONFIG,
        #     code_execution_config=False,
        #     is_termination_msg=lambda x: x.get("content", "")
        #     and x.get("content", "").rstrip().endswith("TERMINATE"),
        #     max_consecutive_auto_reply=1,
        # )

        # sm = """You are a CAD agent that takes a user request and responds only with executable OpenSCAD code.
        #     Please keep the following dimensions in mind when creating the object, as the perspective is fixed for the following space: 100 x 100 x 100
        #     You only write CAD code to construct the object, never to render or display it.
        #     Output the code as a string, without any coding block or other annotations.
        #     """
        # openSCAD_generatorAgent = ag.ConversableAgent(
        #     name="openscad_generator",
        #     llm_config=LLM_CONFIG,
        #     system_message="""You are a CAD agent that takes a user request and responds only with executable OpenSCAD code.
        #     Please keep the following dimensions in mind when creating the object, as the perspective is fixed for the following space: 100 x 100 x 100
        #     You only write CAD code to construct the object, never to render or display it.
        #     Output the code as a string, without any coding block or other annotations.
        #     """,
        # )

        # openSCAD_executorAgent = OpenSCADExecutorAgent(
        #     name="openscad_executor",
        #     system_message="""You are a OpenSCAD code executor agent that takes a openSCADcode and just executes the code.
        #     Run the function and return the output. Nothing else.
        #     Return 'TERMINATE' after task is done.
        #     """,
        #     is_termination_msg=lambda msg: msg.get("content") is not None
        #     and "TERMINATE" in msg["content"],
        #     human_input_mode="NEVER",
        # )

        # feedbackAgent = MultimodalConversableAgent(
        #     name="feedback",
        #     llm_config=LLM_CONFIG,
        #     system_message="""You are an image feedback agent.
        #     Your role is to examine rendered images (from OpenSCAD code) and confirm whether they match the user’s initial description.
        #     If they do match, respond with 'TERMINATE_MATCH'.
        #     Do not give feedback on the color.
        #     If they don't match provide suggestions for how the scene can be improved in a structured way.
        #     Give your feedback in instructive bullets.
        #     Start with
        #     'Initial User Description':
        #     'Feedback:'
        #     """,
        #     is_termination_msg=lambda msg: msg.get("content") is not None
        #     and "TERMINATE_MATCH" in msg["content"],
        #     human_input_mode="NEVER",
        # )

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

        # # assistantAgent.register_for_llm(
        # #     description="Render OpenSCAD scene",
        # # )(self.render_scene)
        # assistantAgent.register_for_llm(
        #     name="renderer",
        #     description="Render OpenSCAD scene",
        # )(render_scene)
        # # openSCAD_generatorAgent.register_for_llm(description="Render OpenSCAD scene")
        # openSCAD_generatorAgent.register_for_llm(
        #     name="renderer",
        #     description="Render OpenSCAD scene",
        # )(render_scene)
        # openSCAD_executorAgent.register_for_execution(name="render_scene")(render_scene)

        # group_chat = ag.GroupChat(
        #     agents=[designerAgent, openSCAD_generatorAgent, openSCAD_executorAgent],
        #     messages=[],
        #     max_round=10,
        # )
        # manager = ag.GroupChatManager(
        #     name="Manager", groupchat=group_chat, llm_config=LLM_CONFIG
        # )

        # chat_history = designerAgent.initiate_chat(manager, message=self.initial_prompt)
        # chat_history = assistantAgent.initiate_chats(
        #     [
        #         {
        #             "recipient": openSCAD_generatorAgent,
        #             "message": self.initial_prompt,
        #             "clear_history": True,
        #             "silent": False,
        #             "summary_method": "last_msg",
        #         },
        #         {
        #             "recipient": openSCAD_executorAgent,
        #             "message": "Call Render scene function as the result of last llm call as the argument",
        #             "summary_method": "reflection_with_llm",
        #         },
        #     ]
        # )

        # chat_history = designerAgent.initiate_chats(
        #     [
        #         {
        #             "recipient": openSCAD_generatorAgent,
        #             "message": self.initial_prompt,
        #             "max_turns": 1,
        #             "summary_method": "last_msg",
        #         },
        #         {
        #             "recipient": openSCAD_executorAgent,
        #             "message": "Call Render scene function as the result of last llm call as the argument",
        #             "max_turns": 1,
        #             "summary_method": "reflection_with_llm",
        #         },
        #     ]
        # )
        # return None
