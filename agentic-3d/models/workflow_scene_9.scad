
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
    union() {
    // Base seat of the chair
    translate([0, 0, 0]) {
        difference() {
            cube([50, 50, 4], center = true);
            translate([0, 0, -1])
            cube([48, 48, 4], center = true);
        }
    }

    // Backrest with ergonomic curve
    translate([0, -25, 4]) {
        rotate([-10, 0, 0]) {
            difference() {
                scale([1, 1, 0.5])
                rotate_extrude(angle = 180)
                translate([15, 0, 0])
                circle(r = 10);
                translate([-10, -10, 4])
                rotate_extrude(angle = 180)
                translate([15, 0, 0])
                circle(r = 12);
            }
        }
    }

    // Chair legs
    for (x = [-20, 20]) {
        for (y = [-20, 20]) {
            translate([x, y, -10]) {
                cylinder(r = 4, h = 15, center = false);
            }
        }
    }

    // Armrests with rounded ends
    for (x = [-24, 24]) {
        translate([0, x, 6]) {
            rotate([0, 0, 0]) {
                linear_extrude(height = 2) {
                    offset(delta = 0.5) {
                        polygon(points=[[0, 0], [20, 0], [18, -4], [2, -4]]);
                    }
                }
            }
        }
    }

    // Support crossbars
    translate([0, 0, -2]) {
        cube([34, 2, 2], center = true);
        translate([0, 0, -4])
        cube([2, 34, 2], center = true);
    }

    // Optional decorative cutouts
    translate([-15, -15, 2]) {
        difference() {
            cube([30, 30, 1], center = true);
            translate([-3, -10, 0])
            cube([6, 20, 1], center = true);
        }
    }
}
    