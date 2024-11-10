from ._constants import DEFAULT_USER_DESCRIPTION
from .strategy import *


class Prompter:
    def __init__(
        self,
        user_description: str = DEFAULT_USER_DESCRIPTION,
        strategies: list[BaseStrategy] = [DirectStrategy],
    ):
        self.user_description = user_description
        self.strategies = strategies
        self.prompts = {}

    def generate_all_prompts(self):
        self.prompts = {}
        for strategy in self.strategies:
            self.prompts[strategy.name] = strategy.create_prompt(self.user_description)

    def get_all_prompts(self):
        if not self.prompts:
            self.generate_all_prompts()
        return self.prompts
