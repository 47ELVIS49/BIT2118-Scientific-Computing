# Task 3 – Mathematical Functions and Vectorization

## B. Inputs and Operation
**Inputs:** 1 million random latency values in milliseconds.  
**Operation:** Convert to seconds and square each value (vectorized vs Python loop).

## C. Parameter Change
I changed the number of values from 1_000_000 to 100_000.  
Both times became smaller, but the speed-up ratio stayed similar. Vectorization is still much faster.

## D. Meaning of Output
The vectorized version is many times faster than a normal Python loop. This shows why NumPy is used for large scientific data.

## E. Modified Case
**New problem:** Convert 500,000 sensor voltage readings from millivolts to volts and square them for power calculation.  
**Change:** `latency_ms = rng.uniform(5, 250, 500_000)`  
**Interpretation:** Same speed advantage applies to sensor data processing.