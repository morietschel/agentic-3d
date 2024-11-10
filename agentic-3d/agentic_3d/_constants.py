import os

# Seed for consistency
RANDOM_SEED = 42

# Scene description
DEFAULT_USER_DESCRIPTION = "designer chair"

# Max iterations
MAX_ITERATIONS = 10

# Rendering settings
IMAGE_SIZE = (800, 600)  # Width, Height in pixels

# Camera settings
CAMERA_POSITION = [25.40, 4.02, 46.29]  # x, y, z position of the camera
CAMERA_LOOK_AT = [0, 0, 0]  # x, y, z point the camera looks at
CAMERA_ANGLE = 90  # Camera angle in degrees

PERMANENT_MODEL_CODE = """
    // Permanent Model (Black)
    color([0, 0, 0]) {
        // Your permanent model code here
        cube([100,0.1,0.1], center = false);
        cube([0.1,100,0.1], center = false);
        cube([0.1,0.1,100], center = false);
    }
    """

# File Paths
MODELS_DIR = "../models"
RENDERS_DIR = "../renders"
CACHE_DB = "../notebooks/.cache/41/cache.db"

# LLM Configuration
LLM_CONFIG = {
    "config_list": [{"model": "gpt-4o-mini", "api_key": os.getenv("OPENAI_API_KEY")}]
}

# AGENT SYSTEM MESSAGES
DEFAULT_OPENSCAD_GENERATOR_AGENT_SYSTEM_MESSAGE = """You are a CAD agent that takes a user request and responds 
            only with executable OpenSCAD code. Please keep the following dimensions in mind when 
            creating the object, as the perspective is fixed for the following space: 100 x 100 x 100
            You only write CAD code to construct the object, never to render or display it.
            Output the code as a string, without any coding block or other annotations.
"""
DEFAULT_FEEDBACK_AGENT_SYSTEM_MESSAGE = """You are an image feedback agent. 
            Your role is to examine rendered images (from OpenSCAD code) and confirm whether they match the user’s initial description. 
            If they do match, respond with 'TERMINATE_MATCH'.
            Do not give feedback on the color.
            If they don't match provide suggestions for how the scene can be improved in a structured way.
            Give your feedback in instructive bullets. 
            Start with 
            'Initial User Description': 
            'Feedback:'
            """
