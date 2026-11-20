# Task 14 – Curve Fitting and Approximation

## B. Inputs and Mathematical Operation
**Inputs:** Concurrent users and measured response times.  
**Operation:** Fit a quadratic model using least-squares (`curve_fit`).

## C. Parameter Change
Changed the last response time from 305 to 280.  
Result: The fitted curve becomes less steep at high user counts.

## D. Meaning of the Output + Graph
The quadratic equation approximates how response time grows with load. RMSE shows the average fitting error. The graph compares real measurements with the model.

## E. Modified Real-World Case
**New problem:** Modelling battery temperature vs charging current.  
**Assumptions:** Quadratic relationship.  
**Interpretation:** Predicts temperature at higher currents for safety design.