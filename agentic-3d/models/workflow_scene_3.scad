
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
    difference() {
    // Create the outer flared conical shape of the lampshade
    hull() {
        for (angle = [0, 360, 720]) {
            rotate([0, 0, angle])
                translate([20, 0, 0])
                    scale([1, 1 - angle / 720, 1])
                        cylinder(h = 30, r = 25, center = true);
        }
    }

    // Create the inner hollow for the lampshade
    translate([0, 0, 1])
        hull() {
            for (angle = [0, 360, 720]) {
                rotate([0, 0, angle])
                    translate([15, 0, 0])
                        scale([1, 1 - angle / 720, 1])
                            cylinder(h = 30, r = 20, center = true);
            }
        }

    // Create the base hole for the light bulb fitting
    translate([0, 0, -1])
        cylinder(h = 8, r = 6, center = true);

    // Add decorative elements (seams for realism)
    for (i = [0:5]) {
        translate([0, 0, i * 6])
            rotate_extrude(angle = 360)
                translate([0, 15, 0])
                    circle(r = 0.6);
    }
}
    