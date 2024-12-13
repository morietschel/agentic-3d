
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
    // Create the outer conical shape of the lampshade
    color("yellow", 0.5) {
        rotate_extrude(angle = 360)
            translate([15, 0, 0]) 
                circle(r = 30);
    }

    // Create the inner hollow for the lampshade
    color("white", 0.3) {
        rotate_extrude(angle = 360)
            translate([12, 0, 0]) 
                circle(r = 28);
    }

    // Create the base connection for the lampshade to the lamp stand
    translate([0, 0, -5])
        cylinder(h = 5, r1 = 7, r2 = 0, center = true);

    // Create a light bulb holder in the center of the lampshade
    translate([0, 0, 5])
        cylinder(h = 10, r = 4, center = true);
}
    