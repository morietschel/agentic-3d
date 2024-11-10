
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
    translate([0, 0, 5])
    difference() {
        scale([1.1, 1.1, 0.5])
        cube([48, 48, 8], center=true);
        translate([0, 0, -0.5])
        scale([1, 1, 0.5])
        cube([46, 46, 8], center=true);
    }

    // Create a curved backrest for comfort
    translate([0, -25, 13])
    rotate([20, 0, 0])
    difference() {
        scale([1, 1, 0.5])
        rotate_extrude(angle=180)
        translate([15, 0, 0])
        circle(r=6);
        translate([-10, -10, 10])
        rotate_extrude(angle=180)
        translate([15, 0, 0])
        circle(r=7);
    }

    // Design strong, slightly tapered legs for aesthetic and stability
    for (x = [-20, 20]) {
        translate([x, -25, 0])
        rotate([0, 0, 10 * sign(x)]) {
            cube([5, 5, 25], center=false);
        }
    }

    // Adding angled rear legs for style
    for (x = [-20, 20]) {
        translate([x, 25, 0])
        rotate([0, 15, 0])
        cube([5, 5, 30], center=false);
    }

    // Optional armrests with a modern curvature
    for (x = [-30, 30]) {
        translate([x, 0, 12])
        rotate([0, 0, 25 * sign(x)])
        linear_extrude(height=5)
        offset(r=1) {
            polygon(points=[[0,0], [25,0], [20,-5], [5,-5]]);
        }
    }

    // Adding decorative cutouts to enhance aesthetic
    translate([-25, 0, 8])
    difference() {
        cube([10, 40, 2], center=true);
        translate([1, 3, 0])
        cube([8, 34, 2], center=true);
    }
}
    