# Task 17 – Ordinary Differential Equations – Euler Method

## B. Inputs and Operation
**Inputs:** Ambient temperature, initial temperature, cooling constant k, step size h.  
**Operation:** Euler method to solve Newton’s law of cooling.

## C. Parameter Change
I changed step size h from 1.0 to 0.5.  
The final temperature became closer to the exact solution (smaller error).

## D. Meaning of Output
Predicted temperature of the hot object after 30 minutes. Smaller step size improves accuracy but needs more calculations.

## E. Modified Case
**New problem:** Cooling of a cup of coffee in a colder room (ambient = 18°C).  
**Change:** `T_ambient = 18.0`  
**Interpretation:** Coffee reaches a lower final temperature faster.