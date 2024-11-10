
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
    // Seat with refined curves
    difference() {
        hull() {
            for (a = [0 : 10 : 360]) {
                r = 25 + (3 * sin(a));
                rotate([0, 0, a])
                    translate([0, r, 0])
                        circle(r=3, center=true);
            }
        }
        translate([0, 0, -1])
            cube([50, 50, 1], center=true);
    }

    // Ergonomic backrest
    translate([0, 20, 5]) {
        difference() {
            rotate([0, 90, 0]) {
                scale([0.6, 1, 1])
                    rotate_extrude(angle=180)
                        translate([0, 12, 0])
                            circle(r=25);
            }
            translate([-8, -0.5, 0])
                cube([40, 5, 30], center=true);
        }
    }
    
    // Customized legs for stability and support
    for (x = [-20, 20]) {
        for (y = [-20, 20]) {
            translate([x, y, -5]) {
                difference() {
                    scale([1, 1, 1.2])
                        cube([8, 8, 25], center=true);
                    translate([-3, -3, 0])
                        cube([14, 14, 2], center=true);
                }
            }
        }
    }

    // Stylish armrests with additional contour
    for (x = [-1, 1]) {
        translate([22 * x, 0, 12]) {
            difference() {
                rotate_extrude(angle=180)
                    translate([0, 15, 0])
                        circle(r=2);
                translate([-7, -0.5, 0])
                    cube([16, 5, 5], center=true);
            }
        }
    }

    // Textured detailing on seat surface
    for (i = [-15, -5, 5, 15]) {
        for (j = [-15, -5, 5, 15]) {
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
    