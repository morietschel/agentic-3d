
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
    // Define the ergonomic seat of the chair with improved proportions
    translate([0, 0, 5])
    difference() {
        scale([1.1, 1.1, 0.5])
        cube([45, 45, 8], center=true);
        translate([0, 0, -0.5])
        scale([1, 1, 0.5])
        cube([43, 43, 8], center=true);
    }

    // Create a more defined and stylish curved backrest
    translate([0, -30, 10])
    rotate([25, 0, 0])
    difference() {
        scale([1, 1, 0.5])
        rotate_extrude(angle=180)
        translate([15, 0, 0])
        circle(r=7);
        translate([-10, -10, 5])
        rotate_extrude(angle=180)
        translate([15, 0, 0])
        circle(r=8);
    }

    // Design stable splayed legs for aesthetic and strength
    for (x = [-17.5, 17.5]) {
        translate([x, -23, 0])
        rotate([0, 0, -15 * sign(x)]) {
            cylinder(r=2, h=25, center=false);
        }
    }

    // Adding tapered rear legs for style and stability
    for (x = [-17.5, 17.5]) {
        translate([x, 23, 0])
        rotate([0, 15, 0]) {
            cylinder(r=2, h=30, center=false);
        }
    }

    // Optional modern armrests with smooth lines
    for (x = [-30, 30]) {
        translate([x, 0, 12])
        rotate([0, 0, 15 * sign(x)])
        linear_extrude(height=5)
        offset(r=0.5) {
            polygon(points=[[0,0], [22,0], [18,-3], [4,-3]]);
        }
    }

    // Adding decorative cutouts to enhance aesthetic appeal
    translate([-22, 0, 6])
    difference() {
        cube([10, 45, 2], center=true);
        translate([1, 4, 0])
        cube([8, 36, 2], center=true);
    }
}
    