//RocketLib
module basic_bodytube(length, radius){
    cylinder(r=radius, h=length, center=true);
}
module basic_transition(length, radius){
    cylinder(r=radius, h=length, center=true);
}
module conical_transition(length, fore_radius, aft_radius){
    cylinder(r=fore_radius, r2 =aft_radius, h=length, center=true);
}
module cone_cone(R = 5, L = 10, s = 500){
// CONICAL NOSE CONE
//
// Formula: y = x * R / L; 
//
//     but there's an easier way...

echo(str("CONICAL NOSE CONE"));    
echo(str("R = ", R)); 
echo(str("L = ", L)); 
echo(str("s = ", s)); 

cylinder(h = L, r1 = R, r2 = 0, center = false, $fn = s);
    
}
module cone_parabolic(R = 5, L = 10, K = 0.5, s = 500){
// PARABOLIC NOSE CONE
//
// Formula: y = R * ((2 * (x / L)) - (K * pow((x / L),2)) / (2 - K);
//
// Parameters:
// K = 0 for cone
// K = 0.5 for 1/2 parabola
// K = 0.75 for 3/4 parabola
// K = 1 for full parabola

echo(str("PARABOLIC NOSE CONE"));
echo(str("R = ", R)); 
echo(str("L = ", L)); 
echo(str("K = ", K)); 
echo(str("s = ", s)); 
    
if (K >= 0 && K <= 1){

        inc = 1/s;

        rotate_extrude(convexity = 10, $fn = s)
        for (i = [1 : s]){
            
            x_last = L * (i - 1) * inc;
            x = L * i * inc;

            y_last = R * ((2 * ((x_last)/L)) - (K * pow(((x_last)/L), 2))) / (2 - K);
            y = R * ((2 * (x/L)) - (K * pow((x/L), 2))) / (2 - K);

            polygon(points = [[y_last, 0], [y, 0], [y, L - x], [y_last, L - x_last]], convexity = 10);
        }
    } else echo(str("ERROR: K = ", K, ", but K must fall between 0 and 1 (inclusive)."));
}
module cone_haack(C = 0, R = 5, L = 10, s = 500){

// SEARS-HAACK BODY NOSE CONE:
//
// Parameters:
// C = 1/3: LV-Haack (minimizes supersonic drag for a given L & V)
// C = 0: LD-Haack (minimizes supersonic drag for a given L & D), also referred to as Von Kármán
//
// Formulae (radians):
// theta = acos(1 - (2 * x / L));
// y = (R / sqrt(PI)) * sqrt(theta - (sin(2 * theta) / 2) + C * pow(sin(theta),3));

echo(str("SEARS-HAACK BODY NOSE CONE"));
echo(str("C = ", C)); 
echo(str("R = ", R)); 
echo(str("L = ", L)); 
echo(str("s = ", s)); 

TORAD = PI/180;
TODEG = 180/PI;

inc = 1/s;

rotate_extrude(convexity = 10, $fn = s)
for (i = [1 : s]){
    x_last = L * (i - 1) * inc;
    x = L * i * inc;

    theta_last = TORAD * acos((1 - (2 * x_last/L)));
    y_last = (R/sqrt(PI)) * sqrt(theta_last - (sin(TODEG * (2*theta_last))/2) + C * pow(sin(TODEG * theta_last), 3));

    theta = TORAD * acos(1 - (2 * x/L));
    y = (R/sqrt(PI)) * sqrt(theta - (sin(TODEG * (2 * theta)) / 2) + C * pow(sin(TODEG * theta), 3));

    rotate([0, 0, -90]) polygon(points = [[x_last - L, 0], [x - L, 0], [x - L, y], [x_last - L, y_last]], convexity = 10);
}
}
module cone_power_series(n = 0.5, R = 5, L = 10, s = 500){
// POWER SERIES NOSE CONE:
//
// Formula: y = R * pow((x / L), n) for 0 <= n <= 1
//
// Parameters:
// n = 1 for a cone
// n = 0.75 for a 3/4 power
// n = 0.5 for a 1/2 power (parabola)
// n = 0 for a cylinder

echo(str("POWER SERIES NOSE CONE"));
echo(str("n = ", n)); 
echo(str("R = ", R)); 
echo(str("L = ", L)); 
echo(str("s = ", s)); 

inc = 1/s;

rotate_extrude(convexity = 10, $fn = s)
for (i = [1 : s]){

    x_last = L * (i - 1) * inc;
    x = L * i * inc;

    y_last = R * pow((x_last/L), n);
    y = R * pow((x/L), n);

    rotate([0, 0, 90]) polygon(points = [[0,y_last],[0,y],[L-x,y],[L-x_last,y_last]], convexity = 10);
}
}
module cone_elliptical(n = 0.5, R = 5, L = 10, s = 500){
// ELLIPTICAL NOSE CONE:
//
// Formula: y = R * sqrt(1 - pow((x / L), 2));

echo(str("ELLIPTICAL NOSE CONE"));    
echo(str("n = ", n)); 
echo(str("R = ", R)); 
echo(str("L = ", L)); 
echo(str("s = ", s)); 

inc = 1/s;

rotate_extrude(convexity = 10, $fn = s)
for (i = [1 : s]){

    x_last = L * (i - 1) * inc;
    x = L * i * inc;

    y_last = R * sqrt(1 - pow((x_last/L), 2));
    y = R * sqrt(1 - pow((x/L), 2));

    rotate([0,0,90]) polygon(points = [[0, y_last], [0, y], [x, y], [x_last, y_last]], convexity = 10);
}
}
module cone_ogive_tan(R = 5, L = 10, s = 500){
// TANGENT OGIVE
//
//

echo(str("TANGENT OGIVE"));    
echo(str("R = ", R)); 
echo(str("L = ", L)); 
echo(str("s = ", s)); 

rho = (pow(R,2) + pow(L,2)) / (2 * R);

inc = 1/s;

rotate_extrude(convexity = 10, $fn = s)
for (i = [1 : s]){
    x_last = L * (i - 1) * inc;
    x = L * i * inc;

    y_last = sqrt(pow(rho,2) - pow((L - x_last), 2)) + R - rho;

    y = sqrt(pow(rho,2) - pow((L - x), 2)) + R - rho;

    rotate([0, 0, -90]) polygon(points = [[x_last - L, 0], [x - L, 0], [x - L, y], [x_last - L, y_last]], convexity = 10);
}
}
