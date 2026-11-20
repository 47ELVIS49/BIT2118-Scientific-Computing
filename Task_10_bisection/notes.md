# Task 10 – Root Finding: Bisection and Fixed-Point Methods

## B. Inputs and Mathematical Operation
**Inputs:**  
- Function: f(T) = T - 25 - 10*exp(-T/20)  
- Bracket for bisection: [20, 40]  
- Initial guess for fixed-point: T = 30  

**Operations:**  
- Bisection method (halving the interval)  
- Fixed-point iteration: T = g(T) where g(T) = 25 + 10*exp(-T/20)

## C. Parameter Change
Changed the ambient temperature constant from 25 to 22 (i.e. f(T) = T - 22 - 10*exp(-T/20)).  
Result: Equilibrium temperature decreased because the surrounding temperature is lower.

## D. Meaning of the Output + Graph
Both methods find the temperature at which heat gain equals heat loss (thermal equilibrium).  
The graph shows the heat-balance function crossing zero at the root. The red dashed line marks the calculated equilibrium temperature.

## E. Modified Real-World Case
**New problem:** Finding the equilibrium temperature of a chemical reactor.  
**Assumptions:** Heat generation and loss follow a similar exponential form.  
**New function:** f(T) = T - 30 - 8*exp(-T/15)  
**Interpretation:** The root is the stable operating temperature of the reactor.