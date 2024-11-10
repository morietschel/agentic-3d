
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
    translate([0, 0, 5])
    difference() {
        cube([50, 50, 5], center=true); // Main seat
        translate([0, 0, -1])
        cube([48, 48, 6], center=true); // Cutout for better contact with the print bed
    }

    // Backrest
    translate([0, -25, 10])
    rotate([15, 0, 0])
    cube([50, 5, 30], center=true); // Angled backrest

    // Side supports for the backrest
    translate([-26, -25, 10])
    cube([4, 40, 10], center=true); // Left support
    translate([26, -25, 10])
    cube([4, 40, 10], center=true); // Right support

    // Front legs
    translate([-20, -20, 0])
    cube([5, 5, 25], center=true); // Left front leg
    translate([-20, 20, 0])
    cube([5, 5, 25], center=true); // Right front leg

    // Rear legs
    translate([20, -20, 0])
    cube([5, 5, 25], center=true); // Left rear leg
    translate([20, 20, 0])
    cube([5, 5, 25], center=true); // Right rear leg

    // Optional Armrests
    translate([-30, -15, 15])
    rotate([0, 0, -15])
    cube([30, 5, 5], center=true); // Left armrest
    translate([30, -15, 15])
    rotate([0, 0, 15])
    cube([30, 5, 5], center=true); // Right armrest
}
    