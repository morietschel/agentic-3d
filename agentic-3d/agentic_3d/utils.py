import os
import subprocess

from ._constants import (
    CACHE_DB,
    IMAGE_SIZE,
    MODELS_DIR,
    PERMANENT_MODEL_CODE,
    RENDERS_DIR,
)


def combine_scad_code(dynamic_code: str) -> str:
    """
    Combines permanent and dynamic OpenSCAD code into a single script.
    Returns the combined code.
    """
    combined_code = f"""
    // Combined Scene

    // Permanent Model
    {PERMANENT_MODEL_CODE}

    // Dynamic Model
    {dynamic_code}
    """
    return combined_code


def save_openscad_code(scad_code: str, filename: str) -> str:
    """
    Save the provided OpenSCAD code to a specified .scad file.
    Args:
        scad_code (str): The OpenSCAD code to be saved.
        filename (str): The name of the file to save the OpenSCAD code in.
    Returns:
        str: The filepath where the OpenSCAD code was saved.
    """
    os.makedirs(MODELS_DIR, exist_ok=True)

    filepath = os.path.join(MODELS_DIR, filename)
    print(f"[DEBUG] Saving OpenSCAD code to {filepath}")

    with open(filepath, "w") as f:
        f.write(scad_code)
    print(f"[DEBUG] OpenSCAD code saved successfully at {filepath}")

    return filepath


def render_model(scad_filepath: str, output_image_file: str) -> str:
    """
    Renders a 3D model from an OpenSCAD file and saves it as an image.
    Args:
        scad_filepath (str): The file path to the OpenSCAD (.scad) file.
        output_image_file (str): The desired output image file name.
    Returns:
        str: The file path to the rendered image.
    Raises:
        subprocess.CalledProcessError: If the OpenSCAD rendering command fails.
        Exception: If an unexpected error occurs during rendering.
    Example:
        rendered_image = render_model("path/to/model.scad", "output_image.png")
    """

    os.makedirs(RENDERS_DIR, exist_ok=True)

    rendered_image_path = os.path.join(RENDERS_DIR, output_image_file)

    cmd = [
        "openscad",
        "-o",
        rendered_image_path,
        "--imgsize={},{}".format(*IMAGE_SIZE),
        "--view=64.10,356.50,34.60,25.40,4.02,46.29,535.52",
        scad_filepath,
    ]

    print(f"[DEBUG] Rendering model to image {rendered_image_path}")
    print(f"[DEBUG] Running command: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"[DEBUG] Rendered image saved at: {rendered_image_path}")
        return rendered_image_path

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] An error occurred during rendering: {e}")
        print(f"[ERROR] Return code: {e.returncode}")
        print(f"[ERROR] Command stderr: {e.stderr}")

    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")


def render_scene(
    scad_code: str,
    scad_filename: str = "scene.scad",
    output_image_file: str = "scene.png",
) -> str:
    """
    Renders a 3D scene from OpenSCAD code and saves it as an image file.
    Args:
        scad_code (str): The OpenSCAD code to render.
        scad_filename (str, optional): The filename to save the OpenSCAD code. Defaults to "scene.scad".
        output_image_file (str, optional): The filename to save the rendered image. Defaults to "scene.png".
    Returns:
        str: The file path of the rendered image.
    """
    combined_scad_code = combine_scad_code(scad_code)
    scad_filepath = save_openscad_code(combined_scad_code, scad_filename)
    output_image_path = render_model(scad_filepath, output_image_file)

    print("[DEBUG] Rendering process completed.")
    return output_image_path


def remove_cache():
    """
    Remove the cache database Autogen creates.
    """
    print("[DEBUG] Removing cache database.")
    os.remove(CACHE_DB)
    print("[DEBUG] Cache database removed successfully.")
