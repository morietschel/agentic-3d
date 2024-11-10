from ._constants import DEFAULT_USER_DESCRIPTION
from .strategy import *


class Prompter:
    """
    The Prompter class is responsible for generating and managing prompts based on user descriptions and strategies.
    Attributes:
        user_description (str): A description provided by the user. Defaults to DEFAULT_USER_DESCRIPTION.
        strategies (list[BaseStrategy]): A list of strategies to generate prompts. Defaults to [DirectStrategy].
        prompts (dict): A dictionary to store generated prompts.
    Methods:
        generate_all_prompts():
            Generates prompts for all strategies and stores them in the prompts attribute.
        get_all_prompts() -> dict:
            Returns all generated prompts. If prompts are not already generated, it calls generate_all_prompts() first.
    """

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
