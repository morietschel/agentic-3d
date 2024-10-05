# main.py

from scad_utils import save_scad_code, render_model
import os

def main():
    print("[DEBUG] Starting the OpenSCAD rendering process")

    # OpenSCAD code for the permanent model (black)
    permanent_model_code = '''
    // Permanent Model (Black)
    color([0, 0, 0]) {
        // Your permanent model code here
        cube([100,0.1,0.1], center = false);
        cube([0.1,100,0.1], center = false);
        cube([0.1,0.1,100], center = false);
    }
    '''

    # OpenSCAD code for the dynamic model
    dynamic_model_code = '''
    // Dynamic Model
    // Your dynamic model code here
    // Example: A sphere
    translate([1.5, 0, 0]) {
        // Simple Chair in OpenSCAD

    // Chair dimensions (in centimeters)
    lw = 2;   // Leg width
    ld = 2;   // Leg depth
    lh = 40;  // Leg height

    sw = 40;  // Seat width
    sd = 40;  // Seat depth
    st = 2;   // Seat thickness

    bw = sw;  // Backrest width
    bh = 30;  // Backrest height
    bt = 2;   // Backrest thickness

    // Leg positions
    leg_positions = [
        [0, 0, 0],                     // Front-left leg
        [sw - lw, 0, 0],               // Front-right leg
        [sw - lw, sd - ld, 0],         // Back-right leg
        [0, sd - ld, 0]                // Back-left leg
    ];

    // Draw legs
    for (pos = leg_positions) {
        translate(pos)
            cube([lw, ld, lh]);
    }

    // Draw seat
    translate([0, 0, lh])
        cube([sw, sd, st]);

    // Draw backrest
    translate([0, sd - bt, lh + st])
        cube([bw, bt, bh]);

    }
    '''

    # Combine both models into a single OpenSCAD code
    combined_scad_code = f'''
    // Combined Scene

    // Permanent Model
    {permanent_model_code}

    // Dynamic Model
    {dynamic_model_code}
    '''

    # Save the combined OpenSCAD code to a .scad file
    scad_filename = 'scene.scad'
    scad_filepath = save_scad_code(combined_scad_code, scad_filename)

    # Render the scene to an image
    output_image = 'scene.png'
    render_model(scad_filepath, output_image)

    print("[DEBUG] Rendering process completed")

if __name__ == "__main__":
    main()
