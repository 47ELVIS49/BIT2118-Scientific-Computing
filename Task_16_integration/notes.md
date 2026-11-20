# Task 16 – Numerical Integration

## B. Inputs and Operation
**Inputs:** Time (hours) and power readings (kW).  
**Operation:** Approximate the integral of power over time using trapezoidal and Simpson’s rules to get energy in kWh.

## C. Parameter Change
I changed the last power reading from 0.9 to 1.5.  
Total energy increased because more power was consumed at the end of the period.

## D. Meaning of Output
The total electrical energy consumed during the 12 hours. Simpson’s rule is usually more accurate for smooth curves.

## E. Modified Case
**New problem:** Estimate total water volume from flow-rate sensor readings over 12 hours.  
**Change:** Replace power_kw with flow rates in m³/h.  
**Interpretation:** The integral gives total cubic metres of water used.