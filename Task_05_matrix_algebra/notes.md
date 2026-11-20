# Task 5 – Matrix Algebra and Matrix Operations

## B. Inputs and Mathematical Operation
**Inputs:**  
- 4 points of a square  
- Rotation angle = 45°  
- Scaling factors (2.0 in x, 1.5 in y)  

**Operations:** Matrix multiplication to combine rotation and scaling, then apply the transformation to all points.

## C. Parameter Change
Changed the rotation angle from 45° to 90°.  
Result: The square is rotated differently and the final positions of the points change.

## D. Meaning of the Output
The output shows the original square corners, the combined transformation matrix, the new positions after rotation + scaling, and the determinant (which indicates whether the transformation preserves orientation).

## E. Modified Real-World Case
**New problem:** Transforming the corners of a robot arm end-effector.  
**Assumptions:** We only need rotation by 30° and uniform scaling by 1.2.  
**New inputs:** angle = 30°, scale = [[1.2, 0], [0, 1.2]]  
**Interpretation:** Gives the new coordinates of the end-effector after the movement.