# utils.py

import os
import subprocess

from ._constants import (
    CAMERA_ANGLE,
    CAMERA_LOOK_AT,
    CAMERA_POSITION,
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
    Save the OpenSCAD code to a .scad file.
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
    Render the .scad file to an image using OpenSCAD.
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
    Saves the SCAD code to a file and renders it to an image.
    Returns the output path.
    """
    combined_scad_code = combine_scad_code(scad_code)
    scad_filepath = save_openscad_code(combined_scad_code, scad_filename)
    output_image_path = render_model(scad_filepath, output_image_file)

    print("[DEBUG] Rendering process completed.")
    return output_image_path
