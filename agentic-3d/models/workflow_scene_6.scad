
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
        cube([50, 50, 3], center=true); // Seat
        translate([-18, -18, -0.1]) 
            cylinder(h=5, r=2, center=true); // Cutout for lighter seat
    }

    // Ergonomic backrest with a slanted design
    translate([0, -25, 12]) {
        linear_extrude(height=12) {
            polygon(points=[[0, 0], [20, 5], [30, 20], [30, 0], [-30, 0], [-30, 20], [-20, 5]], paths=[[0, 1, 2, 3, 4, 5, 6]]);
        }
    }

    // Simplified legs with wider base for stability
    for (x = [-20, 20]) {
        translate([x, -20, -5]) {
            cube([8, 8, 25], center=true); // Simplified leg
        }
    }
    for (x = [-20, 20]) {
        translate([x, 20, -5]) {
            cube([8, 8, 25], center=true); // Another leg
        }
    }

    // Armrests with ergonomic curve
    for (x = [-1, 1]) {
        translate([24 * x, -25, 10]) {
            difference() {
                scale([1, 0.5, 1])
                    rotate_extrude(angle=180)
                        translate([0, 8, 0]) // Adjusted to produce a nicer armrest
                        circle(r=3);
                translate([-6, -0.5, 0])
                    cube([12, 1, 5], center=true); // Thinner armrest block for aesthetic
            }
        }
    }

    // Wider base for overall stability
    translate([0, 0, -3]) {
        cube([65, 65, 5], center=true); // Larger base
    }
}
    