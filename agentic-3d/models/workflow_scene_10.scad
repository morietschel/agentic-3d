
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
    // Create the outer bell-shaped lampshade
    color("lightyellow", 0.7) {
        rotate_extrude(angle = 360)
            translate([15, 0, 0]) 
                scale([1, 0.6])
                    polygon(points=[[0,0], [20,0], [12,30], [8,30]]);
    }

    // Create the inner cavity for light flow
    color("white", 0.5) {
        rotate_extrude(angle = 360)
            translate([12, 0, 0]) 
                scale([1, 0.6])
                    polygon(points=[[0,0], [16,0], [10,28], [6,28]]);
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

    // Create a socket ring for attachment
    translate([0, 0, 10])
        cylinder(h = 1, r = 6, center = true);
}
    