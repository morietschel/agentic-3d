
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
    // Create the outer flared conical shape of the lampshade with a curved surface
    outer_cone = function(h, r1, r2) {
        for (i = [0 : 10]) {
            angle = i * 36;
            rotate([0, 0, angle])
                translate([0, 0, 0])
                    scale([1, 1, h * (1 - i / 10)])
                        cylinder(h = h, r = r1 + i * (r2 - r1) / 10, center = true);
        }
    };

    outer_cone(30, 20, 25);

    // Create the inner hollow for the lampshade with varying thickness
    inner_cone = function(h, r1, r2) {
        for (i = [0 : 10]) {
            angle = i * 36;
            rotate([0, 0, angle])
                translate([0, 0, 1])
                    scale([1, 1, h * (1 - i / 10)])
                        cylinder(h = h, r = r1 + (i + 1) * (r2 - r1) / 10, center = true);
        }
    };

    inner_cone(30, 15, 20);

    // Create the base hole for the light bulb fitting
    translate([0, 0, -1])
        cylinder(h = 5, r = 6, center = true);

    // Add decorative elements (seams for realism)
    for (i = [0:5]) {
        translate([0, 0, i * 6])
            rotate_extrude(angle = 360)
                translate([0, 15, 0])
                    circle(r = 0.6);
    }

    // Create the mounting ring at the top of the lampshade
    translate([0, 0, 30])
        rotate_extrude(angle = 360)
            circle(r = 5);
}
    