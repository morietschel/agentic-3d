from autogen import ConversableAgent, UserProxyAgent
from autogen.agentchat.contrib.multimodal_conversable_agent import (
    MultimodalConversableAgent,
)

from ._constants import LLM_CONFIG


class AgentBuilder:
    """
    A class used to build and manage different types of agents.
    Methods
    -------
    __init__(generator_system_message: str, feedback_system_message: str)
        Initializes the AgentBuilder with the specified system messages for the generator
        and feedback agents.
    build_designer_agent()
        Builds and returns a UserProxyAgent configured as a designer agent.
    build_openscad_generator_agent(system_message: str)
        Builds and returns a ConversableAgent configured as an OpenSCAD generator agent
        with the provided system message.
    build_feedback_agent(system_message: str)
        Builds and returns a MultimodalConversableAgent configured as a feedback agent
        with the provided system message.
    print_agents()
        Prints the names of all the agents managed by the AgentBuilder.
    """

    def __init__(self, generator_system_message: str, feedback_system_message: str):
        """
        Initializes the agent system with the provided system messages for the generator and feedback agents.
        Args:
            generator_system_message (str): The system message to be used by the OpenSCAD generator agent.
            feedback_system_message (str): The system message to be used by the feedback agent.
        """

        self.all_agents = [
            self.build_designer_agent(),
            self.build_openscad_generator_agent(generator_system_message),
            self.build_feedback_agent(feedback_system_message),
        ]

    def build_designer_agent(self) -> UserProxyAgent:
        """
        Builds and returns a UserProxyAgent named as a designer.
        This is essentially the user who has a description they want to build using OpenSCAD.
        Returns:
            UserProxyAgent: The configured designer agent.
        """
        designerAgent = UserProxyAgent(
            name="designer",
            human_input_mode="NEVER",
            llm_config=LLM_CONFIG,
            code_execution_config=False,
            is_termination_msg=lambda x: x.get("content", "")
            and x.get("content", "").rstrip().endswith("TERMINATE"),
            max_consecutive_auto_reply=1,
        )
        return designerAgent

    def build_openscad_generator_agent(self, system_message: str) -> ConversableAgent:
        """
        Builds and returns a ConversableAgent with the role of an OpenSCAD code generator.
        This agent is responsible for generating OpenSCAD code based on the initial
        description as defined in the provided system message.
        Args:
            system_message (str): The system message to be used by the OpenSCAD generator agent.
        Returns:
            ConversableAgent: The configured OpenSCAD generator agent.
        """
        openSCAD_generatorAgent = ConversableAgent(
            name="openscad_generator",
            llm_config=LLM_CONFIG,
            system_message=system_message,
        )
        return openSCAD_generatorAgent

    def build_feedback_agent(self, system_message: str) -> MultimodalConversableAgent:
        """
        Builds and returns a MultimodalConversableAgent with the role of a feedback agent.
        This agent is responsible for providing feedback based on the image and initial
        description as defined in the provided system message.
        Args:
            system_message (str): The system message to be used by the feedback agent.
        Returns:
            MultimodalConversableAgent: The configured feedback agent.
        """
        feedbackAgent = MultimodalConversableAgent(
            name="feedback",
            llm_config=LLM_CONFIG,
            system_message=system_message,
            is_termination_msg=lambda msg: msg.get("content") is not None
            and "TERMINATE_MATCH" in msg["content"],
            human_input_mode="NEVER",
        )
        return feedbackAgent

    def print_agents(self) -> None:
        """
        Prints the names of all the agents managed by the AgentBuilder.
        """
        for agent in self.all_agents:
            print(agent.name)
