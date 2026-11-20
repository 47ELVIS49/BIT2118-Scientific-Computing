# Task 20 – Random Numbers and Monte Carlo Methods

## B. Inputs and Operation
**Inputs:** Capacity, mean demand, standard deviation, number of simulations N.  
**Operation:** Generate random demand scenarios and estimate the probability that demand exceeds capacity.

## C. Parameter Change
I increased mean_demand from 850 to 920.  
Overload probability increased significantly because the average demand is now closer to capacity.

## D. Meaning of Output
The estimated chance that the server will be overloaded under uncertain demand. More simulations give a more reliable estimate.

## E. Modified Case
**New problem:** Probability that a power station exceeds its generation capacity under uncertain electricity demand.  
**Change:** capacity = 5000, mean_demand = 4200, std_demand = 600.  
**Interpretation:** Helps decide whether more generation capacity is needed.