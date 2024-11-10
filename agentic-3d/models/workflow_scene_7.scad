
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
    // Chair seat
    bottom_seat = 3; 
    seat_width = 50; 
    seat_depth = 45; 
    difference() {
        cube([seat_width, seat_depth, bottom_seat], center=true); // Seat
        translate([-18, -18, -0.1]) 
            cylinder(h=5, r=2, center=true); // Cutout for lighter seat
    }

    // Ergonomic backrest with an incline for comfort
    backrest_angle = 20; 
    backrest_height = 30; 
    translate([0, -22, bottom_seat]) {
        linear_extrude(height=backrest_height) {
            polygon(points=[[0, 0], [20, 0], [25, backrest_angle], [-25, backrest_angle], [-20, 0]], paths=[[0, 1, 2, 3, 4]]);
        }
    }

    // Simplified legs with stability features
    leg_height = 20; 
    leg_thickness = 5; 
    for (x = [-1, 1]) {
        translate([20 * x, -22, -leg_height]) {
            cube([leg_thickness, leg_thickness, leg_height], center=true); // Front legs
        }
    }
    for (x = [-1, 1]) {
        translate([20 * x, 22, -leg_height]) {
            cube([leg_thickness, leg_thickness, leg_height], center=true); // Back legs
        }
    }

    // Armrests with a modern curve
    armrest_thickness = 10; 
    for (x = [-1, 1]) {
        translate([24 * x, -25, 10]) {
            difference() {
                scale([1, 0.5, 1])
                    rotate_extrude(angle=180)
                        translate([0, 10, 0])
                        circle(r=3);
                translate([-6, -0.5, 0])
                    cube([12, 1, armrest_thickness], center=true); // Armrest thickness
            }
        }
    }

    // Wider base for overall stability
    base_width = 70; 
    base_depth = 60; 
    translate([0, 0, -3]) {
        cube([base_width, base_depth, 5], center=true); // Larger base for stability
    }
}
    