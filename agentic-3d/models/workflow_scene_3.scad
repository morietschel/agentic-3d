
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
    // Seat with a slight curve for comfort
    translate([0, 0, 5])
    difference() {
        hull() {
            translate([-25, -25, 0]) circle(r=25);
            translate([25, -25, 0]) circle(r=25);
            translate([-25, 25, 0]) circle(r=25);
            translate([25, 25, 0]) circle(r=25);
        }
        translate([0, 0, -1])
        hull() {
            translate([-24, -24, 0]) circle(r=24);
            translate([24, -24, 0]) circle(r=24);
            translate([-24, 24, 0]) circle(r=24);
            translate([24, 24, 0]) circle(r=24);
        }
    }

    // Ergonomic backrest
    translate([0, -25, 15])
    rotate([15, 0, 0])
    linear_extrude(height=30) {
        polygon(points=[[0,0], [-25,30], [25,30]]);
    }

    // Front legs with a tapered design
    translate([-15, -15, 0])
    linear_extrude(height=25) {
        polygon(points=[[0,0], [5,0], [3,-10], [-3,-10], [-5,0]]);
    } 
    translate([-15, 15, 0])
    linear_extrude(height=25) {
        polygon(points=[[0,0], [5,0], [3,-10], [-3,-10], [-5,0]]);
    } 

    // Rear legs with a slightly larger tapered design
    translate([15, -15, 0])
    linear_extrude(height=30) {
        polygon(points=[[0,0], [6,0], [4,-12], [-4,-12], [-6,0]]);
    } 
    translate([15, 15, 0])
    linear_extrude(height=30) {
        polygon(points=[[0,0], [6,0], [4,-12], [-4,-12], [-6,0]]);
    }

    // Optional curved armrests
    translate([-30, 0, 15])
    rotate([0, 0, 30])
    linear_extrude(height=5)
    offset(r=5) {
        polygon(points=[[0,0], [25,0], [20,-5], [5,-5]]);
    }
    translate([30, 0, 15])
    rotate([0, 0, -30])
    linear_extrude(height=5)
    offset(r=5) {
        polygon(points=[[0,0], [25,0], [20,-5], [5,-5]]);
    }
}
    