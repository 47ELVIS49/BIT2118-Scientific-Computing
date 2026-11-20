# Task 4 – Floating-Point Arithmetic and Numerical Errors

## B. Inputs and Operation
**Inputs:** 0.1 + 0.2, √2 approximation, and small values of x.  
**Operations:** Exact equality check, absolute/relative error, and comparison of unstable vs stable formula.

## C. Parameter Change
I changed `approx_value = 1.414` to `1.4142`.  
Absolute and relative errors became smaller because the approximation is closer to the true value.

## D. Meaning of Output
0.1 + 0.2 is not exactly 0.3 in floating-point. We must use tolerance (`np.isclose`). The stable formula avoids cancellation error for very small x.

## E. Modified Case
**New problem:** Banking system comparing 0.1 + 0.2 money values.  
**Change:** Use `np.isclose` instead of `==` when checking if two money amounts are equal.  
**Interpretation:** Prevents wrong decisions caused by floating-point rounding.