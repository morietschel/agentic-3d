
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
    str = "union() {\n" +
"    // Seat\n" +
"    translate([0, 0, 30])\n" +
"    cube([60, 60, 5], center=true);\n" +
"\n" +
"    // Backrest\n" +
"    translate([0, -30, 35])\n" +
"    rotate([0, 0, 15])\n" +
"    cube([60, 5, 40], center=true);\n" +
"\n" +
"    // Legs\n" +
"    translate([-25, -25, 0])\n" +
"    rotate([0, 0, 0])\n" +
"    cube([5, 5, 30], center=true);\n" +
"    translate([-25, 25, 0])\n" +
"    cube([5, 5, 30], center=true);\n" +
"    translate([25, -25, 0])\n" +
"    cube([5, 5, 30], center=true);\n" +
"    translate([25, 25, 0])\n" +
"    cube([5, 5, 30], center=true);\n" +
"}";
    