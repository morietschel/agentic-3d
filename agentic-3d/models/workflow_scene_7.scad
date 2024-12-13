
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
    // Create the outer shape of a bell-style lampshade with a smooth, flowing profile
    scale([1, 1, 0.9])
        hull() {
            for (i = [0, 1, 2, 3, 4]) {
                rotate(i * 360 / 5)
                    translate([20, 0, 0])
                        circle(r = 28 + 4 * sin(i * 360 / 5 / 4)); // Using sine for smoothness
            }
        }

    // Create the inner hollow for the lampshade with a smooth transition
    scale([1, 1, 0.9])
        translate([0, 0, 2])
            hull() {
                for (i = [0, 1, 2, 3, 4]) {
                    rotate(i * 360 / 5)
                        translate([18, 0, 0])
                            circle(r = 24 + 3 * sin(i * 360 / 5 / 4)); // Inner curves
                }
            }

    // Create a decorative brim at the bottom edge of the lampshade for enhanced visual interest
    translate([0, 0, -1])
        cylinder(h = 3, r = 30, center = true);

    // Create the base hole for the light bulb fitting
    translate([0, 0, -1])
        cylinder(h = 5, r = 8, center = true);

    // Create the holder for the light bulb
    translate([0, 0, 5])
        cylinder(h = 7, r = 6, center = true);
}
    