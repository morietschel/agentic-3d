
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
        cube([50, 50, 3], center=true);
        translate([-18, -18, -0.1]) 
            cylinder(h=5, r=2, center=true);
    }

    // Ergonomic backrest
    translate([0, -25, 15]) {
        linear_extrude(height=15) {
            polygon(points=[[0, 0], [20, 5], [15, 20], [-15, 20], [-20, 5]], paths=[[0, 1, 2, 3, 4]]);
        }
    }

    // Stylized legs
    for (x = [-20, 20]) {
        for (y = [-20, 20]) {
            translate([x, y, -5]) {
                difference() {
                    cube([10, 10, 30], center=true);
                    translate([-2, -2, 0])
                        cube([14, 14, 2], center=true);
                }
            }
        }
    }

    // Armrests
    for (x = [-1, 1]) {
        translate([24 * x, -25, 10]) {
            difference() {
                scale([1, 0.5, 1])
                    rotate_extrude(angle=180)
                        translate([0, 10, 0])
                            circle(r=3);
                translate([-8, -0.5, 0])
                    cube([16, 1, 5], center=true);
            }
        }
    }

    // Wider base for stability
    translate([0, 0, -3]) {
        cube([60, 60, 5], center=true);
    }

    // Seat surface texture
    for (i = [-14, -6, 6, 14]) {
        for (j = [-14, -6, 6, 14]) {
            translate([i, j, 2]) {
                cylinder(h=2, r=0.6, center=true);
            }
        }
    }
}
    