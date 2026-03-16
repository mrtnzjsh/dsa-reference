# Matrix Chain Multiplication

## Overview

Matrix Chain Multiplication is a classic dynamic programming problem that finds the minimum number of scalar multiplications needed to multiply a chain of matrices. This algorithm is fundamental in computational geometry, computer graphics, optimization, and various other fields.

### Problem Definition

Given:
- A chain of n matrices with dimensions:
  - Matrix 1: p0 × p1
  - Matrix 2: p1 × p2
  - Matrix 3: p2 × p3
  - ...
  - Matrix n: p(n-1) × pn

Constraints:
- Matrix multiplication is associative but not commutative
- The order of multiplication affects the total number of scalar multiplications

Objective:
- Find the optimal parenthesization that minimizes the total cost (number of scalar multiplications)

### Matrix Multiplication Cost

For matrices A (m × n) and B (n × p), the product AB is an m × p matrix. The number of scalar multiplications required is:
`cost = m × n × p`

## Algorithm Steps

The algorithm uses a 2D DP table to store solutions to subproblems:

1. **Create DP table**: Create a 2D array dp\[n\][n]` where dp\[i\][j]` represents the minimum cost to multiply matrices from i to j

2. **Initialize single Initialize dp\[i\][i] = 0` for all i (single matrix requires no multiplication)

3. **Set bounds**: Initialize dp\[i\][j] = infinity` for all i < j

4. **Fill DP table**: Fill the DP table for chains of increasing length:
   - For length from 2 to n:
     - For i from 0 to n - length:
       - j = i + length - 1
       - For k from i to j - 1:
         - cost = dp\[i\][k] + dp\[k+1\][j] + p\[i\] * p[k+1] * p[j+1]
         - dp\[i\][j] = min(dp\[i\][j], cost)

5. **Return result**: The answer is dp\[0\][n-1]` - the minimum cost

## Input

- `p`: A list of integers representing the dimensions of the matrices
  - Where Matrix i has dimensions `p[i-1] × p\[i\]

## Output

- Returns the minimum number of scalar multiplications needed

## Example

**Example 1:**
```python
>>> p = [40, 20, 30, 10, 30]
>>> matrix_chain_multiplication(p)
26000
```

**Step-by-step breakdown for p = [40, 20, 30, 10, 30]:**

We have 4 matrices:
- Matrix 1: 40 × 20
- Matrix 2: 20 × 30
- Matrix 3: 30 × 10
- Matrix 4: 10 × 30

Create dp table of size 5×5

**Initialize:**
- dp\[i\][i] = 0 for all i
- dp\[i\][j] = infinity for i < j

**Fill the table for chains of increasing length:**

**Length = 2:**
- dp\[0\][1]: matrices 1-2 (40×20 and 20×30)
  - k=0: dp\[0\][0] + dp\[1\][1] + p\[0\] × p\[1\] × p\[2\] = 0 + 0 + 40×20×30 = 24000
  - dp\[0\][1] = 24000

- dp\[1\][2]: matrices 2-3 (20×30 and 30×10)
  - k=1: dp\[1\][1] + dp\[2\][2] + p\[1\] × p\[2\] × p\[3\] = 0 + 0 + 20×30×10 = 6000
  - dp\[1\][2] = 6000

- dp\[2\][3]: matrices 3-4 (30×10 and 10×30)
  - k=2: dp\[2\][2] + dp\[3\][3] + p\[2\] × p\[3\] × p\[4\] = 0 + 0 + 30×10×30 = 9000
  - dp\[2\][3] = 9000

**Length = 3:**
- dp\[0\][2]: matrices 1-3 (40×20, 20×30, 30×10)
  - k=0: dp\[0\][0] + dp\[1\][2] + p\[0\] × p\[1\] × p\[3\] = 0 + 6000 + 40×20×10 = 1400 + 8000 = 14000
  - k=1: dp\[0\][1] + dp\[2\][2] + p\[0\] × p\[2\] × p\[3\] = 24000 + 0 + 40×30×10 = 24000 + 12000 = 36000
  - dp\[0\][2] = min(14000, 36000) = 14000

- dp\[1\][3]: matrices 2-4 (20×30, 30×10, 10×30)
  - k=1: dp\[1\][1] + dp\[2\][3] + p\[1\] × p\[2\] × p\[4\] = 0 + 9000 + 20×30×30 = 9000 + 18000 = 27000
  - k=2: dp\[1\][2] + dp\[3\][3] + p\[1\] × p\[3\] × p\[4\] = 6000 + 0 + 20×10×30 = 6000 + 6000 = 12000
  - dp\[1\][3] = min(27000, 12000) = 12000

**Length = 4:**
- dp\[0\][3]: matrices 1-4 (40×20, 20×30, 30×10, 10×30)
  - k=0: dp\[0\][0] + dp\[1\][3] + p\[0\] × p\[1\] × p\[4\] = 0 + 12000 + 40×20×30 = 12000 + 24000 = 36000
  - k=1: dp\[0\][1] + dp\[2\][3] + p\[0\] × p\[2\] × p\[4\] = 24000 + 9000 + 40×30×30 = 24000 + 9000 + 36000 = 69000
  - k=2: dp\[0\][2] + dp\[3\][3] + p\[0\] × p\[3\] × p\[4\] = 14000 + 0 + 40×10×30 = 14000 + 12000 = 26000
  - dp\[0\][3] = min(36000, 69000, 26000) = 26000

**Final result:** dp\[0\][3] = 26000

The optimal parenthesization is ((A1 × (A2 × A3)) × A4) or ((A1 × A2) × (A3 × A4))

**Example 2:**
```python
>>> p = [10, 30, 5, 60]
>>> matrix_chain_multiplication(p)
4500
```

**Example 3:**
```python
>>> p = [10, 20, 30]
>>> matrix_chain_multiplication(p)
6000
```

**Example 4:**
```python
>>> p = [10, 20, 30, 40, 50, 60]
>>> matrix_chain_multiplication(p)
18000
```

## Complexity Analysis

### Time Complexity: O(n³)

- n: Number of matrices
- Three nested loops: O(n²) for the outer two loops, O(n) for the inner loop

### Space Complexity: O(n²)

- The 2D DP table requires O(n²) space
- Can be optimized to O(n) for just storing the optimal cost

### Optimization

- For very large chains, consider using "Knuth optimization" which reduces time complexity to O(n²) under certain conditions
- The Matrix Chain Multiplication problem is related to the optimal binary search tree problem

## Notes

The Matrix Chain Multiplication problem is a classic dynamic programming problem that demonstrates the principle of optimal substructure. The key insight is that the optimal solution for a chain of length L can be built from optimal solutions for smaller chains.

Applications:
- Computational geometry
- Computer graphics
- Optimal parentheses placement for matrix multiplication
- Sequence alignment in bioinformatics
- Compiler optimization
- Circuit design and optimization
- Neural network optimization
- Physics simulations
