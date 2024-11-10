# This file defines all the different autogen agents for our purposes.
from typing import Dict, List, Tuple, Union

import autogen
from autogen import ConversableAgent, UserProxyAgent
from autogen.agentchat.contrib.multimodal_conversable_agent import (
    MultimodalConversableAgent,
)

# from autogen.agentchat.contrib.capabilities.teachability import Teachability
from ._constants import LLM_CONFIG
from .utils import combine_scad_code, render_model, save_openscad_code


class AgentBuilder:
    def __init__(self, generator_system_message: str, feedback_system_message: str):
        self.all_agents = [
            self.get_designer_agent(),
            self.get_openscad_generator_agent(generator_system_message),
            self.get_feedback_agent(feedback_system_message),
        ]

    def get_designer_agent(self):
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

    def get_openscad_generator_agent(self, system_message: str):
        openSCAD_generatorAgent = ConversableAgent(
            name="openscad_generator",
            llm_config=LLM_CONFIG,
            system_message=system_message,
        )
        return openSCAD_generatorAgent

    def get_feedback_agent(self, system_message: str):
        feedbackAgent = MultimodalConversableAgent(
            name="feedback",
            llm_config=LLM_CONFIG,
            system_message=system_message,
            is_termination_msg=lambda msg: msg.get("content") is not None
            and "TERMINATE_MATCH" in msg["content"],
            human_input_mode="NEVER",
        )
        return feedbackAgent

    def print_agents(self):
        for agent in self.all_agents:
            print(agent.name)


class OpenSCADExecutorAgent(ConversableAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, llm_config=False, **kwargs)
        self.register_reply(ConversableAgent, self.get_openscad_code)

    def get_openscad_code(
        self,
        messages: List[Dict] = [],
        sender=None,
        config=None,
    ) -> Tuple[bool, Union[str, Dict, None]]:
        last_message = messages[-1]["content"]
        result = self.render_scene(last_message)
        return True, result

    def render_scene(
        scad_code: str,
        scad_filename: str = "scene.scad",
        output_image_file: str = "scene.png",
    ) -> str:
        """
        Saves the SCAD code to a file and renders it to an image.
        Returns the output path.
        """
        combined_scad_code = combine_scad_code(scad_code)
        scad_filepath = save_openscad_code(combined_scad_code, scad_filename)
        output_image_path = render_model(scad_filepath, output_image_file)

        print("[DEBUG] Rendering process completed.")
        return output_image_path
