from dotenv import load_dotenv
import os
from scad_utils import save_scad_code, render_model
from api_utils import openai_api_call

# Load environment variables from .env
load_dotenv()

def get_dynamic_model_code(user_input):
    """
    Calls the OpenAI API to get OpenSCAD code based on user input.
    """
    assistant_reply = openai_api_call(user_input)
    if assistant_reply:
        print("Received OpensScad Code")
        return assistant_reply
    else:
        print("Failed to get a response from the OpenAI API.")
        return None

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
    """
    scad_filepath = save_scad_code(scad_code, scad_filename)
    render_model(scad_filepath, output_image)
    print("[DEBUG] Rendering process completed")

def main():
    # Example OpenAI query
    user_input = "Give me the code for a designer chair."

    # Get dynamic model code from OpenAI
    dynamic_model_code = get_dynamic_model_code(user_input)
    if not dynamic_model_code:
        return  # Exit if API call failed

    # Get permanent model code
    permanent_model_code = get_permanent_model_code()

    # Combine both codes
    combined_scad_code = combine_scad_code(permanent_model_code, dynamic_model_code)

    # Render the scene
    render_scene(combined_scad_code)

if __name__ == "__main__":
    main()
