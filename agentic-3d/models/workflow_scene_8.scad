
    // Combined Scene

    // Permanent Model
    
    // Permanent Model (Black)
    color([0, 0, 0]) {
        // Your permanent model code here
        cube([100,0.1,0.1], center = false);
        cube([0.1,100,0.1], center = false);
        cube([0.1,0.1,100], center = false);
    }
    

    // Dynamic Model
    translate([0, 0, 0]) {
    // Chair seat dimensions
    seat_height = 5; 
    seat_width = 50; 
    seat_depth = 45; 
    difference() {
        cube([seat_width, seat_depth, seat_height], center=true); // Main seat
        translate([-18, -18, -0.1]) 
            cylinder(h=3, r=2, center=true); // Cutout for lighter seat
    }

    // Ergonomic backrest with a smooth curve
    backrest_height = 30; 
    backrest_width = 45; 
    translate([0, -22, seat_height]) {
        rotate_extrude(angle=180) {
            translate([0, 10, 0])
                circle(r=20); // Smooth backrest curve
        }
    }

    // Chair legs with strength and stability
    leg_height = 20; 
    leg_thickness = 5; 
    for (x = [-1, 1]) {
        for (y = [-1, 1]) {
            translate([20 * x, 22 * y, -leg_height]) {
                cube([leg_thickness, leg_thickness, leg_height], center=true); // All four legs
            }
        }
    }

    // Curved armrests for comfort
    armrest_thickness = 10; 
    for (x = [-1, 1]) {
        translate([24 * x, -25, 10]) {
            difference() {
                scale([1, 0.5, 1])
                    rotate_extrude(angle=180)
                        translate([0, 6, 0])
                        circle(r=4); // Armrest contour
                translate([-6, -0.5, 0])
                    cube([12, 1, armrest_thickness], center=true); // Armrest thickness
            }
        }
    }

    // Base for added stability 
    base_height = 5; 
    base_width = 70; 
    base_depth = 60; 
    translate([0, 0, -base_height]) {
        cube([base_width, base_depth, base_height], center=true); // Base platform
    }
    
    // Tolerance adjustments for easier assembly
    translate([-26, -21, seat_height]) {
        cube([7, 5, 10], center=true); // Tolerance cutout for leg attachment
    }
    
    translate([26, -21, seat_height]) {
        cube([7, 5, 10], center=true); // Tolerance cutout for leg attachment
    }

    translate([-26, 21, seat_height]) {
        cube([7, 5, 10], center=true); // Tolerance cutout for leg attachment
    }

    translate([26, 21, seat_height]) {
        cube([7, 5, 10], center=true); // Tolerance cutout for leg attachment
    }
}
    