
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
    // Seat with rounded edges
    difference() {
        hull() {
            for (a = [0 : 10 : 360]) {
                r = 20 + (5 * sin(a));
                rotate([0, 0, a])
                    translate([0, r, 0])
                        circle(r=2, center=true);
            }
        }
        translate([0, 0, -0.5])
            cube([40, 40, 1], center=true);
    }

    // Backrest with curve
    translate([0, 15, 5]) {
        difference() {
            rotate([0, 90, 0]) {
                scale([0.5, 1, 1])
                    rotate_extrude(angle=180)
                        translate([0, 10, 0])
                            circle(r=20);
            }
            translate([-5, -0.5, 5])
                cube([30, 5, 31], center=true);
        }
    }

    // Wider and tapered legs for stability
    for (x = [-15, 15]) {
        for (y = [-15, 15]) {
            translate([x, y, -5]) {
                difference() {
                    scale([1, 1, 1.5])
                        cube([5, 5, 20], center=true);
                    translate([-2, -2, 0])
                        cube([9, 9, 1], center=true);
                }
            }
        }
    }

    // Curved armrests with detailing
    for (x = [-1, 1]) {
        translate([20 * x, 0, 10]) {
            difference() {
                rotate_extrude(angle=180)
                    translate([0, 12, 0])
                        circle(r=1);
                translate([-5, -0.5, 0])
                    cube([12, 5, 4], center=true);
            }
        }
    }

    // Textured detail on seat
    for (i = [-10, 10]) {
        for (j = [-10, 10]) {
            translate([i, j, 0]) {
                cube([1, 1, 0.5], center=true);
            }
        }
    }
}
    