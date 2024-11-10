
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

    // Backrest with ergonomic angle
    translate([0, -25, 4]) {
        rotate([15, 0, 0]) {
            translate([-20, 0, 0])
            linear_extrude(height = 4) {
                polygon(points=[[0, 0], [40, 0], [20, 20]]);
            }
        }
    }

    // Chair legs
    for (x = [-20, 20]) {
        for (y = [-20, 20]) {
            translate([x, y, -10]) {
                cylinder(r = 6, h = 15, center = false);
            }
        }
    }

    // Armrests with a smooth profile
    for (x = [-24, 24]) {
        translate([0, x, 6]) {
            rotate([0, 0, 0]) {
                linear_extrude(height = 3) {
                    offset(delta = 0.5) {
                        polygon(points=[[0, 0], [20, 0], [18, 4], [2, 4]]);
                    }
                }
            }
        }
    }

    // Cross supports for stability
    translate([0, 0, -2]) {
        difference() {
            cube([36, 3, 2], center = true);
            translate([0, 0, -3])
            cube([2, 36, 2], center = true);
        }
    }

    // Decorative side cutouts
    translate([-15, -15, 2]) {
        difference() {
            cube([30, 30, 2], center = true);
            translate([-5, -12, 0])
            cube([10, 24, 2], center = true);
        }
    }
}
    