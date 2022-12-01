1) NOMES working on Windows (about $1/2$ of the ppl)
2) Include construct recursively (cannot be done)
3) Will make recursive use of include work
Unexpected Black Face -> Default colors
-> So it means you need to reverse sequence of vertices
4) Need to use merge STL option
5) Printers -> Go to Jacobs Hall
6) New SLiders -> My scale -. List scale -> Sweep (add sliders)
7) Make smooth curve using b-spline construct
8) Make sure bspline is geometrically continous
9) Mintorsion
Sweep: Need cross-section
: Need path
Azimuth: Change degree of cross section
Torsion -> Angle of cross section start(different) with end
Mintorsion -> Take cross-section, and just extrude the thing from one vertice to another
Figure 8 -> Flipped cross-section loop
- local influencce of sweep
- Azimuth -> starting twist
- Twist (how much turn(total) in tlhe entire curve)

Azimuth -> warp extra 20 degree positive, 30 degree negative, plus 10, negative 10, using the control points to do so. (turn in/out)

Scale in control point, (x,y), scale cross-section.
Never used option to have sweep cross section be not perpendicular to sweep path

No of segments make as little as possible
Quadrilateral control polygon
Min no of segments = 12
Shouldn't have less than or equal to 7 segments. Order of bspline = 3,4,5
Crash -> more prone to crash
