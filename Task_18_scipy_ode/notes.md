# Task 18 – Numerical Solution of ODEs Using SciPy

## B. Inputs and Mathematical Operation
**Inputs:** Supply voltage Vs, resistance R, capacitance C, initial voltage V0.  
**Operation:** Solve the first-order ODE dV/dt = (Vs - V)/(R*C) using `scipy.integrate.solve_ivp`.

## C. Parameter Change
Changed capacitance C from 0.001 to 0.002.  
Result: The capacitor charges more slowly (the curve rises more gradually).

## D. Meaning of the Output + Graph
The graph shows how the capacitor voltage rises toward the supply voltage over time. The numerical solution matches the exact solution very closely.

## E. Modified Real-World Case
**New problem:** Modelling the discharge of a capacitor in an RC circuit.  
**Assumptions:** Same R and C, but initial voltage = 5 V and supply = 0 V.  
**Interpretation:** Shows how quickly the voltage drops to zero – useful for timing circuits.