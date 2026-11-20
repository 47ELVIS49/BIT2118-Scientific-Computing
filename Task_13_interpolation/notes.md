# Task 13 – Interpolation

## B. Inputs and Mathematical Operation
**Inputs:** Hourly temperature measurements.  
**Operations:** Linear interpolation and Cubic Spline interpolation to estimate temperature every 10 minutes.

## C. Parameter Change
Changed the temperature at 12:00 from 25.0 to 27.0.  
Result: Both interpolated curves rise higher around midday.

## D. Meaning of the Output + Graph
The graph shows the original hourly points and the continuous curves estimated by linear and cubic methods. Cubic spline is smoother.

## E. Modified Real-World Case
**New problem:** Estimating missing humidity readings between hourly sensor data.  
**Assumptions:** Same times, different humidity values.  
**Interpretation:** Fills in the gaps for continuous monitoring.