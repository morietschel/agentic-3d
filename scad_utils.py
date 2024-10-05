# scad_utils.py

import os
import subprocess
from config import (
    IMAGE_SIZE, CAMERA_POSITION, CAMERA_LOOK_AT, CAMERA_ANGLE
)

def save_scad_code(scad_code, filename):
    """
    Save the OpenSCAD code to a .scad file.
    """
    models_dir = 'models'
    os.makedirs(models_dir, exist_ok=True)
    filepath = os.path.join(models_dir, filename)
    print(f"[DEBUG] Saving OpenSCAD code to {filepath}")
    with open(filepath, 'w') as f:
        f.write(scad_code)
    print(f"[DEBUG] OpenSCAD code saved successfully at {filepath}")
    return filepath

def render_model(scad_file, output_image):
    """
    Render the .scad file to an image using OpenSCAD.
    """
    renders_dir = 'renders'
    os.makedirs(renders_dir, exist_ok=True)
    output_path = os.path.join(renders_dir, output_image)

    cmd = [
        'openscad',
        '-o', output_path,
        '--imgsize={},{}'.format(*IMAGE_SIZE),
        '--view=64.10,356.50,34.60,25.40,4.02,46.29,535.52',
        scad_file
    ]

    print(f"[DEBUG] Rendering model to image {output_path}")
    print(f"[DEBUG] Running command: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"[DEBUG] Rendered image saved at: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] An error occurred during rendering: {e}")
        print(f"[ERROR] Return code: {e.returncode}")
        print(f"[ERROR] Command stderr: {e.stderr}")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
