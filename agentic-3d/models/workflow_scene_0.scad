
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
    translate([0, 0, 0]) {
    // Seat
    difference() {
        cube([40, 40, 5], center=true);
        translate([5, 5, -0.5])
            cube([30, 30, 6], center=true);
    }

    // Backrest
    translate([0, 20, 5]) {
        difference() {
            cube([40, 5, 30], center=true);
            translate([-5, -0.5, 5])
                cube([30, 5, 31], center=true);
        }
    }

    // Legs
    for (x = [-15, 15]) {
        for (y = [-15, 15]) {
            translate([x, y, -5]) {
                cube([5, 5, 20], center=true);
            }
        }
    }

    // Armrests
    translate([20, 0, 5]) {
        rotate([0, 0, 90]) {
            difference() {
                cube([15, 5, 15], center=true);
                translate([-5, -0.5, 5])
                    cube([10, 5, 16], center=true);
            }
        }
    }
    translate([-20, 0, 5]) {
        rotate([0, 0, 90]) {
            difference() {
                cube([15, 5, 15], center=true);
                translate([-5, -0.5, 5])
                    cube([10, 5, 16], center=true);
            }
        }
    }
}
    