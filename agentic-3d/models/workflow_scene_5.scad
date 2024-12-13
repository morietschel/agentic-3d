
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
    // Create the outer shape of a bell-style lampshade
    cylinder(h = 30, r1 = 25, r2 = 20, center = true);

    // Create the inner hollow for the lampshade with a smooth transition
    translate([0, 0, 2])
        cylinder(h = 28, r1 = 23, r2 = 18, center = true);

    // Create a brim at the bottom edge of the lampshade for stability
    translate([0, 0, -1])
        cylinder(h = 2, r = 27, center = true);

    // Create the base hole for the light bulb fitting
    translate([0, 0, -1])
        cylinder(h = 5, r = 7, center = true);

    // Create the holder for the light bulb
    translate([0, 0, 5])
        cylinder(h = 5, r = 8, center = true);
}
    