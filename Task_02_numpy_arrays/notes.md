# Task 2 – NumPy Arrays and Numerical Computation

## B. Inputs and Mathematical Operation
**Inputs:** Array of 24 hourly temperatures in Celsius.  
**Operations:** Mean, minimum, maximum, and vectorized conversion to Fahrenheit using the formula F = 1.8*C + 32.

## C. Parameter Change
I changed the first temperature from 18.5 to 15.0.  
New results: Mean becomes lower, minimum becomes 15.0.  
The mean decreased because one of the values was reduced.

## D. Meaning of the Output
The output shows the daily average temperature, the coldest and hottest readings of the day, and the first few temperatures converted to Fahrenheit. This helps a weather station quickly summarize the day.

## E. Modified Real-World Case
**New problem:** A hospital monitors body temperatures of 10 patients.  
**Assumptions:** Temperatures are in Celsius. We need mean, min, max and conversion to Fahrenheit.  
**New inputs:**  
`temperatures_c = np.array([36.5, 37.1, 38.2, 36.8, 37.0, 39.1, 36.9, 37.4, 38.0, 36.7])`  

**Interpretation:** The mean shows the average patient temperature. Max shows if any patient has high fever.