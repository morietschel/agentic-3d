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

def render_model(scad_filepath, output_image, view_params=None):
    """Renders OpenSCAD model to image"""
    output_path = os.path.join("renders", output_image)
    
    command = [
        'openscad',
        '-o', output_path,
        '--imgsize=800,600'
    ]
    
    if view_params:
        command.append(f'--view={view_params}')
        
    command.append(scad_filepath)
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"OpenSCAD Error: {result.stderr}")
    except Exception as e:
        print(f"[ERROR] An error occurred during rendering: {e}")
        raise
        
    return output_path