
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
    difference() {
        hull() {
            for (a = [0 : 10 : 360]) {
                r = 22 + (2 * sin(a));
                rotate([0, 0, a])
                    translate([0, r, 0])
                        circle(r=4, center=true);
            }
        }
        translate([0, 0, -1])
            cube([50, 50, 1], center=true);
    }

    // Ergonomic backrest
    translate([0, 0, 12]) {
        difference() {
            rotate([0, 90, 0]) {
                scale([0.4, 1, 1])
                    rotate_extrude(angle=180)
                        translate([0, 10, 0])
                            circle(r=18);
            }
            translate([-9, -0.5, 0])
                cube([34, 5, 22], center=true);
        }
    }
    
    // Stable legs
    for (x = [-16, 16]) {
        for (y = [-16, 16]) {
            translate([x, y, -5]) {
                difference() {
                    cube([10, 10, 25], center=true);
                    translate([-2, -2, 0])
                        cube([14, 14, 2], center=true);
                }
            }
        }
    }

    // Stylish armrests
    for (x = [-1, 1]) {
        translate([22 * x, 0, 15]) {
            difference() {
                rotate_extrude(angle=180)
                    translate([0, 12, 0])
                        circle(r=1.5);
                translate([-5, -0.5, 0])
                    cube([12, 5, 3], center=true);
            }
        }
    }

    // Textured seat surface
    for (i = [-12, -4, 4, 12]) {
        for (j = [-12, -4, 4, 12]) {
            translate([i, j, 0.5]) {
                difference() {
                    cylinder(h=1, r=0.75, center=true);
                    translate([-1, -1, -0.5])
                        cube([2, 2, 1], center=true);
                }
            }
        }
    }
}
    