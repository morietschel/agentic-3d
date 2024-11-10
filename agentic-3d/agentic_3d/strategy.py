class BaseStrategy:
    def __init__(self):
        self.name = "base"

    def create_prompt(self, user_description: str):
        raise NotImplementedError("Subclasses should implement this method")


class DirectStrategy(BaseStrategy):
    def __init__(self):
        self.name = "direct"

    def create_prompt(self, user_description: str) -> str:
        return f"Generate OpenSCAD code for the following object description: {user_description}"


class Print3DStrategy(BaseStrategy):
    def __init__(self):
        self.name = "print3d"

    def create_prompt(self, user_description: str) -> str:
        return f"Generate OpenSCAD code for the following object description: {user_description}. Optimize the design for 3D printing with appropriate tolerances and supports."


class ArtisticStrategy(BaseStrategy):
    def __init__(self):
        self.name = "artistic"

    def create_prompt(self, user_description: str) -> str:
        return f"Generate OpenSCAD code for the following object description: {user_description}. Create a sculptural or artistic interpretation of the object with creative flair. Optimize the design for aesthetic appeal."


class DimensionStrategy(BaseStrategy):
    def __init__(self):
        self.name = "dimension"

    def create_prompt(self, user_description: str, dimensions: str) -> str:
        return f"Generate OpenSCAD code for the following object description: {user_description}. Ensure the object has the following dimensions: {dimensions}."


class FeatureStrategy(BaseStrategy):
    def __init__(self):
        self.name = "feature"

    def create_prompt(self, user_description: str, features: str) -> str:
        return f"Generate OpenSCAD code for the following object description: {user_description}. Include the following features: {features}."


class ConstraintStrategy(BaseStrategy):
    def __init__(self):
        self.name = "constraint"

    def create_prompt(
        self, user_description: str, material: str, properties: str
    ) -> str:
        return f"Generate OpenSCAD code for the following object description: {user_description} Generate OpenSCAD code for the following object description: {user_description}. The object should be made of {material} and have the following properties: {properties}."
