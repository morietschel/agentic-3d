from scad_utils import save_scad_code, render_model
from api_utils import initial_code_api_call, updated_code_api_call, feedback_api_call
from config import SCENE_DESCRIPTION, MAX_ITERATIONS

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

def get_dynamic_model_code(current_scad_code=None, scene_feedback=None):
    """
    Calls the OpenAI API to get OpenSCAD code based on user input and scene feedback (if inputted).
    Returns the API call reply if there is one.
    """
    if scene_feedback:
        assistant_reply = updated_code_api_call(current_scad_code, scene_feedback)
    else:
        print("First iteration. Generating initial code based on object description.")
        assistant_reply = initial_code_api_call()

    if assistant_reply:
        print("Received OpensSCAD Code")
        return assistant_reply
    else:
        print("Failed to get a response from the OpenAI API.")
        return None
    
def get_scene_feedback(output_image):
    """
    Calls the OpenAI API to get feedback based on output image and user input.
    Returns the API call reply if there is one.
    """
    assistant_reply = feedback_api_call(output_image)
    if assistant_reply:
        print("Received feedback")
        return assistant_reply
    else:
        print("Failed to get a response from the OpenAI API.")
        return None

def combine_scad_code(permanent_code, dynamic_code):
    """
    Combines permanent and dynamic OpenSCAD code into a single script.
    Returns the combined code.
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
    Returns the output path.
    """
    scad_filepath = save_scad_code(scad_code, scad_filename)
    output_path = render_model(scad_filepath, output_image)

    print("[DEBUG] Rendering process completed")
    return output_path

def main():
    """ 
        Returns True if function generates matching render, and False if not. 
    """
    iteration_count = 1
    match = False

    # Get permanent model code
    permanent_model_code = get_permanent_model_code()
    
    while iteration_count <= MAX_ITERATIONS and not match:
        print(f"Iteration {iteration_count}...")

        if iteration_count == 1:
            # Get initial dynamic model code from OpenAI using only user input
            dynamic_model_code = get_dynamic_model_code()
            if not dynamic_model_code:
                print("[ERROR] Initial API call failed. Exiting.")
                return  # Exit if API call failed
        else:
            # Update dynamic model code from OpenAI using user input and scene feedback
            dynamic_model_code = get_dynamic_model_code(dynamic_model_code, scene_feedback)
            if not dynamic_model_code:
                print("[ERROR] API call failed. Exiting.")
                return  # Exit if API call failed

        # Combine both codes
        combined_scad_code = combine_scad_code(permanent_model_code, dynamic_model_code)

        # Render the scene and return the output path
        output_path = render_scene(combined_scad_code, scad_filename=f'scene{iteration_count}.scad', output_image=f'scene{iteration_count}.png')

        # Get feedback on scene image
        scene_feedback = get_scene_feedback(output_path)
        if scene_feedback['match']:
            print(f"Object generation successful. Completed in {iteration_count} iterations.")
            return True
        #print("scene_feedback:", scene_feedback)

        iteration_count += 1

    print(f"Object generation unsuccessfull. Terminated after 10 iterations.")
    return False

if __name__ == "__main__":
    main()