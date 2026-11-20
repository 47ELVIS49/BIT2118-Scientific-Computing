# Task 7 – Gaussian Elimination and LU Decomposition

## B. Inputs and Mathematical Operation
**Inputs:** Coefficient matrix A and three different measurement vectors b.  
**Operations:** LU factorization of A once, then solve A x = b for each measurement vector using the factors.

## C. Parameter Change
Changed the first measurement vector from [15, 10, 10] to [20, 12, 8].  
Result: The solution vector x changes because the right-hand side is different.

## D. Meaning of the Output
LU decomposition allows us to reuse the expensive factorization when we have many different b vectors. The residual norm near zero confirms accuracy.

## E. Modified Real-World Case
**New problem:** A structural engineering model that reuses the same stiffness matrix for different load cases.  
**Assumptions:** Same A matrix, different load vectors.  
**Interpretation:** Fast repeated solutions of the linear system for different loading conditions.