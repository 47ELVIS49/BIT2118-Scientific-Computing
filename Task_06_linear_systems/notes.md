# Task 6 – Solution of Systems of Linear Equations

## B. Inputs and Operation
**Inputs:** Coefficient matrix A (CPU and memory usage) and vector b (total usage).  
**Operation:** Solve Ax = b using `np.linalg.solve`.

## C. Parameter Change
I changed total CPU from 20 to 24 (`b = np.array([24.0, 72.0])`).  
Number of Type A servers increased while Type B decreased to still meet the memory constraint.

## D. Meaning of Output
The solution tells how many of each server type are running. Residual near zero confirms the solution is correct.

## E. Modified Case
**New problem:** Two types of printers using different amounts of paper and ink.  
**New A and b:**  
```python
A = np.array([[3.0, 5.0], [2.0, 4.0]])
b = np.array([35.0, 28.0])