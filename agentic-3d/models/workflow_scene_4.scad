
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
        cube([45, 45, 3], center=true);
        translate([-20, -20, -0.1]) 
            cylinder(h=5, r=1.5, center=true);
    }

    // Ergonomic backrest
    translate([0, -22, 15]) {
        difference() {
            rotate_extrude(angle=180)
                translate([0, 12, 0])
                    circle(r=20);
            translate([-10, -0.5, 0])
                cube([20, 1, 15], center=true);
        }
    }

    // Stylized legs
    for (x = [-18, 18]) {
        for (y = [-18, 18]) {
            translate([x, y, -7]) {
                difference() {
                    cube([8, 8, 30], center=true);
                    translate([-1, -1, 0])
                        cube([10, 10, 2], center=true);
                }
            }
        }
    }

    // Armrests
    for (x = [-1, 1]) {
        translate([22 * x, -22, 10]) {
            difference() {
                scale([1, 0.5, 1])
                    rotate_extrude(angle=180)
                        translate([0, 8, 0])
                            circle(r=3);
                translate([-7, -0.5, 0])
                    cube([14, 1, 4], center=true);
            }
        }
    }

    // Reinforced base with support for stability
    translate([0, 0, -3]) {
        difference() {
            cube([50, 50, 4], center=true);
            translate([-12, -12, 0])
                cube([24, 24, 4], center=true);
        }
    }

    // Seat surface texture
    for (i = [-11, -4, 4, 11]) {
        for (j = [-11, -4, 4, 11]) {
            translate([i, j, 2]) {
                cylinder(h=2, r=0.5, center=true);
            }
        }
    }
}
    