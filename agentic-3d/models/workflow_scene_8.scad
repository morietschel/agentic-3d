
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
    // Define the ergonomic seat of the chair
    translate([0, 0, 4])
    difference() {
        cube([48, 48, 6], center=true);
        translate([0, 0, -0.5])
        cube([46, 46, 6], center=true);
    }

    // Curved backrest for enhanced comfort and style
    translate([0, -32, 10])
    rotate([20, 0, 0]) {
        difference() {
            scale([1.1, 1, 0.5])
            rotate_extrude(angle=180)
            translate([15, 0, 0])
            circle(r=9);
            translate([-10, -10, 4])
            rotate_extrude(angle=180)
            translate([15, 0, 0])
            circle(r=11);
        }
    }

    // Thickened and stylish legs for stability and aesthetic
    for (x = [-20, 20]) {
        translate([x, -25, 0])
        rotate([0, 0, -10 * sign(x)]) {
            cylinder(r=3, h=30, center=false);
        }
    }

    for (x = [-20, 20]) {
        translate([x, 25, 0])
        rotate([0, 10, 0]) {
            cylinder(r=3, h=35, center=false);
        }
    }

    // Modern ergonomic armrests
    for (x = [-30, 30]) {
        translate([x, 0, 12])
        rotate([0, 0, 15 * sign(x)])
        linear_extrude(height=6) {
            offset(r=0.5) {
                polygon(points=[[0,0], [24,0], [20,-4], [5,-4]]);
            }
        }
    }

    // Adding structural support under the seat
    translate([0, 0, 0]) {
        cube([6, 6, 4], center=true);
        translate([0, -24, 0])
        cube([6, 6, 4], center=true);
    }

    // Adding decorative elements
    translate([-15, -15, 5])
    difference() {
        cube([30, 30, 1], center=true);
        translate([-4, -10, 0])
        cube([8, 20, 1], center=true);
    }
}
    