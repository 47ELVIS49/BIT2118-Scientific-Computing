# Task 19 – Numerical Optimization

## B. Inputs and Mathematical Operation
**Inputs:** Cost coefficients (12 and 18), capacity coefficients (100 and 170), minimum required capacity 1000.  
**Operations:** Minimize cost subject to capacity constraint using SLSQP, then search for best integer solution.

## C. Parameter Change
Changed the cost of Type B servers from 18 to 15.  
Result: The optimizer uses more Type B servers because they became cheaper.

## D. Meaning of the Output
The continuous solution gives the ideal (possibly fractional) number of each server type. The integer search finds the cheapest whole-number combination that still meets the capacity requirement.

## E. Modified Real-World Case
**New problem:** Minimizing the cost of two types of cloud virtual machines while meeting a minimum CPU requirement.  
**Assumptions:** Different costs and capacities.  
**Interpretation:** Helps choose the cheapest mix of VMs that satisfies the performance need.