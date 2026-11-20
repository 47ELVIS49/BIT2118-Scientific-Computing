# Task 12 – Polynomial and Nonlinear Equation Solving

## B. Inputs and Mathematical Operation
**Inputs:** System of two nonlinear equations (circle and parabola) and different initial guesses.  
**Operation:** Use `scipy.optimize.root` to find intersection points.

## C. Parameter Change
Changed the circle equation from x² + y² = 4 to x² + y² = 9 (larger circle).  
Result: The intersection points move farther from the origin.

## D. Meaning of the Output
The solutions are the points where the circle and the parabola intersect. Residuals near zero confirm the points satisfy both equations.

## E. Modified Real-World Case
**New problem:** Finding intersection of a robot path (parabola) with a safety boundary (circle).  
**Assumptions:** Same mathematical form, different radius.  
**Interpretation:** Gives the coordinates where the path touches the boundary.