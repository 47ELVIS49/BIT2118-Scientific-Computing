# Task 9 – Eigenvalues and Eigenvectors

## B. Inputs and Mathematical Operation
**Inputs:** Adjacency matrix of a small undirected network.  
**Operations:** Compute eigenvalues and eigenvectors, extract the dominant ones, and normalize to get node importance scores.

## C. Parameter Change
Changed the matrix by adding an extra connection (set A[0,3] = A[3,0] = 1).  
Result: The importance ranking of the nodes changes.

## D. Meaning of the Output
The dominant eigenvector gives a measure of how structurally important each node is (similar to the idea behind PageRank). Higher score = more central node.

## E. Modified Real-World Case
**New problem:** Ranking importance of people in a small social network.  
**Assumptions:** Undirected friendships represented by the adjacency matrix.  
**Interpretation:** Identifies the most influential people based on connections.