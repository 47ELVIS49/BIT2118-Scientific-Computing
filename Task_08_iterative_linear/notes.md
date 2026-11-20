# Task 8 – Iterative Methods for Linear Systems

## B. Inputs and Mathematical Operation
**Inputs:** 5×5 tridiagonal matrix A and boundary vector b.  
**Operations:** Jacobi and Gauss-Seidel iterative methods to solve the steady-state temperature system.

## C. Parameter Change
Changed the right boundary temperature from 20 to 50 (`b = [100, 0, 0, 0, 50]`).  
Result: All interior temperatures increased.

## D. Meaning of the Output + Graph
The methods iteratively improve the temperature estimates until the change is very small.  
The graph shows that Gauss-Seidel converges faster than Jacobi.

## E. Modified Real-World Case
**New problem:** Temperature distribution along a metal rod with different end temperatures.  
**Assumptions:** Same structure, different boundary values.  
**Interpretation:** Predicts the steady-state temperatures at interior points.