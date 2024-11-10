
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
    // Define the seat of the chair with a broader shape for comfort
    translate([0, 0, 5])
    difference() {
        scale([1, 1, 0.5])
        cube([50, 50, 10], center=true);
        translate([0, 0, -1])
        scale([1, 1, 0.5])
        cube([48, 48, 10], center=true);
    }

    // Create an ergonomic backrest with a distinct curve
    translate([0, -25, 15])
    rotate([15, 0, 0])
    difference() {
        scale([1, 1, 0.5])
        rotate_extrude(angle=180)
        translate([20, 0, 0])
        circle(r=5);
        translate([-10, -10, 5])
        rotate_extrude(angle=180)
        translate([20, 0, 0])
        circle(r=6);
    }

    // Design functional, straight legs for stability
    for (x = [-20, 20]) {
        translate([x, -25, 0])
        cube([5, 5, 25], center=false);
    }

    // Adding the rear legs with a slight angle for aesthetics
    for (x = [-20, 20]) {
        translate([x, 25, 0])
        rotate([0, 20, 0])
        cube([5, 5, 30], center=false);
    }

    // Optional armrests, designed to enhance comfort
    for (x = [-30, 30]) {
        translate([x, 0, 15])
        rotate([0, 0, 15 * sign(x)])
        linear_extrude(height=5)
        offset(r=1) {
            polygon(points=[[0,0], [25,0], [20,-5], [5,-5]]);
        }
    }
}
    