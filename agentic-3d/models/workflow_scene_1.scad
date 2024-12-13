
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
    // Create the outer flared shape of the lampshade
    difference() {
        rotate_extrude(angle = 360) 
            translate([30, 0, 0]) 
                polygon(points=[[0, 0], [0, 20], [15, 30], [30, 20], [30, 0]]);
        translate([0, 0, 1]) 
            rotate_extrude(angle = 360) 
                translate([22, 0, 0]) 
                    polygon(points=[[0, 0], [0, 20], [12, 28], [20, 20], [20, 0]]);
    }
    
    // Create the base hole for the light bulb fitting
    translate([0, 0, -1])
        cylinder(h = 5, r = 10, center = true);
}
    