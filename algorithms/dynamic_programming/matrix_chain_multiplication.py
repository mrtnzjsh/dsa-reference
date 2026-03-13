"""
Matrix Chain Multiplication Algorithm Implementation

This module implements the Matrix Chain Multiplication algorithm using dynamic programming
to find the minimum number of scalar multiplications needed to multiply a chain of matrices.
Matrix chain multiplication is an important problem in computer science with applications
in computational geometry, graphics, and optimization. The algorithm uses dynamic programming
to efficiently solve this problem by breaking it down into smaller subproblems.

Matrix Chain Multiplication Problem Overview:
    Matrix chain multiplication is a fundamental problem with numerous applications:
    - Computational geometry (computing product of transformation matrices)
    - Computer graphics (3D rendering and transformations)
    - Optimal parentheses placement for matrix multiplication
    - Sequence alignment in bioinformatics
    - Compiler optimization (register allocation)
    - Circuit design and optimization
    - Neural network optimization
    - Physics simulations

Problem Definition:
    Given:
    - A chain of n matrices with dimensions:
      Matrix 1: p0 × p1
      Matrix 2: p1 × p2
      Matrix 3: p2 × p3
      ...
      Matrix n: p(n-1) × pn
    Constraints:
    - Matrix multiplication is associative but not commutative
    - The order of multiplication affects the total number of scalar multiplications
    Objective:
    - Find the optimal parenthesization that minimizes the total cost (number of scalar multiplications)

Matrix Multiplication Cost:
    For matrices A (m × n) and B (n × p), the product AB is an m × p matrix.
    The number of scalar multiplications required is m × n × p.

Dynamic Programming Algorithm Steps:
    The algorithm uses a 2D DP table to store solutions to subproblems:

    1. Create a 2D array dp[n][n] where:
       - dp[i][j] represents the minimum cost to multiply matrices from i to j
    2. Initialize dp[i][i] = 0 for all i (single matrix requires no multiplication)
    3. Initialize dp[i][j] = infinity for i < j
    4. Fill the DP table for chains of increasing length:
       For length from 2 to n:
         For i from 0 to n - length:
           j = i + length - 1
           For k from i to j - 1:
             cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
             dp[i][j] = min(dp[i][j], cost)
    5. The answer is dp[0][n-1] - the minimum cost

Input:
    p: A list of integers representing the dimensions of the matrices
      where Matrix i has dimensions p[i-1] × p[i]

Output:
    Returns the minimum number of scalar multiplications needed

Example:
    >>> p = [40, 20, 30, 10, 30]
    >>> matrix_chain_multiplication(p)
    26000

    >>> p = [10, 30, 5, 60]
    >>> matrix_chain_multiplication(p)
    4500

    >>> p = [10, 20, 30]
    >>> matrix_chain_multiplication(p)
    6000

    >>> p = [10, 20, 30, 40, 50, 60]
    >>> matrix_chain_multiplication(p)
    18000

    Step-by-step example for matrix_chain_multiplication([40, 20, 30, 10, 30]):
    We have 4 matrices:
    - Matrix 1: 40 × 20
    - Matrix 2: 20 × 30
    - Matrix 3: 30 × 10
    - Matrix 4: 10 × 30

    Create dp table of size 5×5

    Initialize:
    dp[i][i] = 0 for all i
    dp[i][j] = infinity for i < j

    Fill the table for chains of increasing length:

    Length = 2:
    - dp[0][1]: matrices 1-2 (40×20 and 20×30)
      k=0: dp[0][0] + dp[1][1] + p[0] * p[1] * p[2] = 0 + 0 + 40*20*30 = 24000
      dp[0][1] = 24000
    - dp[1][2]: matrices 2-3 (20×30 and 30×10)
      k=1: dp[1][1] + dp[2][2] + p[1] * p[2] * p[3] = 0 + 0 + 20*30*10 = 6000
      dp[1][2] = 6000
    - dp[2][3]: matrices 3-4 (30×10 and 10×30)
      k=2: dp[2][2] + dp[3][3] + p[2] * p[3] * p[4] = 0 + 0 + 30*10*30 = 9000
      dp[2][3] = 9000

    Length = 3:
    - dp[0][2]: matrices 1-3 (40×20, 20×30, 30×10)
      k=0: dp[0][0] + dp[1][2] + p[0] * p[1] * p[3] = 0 + 6000 + 40*20*10 = 6000 + 8000 = 14000
      k=1: dp[0][1] + dp[2][2] + p[0] * p[2] * p[3] = 24000 + 0 + 40*30*10 = 24000 + 12000 = 36000
      dp[0][2] = min(14000, 36000) = 14000
    - dp[1][3]: matrices 2-4 (20×30, 30×10, 10×30)
      k=1: dp[1][1] + dp[2][3] + p[1] * p[2] * p[4] = 0 + 9000 + 20*30*30 = 9000 + 18000 = 27000
      k=2: dp[1][2] + dp[3][3] + p[1] * p[3] * p[4] = 6000 + 0 + 20*10*30 = 6000 + 6000 = 12000
      dp[1][3] = min(27000, 12000) = 12000

    Length = 4:
    - dp[0][3]: matrices 1-4 (40×20, 20×30, 30×10, 10×30)
      k=0: dp[0][0] + dp[1][3] + p[0] * p[1] * p[4] = 0 + 12000 + 40*20*30 = 12000 + 24000 = 36000
      k=1: dp[0][1] + dp[2][3] + p[0] * p[2] * p[4] = 24000 + 9000 + 40*30*30 = 24000 + 9000 + 36000 = 69000
      k=2: dp[0][2] + dp[3][3] + p[0] * p[3] * p[4] = 14000 + 0 + 40*10*30 = 14000 + 12000 = 26000
      dp[0][3] = min(36000, 69000, 26000) = 26000

    Final result: dp[0][3] = 26000
    The optimal parenthesization is ((A1 × (A2 × A3)) × A4) or ((A1 × A2) × (A3 × A4))
    Both give the same cost: (20×30×10) + (40×20×10) + (40×30×30) = 6000 + 8000 + 12000 = 26000

Complexity Analysis:
    Time Complexity: O(n^3)
    - n: Number of matrices
    - Three nested loops: O(n^2) for the outer two loops, O(n) for the inner loop
    - Space Complexity: O(n^2)
    - The 2D DP table requires O(n^2) space
    - Can be optimized to O(n) for just storing the optimal cost

    Space Complexity:
    - 2D DP table: O(n^2)
    - For storing parenthesization information: O(n^2) additional space
    - Total space complexity is O(n^2)

    Note:
    The Matrix Chain Multiplication problem is a classic dynamic programming problem
    that demonstrates the principle of optimal substructure. The key insight is that
    the optimal solution for a chain of length L can be built from optimal solutions
    for smaller chains. The algorithm is efficient for small to moderate chain lengths,
    but the time complexity grows cubically with the number of matrices. For very large
    chains, consider using the "Knuth optimization" which reduces the time complexity
    to O(n^2) under certain conditions. The Matrix Chain Multiplication problem has
    numerous real-world applications in computational geometry, computer graphics, and
    optimization. It's also related to the optimal binary search tree problem, which
    has applications in database systems and information retrieval.
"""

def matrix_chain_multiplication(p: list[int]) -> int:
    """
    Find the minimum cost of matrix chain multiplication using dynamic programming.

    Args:
        p: List of dimensions where Matrix i has dimensions p[i-1] × p[i]

    Returns:
        Minimum number of scalar multiplications needed
    """
    n = len(p) - 1

    # Create DP table
    dp = [[0] * n for _ in range(n)]

    # Fill the DP table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n-1]


def matrix_chain_multiplication_with_parenthesization(p: list[int]) -> tuple[int, list[list[int]]]:
    """
    Find the minimum cost and the optimal parenthesization.

    Args:
        p: List of dimensions where Matrix i has dimensions p[i-1] × p[i]

    Returns:
        A tuple of (minimum_cost, optimal_parenthesization)
    """
    n = len(p) - 1

    # Create DP table
    dp = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    # Fill the DP table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    s[i][j] = k

    # Build parenthesization string
    def build_parenthesis(i, j):
        if i == j:
            return f"A{i+1}"
        else:
            return f"({build_parenthesis(i, s[i][j])} × {build_parenthesis(s[i][j] + 1, j)})"

    return dp[0][n-1], build_parenthesis(0, n-1)
