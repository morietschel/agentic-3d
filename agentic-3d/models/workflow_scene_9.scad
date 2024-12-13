
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
    // Create the outer domed shape of the lampshade
    color("lightyellow", 0.7) {
        rotate_extrude(angle = 360)
            translate([15, 0, 0]) 
                scale([1, 0.5])
                    circle(r = 30);
    }

    // Create the inner cavity for light flow
    color("white", 0.5) {
        rotate_extrude(angle = 360)
            translate([12, 0, 0]) 
                scale([1, 0.5])
                    circle(r = 28);
    }

    // Create the trim at the bottom of the lampshade
    translate([0, 0, -0.5])
        cylinder(h = 1, r = 15, center = true);
    
    // Create a connection base for the lampshade to attach to the lamp stand
    translate([0, 0, -5])
        cylinder(h = 5, r = 5, center = true);

    // Create a light bulb holder with a mounting feature
    translate([0, 0, 5])
        cylinder(h = 10, r = 4, center = true);
}
    