
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
    seat_height = 10;  // Adjusted for better height
    seat_width = 50; 
    seat_depth = 45; 
    difference() {
        cube([seat_width, seat_depth, seat_height], center=true); // Main seat
        translate([-18, -18, -0.1]) 
            cylinder(h=3, r=2, center=true); // Cutout for lighter seat
    }

    // Ergonomic backrest with a smooth curve
    backrest_height = 30; 
    backrest_width = 50; 
    translate([0, -22, seat_height]) {
        rotate_extrude(angle=180) {
            translate([0, 8, 0])
                circle(r=20); // Smooth backrest curve
        }
    }

    // Chair legs with strength and stability
    leg_height = 15; 
    leg_thickness = 6;  // Thicker legs for more stability
    for (x = [-1, 1]) {
        for (y = [-1, 1]) {
            translate([20 * x, 22 * y, -leg_height]) {
                cube([leg_thickness, leg_thickness, leg_height], center=true); // All four legs
            }
        }
    }

    // Curved armrests for comfort
    armrest_thickness = 5; 
    for (x = [-1, 1]) {
        translate([25 * x, -25, 10]) {
            difference() {
                scale([1, 0.5, 1])
                    rotate_extrude(angle=180)
                        translate([0, 4, 0])
                        circle(r=7); // Wider armrest contour
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
    
    // Tolerance cuts for leg attachment
    tolerance_height = 2;  // Reduced tolerance height for snug fit
    translate([-24, -21, seat_height]) {
        cube([6, 6, tolerance_height], center=true); // Tolerance cutout for leg attachment
    }
    
    translate([24, -21, seat_height]) {
        cube([6, 6, tolerance_height], center=true); // Tolerance cutout for leg attachment
    }

    translate([-24, 21, seat_height]) {
        cube([6, 6, tolerance_height], center=true); // Tolerance cutout for leg attachment
    }

    translate([24, 21, seat_height]) {
        cube([6, 6, tolerance_height], center=true); // Tolerance cutout for leg attachment
    }
}
    