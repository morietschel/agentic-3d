
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
    cylinder(h = 50, r = 30, center = true);
    translate([0, 0, 1])
        cylinder(h = 51, r = 25, center = true);
}
    