
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
    // Seat
    translate([0, 0, 10])
    cube([50, 50, 5], center=true);

    // Backrest
    translate([0, -25, 15])
    rotate([0, 0, 10])
    cube([54, 5, 30], center=true);
    
    // Side supports for the backrest
    translate([-27, -25, 15])
    rotate([0, 0, 0])
    cube([5, 40, 10], center=true);
    translate([27, -25, 15])
    cube([5, 40, 10], center=true);

    // Front leg structure
    translate([-20, -20, 0])
    rotate([0, 0, 0])
    cube([5, 5, 30], center=true);
    translate([-20, 20, 0])
    cube([5, 5, 30], center=true);
    
    // Rear leg structure
    translate([20, -20, 0])
    cube([5, 5, 30], center=true);
    translate([20, 20, 0])
    cube([5, 5, 30], center=true);
}
    