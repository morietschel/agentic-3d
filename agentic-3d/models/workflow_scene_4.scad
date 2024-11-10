
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
    // Seat with a comfortable shape
    translate([0, 0, 5])
    difference() {
        scale([1, 1, 0.5])
        cylinder(r=25, h=15);
        translate([0, 0, -1])
        scale([1, 1, 0.5])
        cylinder(r=24.5, h=15);
    }

    // Angled ergonomic backrest
    translate([0, -25, 10])
    rotate([20, 0, 0])
    linear_extrude(height=30) {
        polygon(points=[[0,0], [-20,20], [20,20]]);
    }

    // Front legs with a splayed design
    for (x = [-18, 18]) {
        translate([x, -20, 0]) // Adjusting front legs position
        linear_extrude(height=25) {
            polygon(points=[[0,0], [3,0], [2,-10], [-2,-10], [-3,0]]);
        }
    }

    // Rear legs, slightly thicker and taller for stability
    for (x = [-18, 18]) {
        translate([x, 20, 0]) // Adjusting rear legs position
        linear_extrude(height=32) {
            polygon(points=[[0,0], [4,0], [3,-12], [-3,-12], [-4,0]]);
        }
    }

    // Curved armrests for added comfort
    for (x = [-30, 30]) {
        translate([x, 0, 15])
        rotate([0, 0, 15 * sign(x)])
        linear_extrude(height=5)
        offset(r=1) {
            polygon(points=[[0,0], [25,0], [20,-5], [5,-5]]);
        }
    }
}
    