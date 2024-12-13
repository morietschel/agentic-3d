
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
            translate([25, 0, 0])
                polygon(points=[[0, 0], [0, 30], [12, 45], [25, 30], [25, 0]]);
        translate([0, 0, 1])
            rotate_extrude(angle = 360)
                translate([20, 0, 0])
                    polygon(points=[[0, 0], [0, 28], [10, 40], [18, 28], [18, 0]]);
    }
    
    // Create the base hole for the light bulb fitting
    translate([0, 0, -1])
        cylinder(h = 5, r = 8, center = true);
    
    // Add seams for realism
    for (i = [0:5]) {
        translate([0, 0, i * 6])
            rotate_extrude(angle = 360)
                translate([0, 20, 0])
                    circle(r = 0.5);
    }
}
    