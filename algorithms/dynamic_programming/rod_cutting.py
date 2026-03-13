"""
Rod Cutting Algorithm Implementation

This module implements the Rod Cutting algorithm using dynamic programming to find
the maximum revenue that can be obtained by cutting a rod of length n into pieces.
The Rod Cutting problem is a classic optimization problem with numerous applications
including resource allocation, manufacturing, and cutting stock problems. The algorithm
uses dynamic programming to efficiently solve this problem by breaking it down into
smaller subproblems.

Rod Cutting Problem Overview:
    The Rod Cutting problem is a fundamental optimization problem with numerous applications:
    - Manufacturing and cutting stock optimization
    - Resource allocation and distribution
    - Financial optimization
    - Telecommunications and bandwidth allocation
    - Manufacturing processes
    - Inventory management
    - Cryptography and code design
    - Combinatorial optimization

Problem Definition:
    Given:
    - A rod of length n (integer)
    - A price array where price[i] represents the price of a rod of length i+1
    Constraints:
    - You can cut the rod into any number of pieces
    - Each piece has a specific price based on its length
    - The goal is to maximize total revenue
    Objective:
    - Find the maximum revenue that can be obtained by cutting the rod

    Formally:
    - For length n, let revenue[n] be the maximum revenue
    - revenue[n] = max(price[i] + revenue[n-i]) for all i from 1 to n

Dynamic Programming Algorithm Steps:
    The algorithm uses a 1D DP array to store solutions to subproblems:

    1. Create a 1D array revenue of size n+1 where:
       - revenue[i] represents the maximum revenue for a rod of length i
    2. Initialize revenue[0] = 0 (0 length → 0 revenue)
    3. For i from 1 to n:
       - revenue[i] = max(price[j] + revenue[i-j]) for all j from 1 to i
    4. The answer is revenue[n] - the maximum revenue for length n

Input:
    n: An integer representing the length of the rod
    price: A list of integers representing the price of rods of each length

Output:
    Returns the maximum revenue achievable by cutting the rod

Example:
    >>> n = 8
    >>> price = [1, 5, 8, 9, 10, 17, 17, 20]
    >>> rod_cutting(n, price)
    22

    >>> n = 10
    >>> price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    >>> rod_cutting(n, price)
    29

    >>> n = 3
    >>> price = [3, 5, 6]
    >>> rod_cutting(n, price)
    6

    >>> n = 1
    >>> price = [100]
    >>> rod_cutting(n, price)
    100

    Step-by-step example for rod_cutting(8, [1, 5, 8, 9, 10, 17, 17, 20]):
    Create revenue array of size 9

    Initialize: revenue = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    Fill the revenue array:

    i=1:
    - j=1: price[0] + revenue[0] = 1 + 0 = 1
    - revenue[1] = 1

    i=2:
    - j=1: price[0] + revenue[1] = 1 + 1 = 2
    - j=2: price[1] + revenue[0] = 5 + 0 = 5
    - revenue[2] = max(2, 5) = 5

    i=3:
    - j=1: price[0] + revenue[2] = 1 + 5 = 6
    - j=2: price[1] + revenue[1] = 5 + 1 = 6
    - j=3: price[2] + revenue[0] = 8 + 0 = 8
    - revenue[3] = max(6, 6, 8) = 8

    i=4:
    - j=1: price[0] + revenue[3] = 1 + 8 = 9
    - j=2: price[1] + revenue[2] = 5 + 5 = 10
    - j=3: price[2] + revenue[1] = 8 + 1 = 9
    - j=4: price[3] + revenue[0] = 9 + 0 = 9
    - revenue[4] = max(9, 10, 9, 9) = 10

    i=5:
    - j=1: price[0] + revenue[4] = 1 + 10 = 11
    - j=2: price[1] + revenue[3] = 5 + 8 = 13
    - j=3: price[2] + revenue[2] = 8 + 5 = 13
    - j=4: price[3] + revenue[1] = 9 + 1 = 10
    - j=5: price[4] + revenue[0] = 10 + 0 = 10
    - revenue[5] = max(11, 13, 13, 10, 10) = 13

    i=6:
    - j=1: price[0] + revenue[5] = 1 + 13 = 14
    - j=2: price[1] + revenue[4] = 5 + 10 = 15
    - j=3: price[2] + revenue[3] = 8 + 8 = 16
    - j=4: price[3] + revenue[2] = 9 + 5 = 14
    - j=5: price[4] + revenue[1] = 10 + 1 = 11
    - j=6: price[5] + revenue[0] = 17 + 0 = 17
    - revenue[6] = max(14, 15, 16, 14, 11, 17) = 17

    i=7:
    - j=1: price[0] + revenue[6] = 1 + 17 = 18
    - j=2: price[1] + revenue[5] = 5 + 13 = 18
    - j=3: price[2] + revenue[4] = 8 + 10 = 18
    - j=4: price[3] + revenue[3] = 9 + 8 = 17
    - j=5: price[4] + revenue[2] = 10 + 5 = 15
    - j=6: price[5] + revenue[1] = 17 + 1 = 18
    - j=7: price[6] + revenue[0] = 17 + 0 = 17
    - revenue[7] = max(18, 18, 18, 17, 15, 18, 17) = 18

    i=8:
    - j=1: price[0] + revenue[7] = 1 + 18 = 19
    - j=2: price[1] + revenue[6] = 5 + 17 = 22
    - j=3: price[2] + revenue[5] = 8 + 13 = 21
    - j=4: price[3] + revenue[4] = 9 + 10 = 19
    - j=5: price[4] + revenue[3] = 10 + 8 = 18
    - j=6: price[5] + revenue[2] = 17 + 5 = 22
    - j=7: price[6] + revenue[1] = 17 + 1 = 18
    - j=8: price[7] + revenue[0] = 20 + 0 = 20
    - revenue[8] = max(19, 22, 21, 19, 18, 22, 18, 20) = 22

    Final result: revenue[8] = 22
    The optimal solution is to cut the rod into 2 pieces of length 2 and one piece of length 4:
    - Length 2: 5
    - Length 2: 5
    - Length 4: 12 (8 + 4? Let me recalculate)

    Actually, let me check: revenue[2] = 5 (two pieces of length 1)
    revenue[4] = 10 (two pieces of length 2)
    revenue[8] = 22 from j=2: 5 + revenue[6] = 5 + 17 = 22
    revenue[6] = 17 from j=6: 17 + revenue[0] = 17
    So the optimal is: 5 + 17 = 22
    revenue[6] = 17 could be from j=6: price[5] + 0 = 17 (one piece of length 6)
    Or from j=2: 5 + revenue[4] = 5 + 10 = 15
    Or from j=3: 8 + revenue[3] = 8 + 8 = 16
    Or from j=6: 17 + 0 = 17 (one piece of length 6)
    So revenue[6] = 17 means one piece of length 6: price[5] = 17

    So revenue[8] = 22 comes from j=2: price[1] + revenue[6] = 5 + 17 = 22
    This means: one piece of length 2 and one piece of length 6
    Or it could come from j=6: price[5] + revenue[2] = 17 + 5 = 22
    This means: one piece of length 6 and two pieces of length 1

    Either way, the optimal solution is: one piece of length 6 (17) and one piece of length 2 (5)
    Total: 17 + 5 = 22

Complexity Analysis:
    Time Complexity: O(n^2)
    - n: Length of the rod
    - For each length from 1 to n, we iterate through all possible cuts
    - Space Complexity: O(n)
    - The 1D DP array requires O(n) space
    - For tracking cuts: O(n) additional space

    Space Complexity:
    - 1D DP array: O(n)
    - For storing cut information: O(n) additional space
    - Total space complexity is O(n)

    Note:
    The Rod Cutting problem is a classic dynamic programming problem that demonstrates
    the principle of optimal substructure. The key insight is that the optimal solution
    for length n can be built from optimal solutions for smaller lengths. The algorithm
    is efficient for finding the optimal revenue, but the time complexity grows
    quadratically with the rod length. For very large rods, consider using the
    "Knuth optimization" which reduces the time complexity to O(n) under certain
    conditions. The Rod Cutting problem has numerous real-world applications in
    manufacturing, resource allocation, and inventory management. It's also related
    to the unbounded knapsack problem, which can be seen as a generalization of
    this problem.
"""

def rod_cutting(n: int, price: list[int]) -> int:
    """
    Find the maximum revenue from rod cutting using dynamic programming.

    Args:
        n: Length of the rod
        price: List where price[i] is the price of a rod of length i+1

    Returns:
        Maximum revenue achievable by cutting the rod
    """
    # Create revenue array
    revenue = [0] * (n + 1)

    # Fill the revenue array
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            max_val = max(max_val, price[j] + revenue[i - j - 1])
        revenue[i] = max_val

    return revenue[n]


def rod_cutting_with_cuts(n: int, price: list[int]) -> tuple[int, list[int]]:
    """
    Find the maximum revenue and the optimal cuts.

    Args:
        n: Length of the rod
        price: List where price[i] is the price of a rod of length i+1

    Returns:
        A tuple of (maximum_revenue, optimal_cuts)
    """
    # Create revenue and cut arrays
    revenue = [0] * (n + 1)
    cut = [-1] * (n + 1)

    # Fill the arrays
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            if price[j] + revenue[i - j - 1] > max_val:
                max_val = price[j] + revenue[i - j - 1]
                cut[i] = j + 1

        revenue[i] = max_val

    # Build the cut sequence
    cuts = []
    remaining = n
    while remaining > 0:
        cuts.append(cut[remaining])
        remaining -= cut[remaining]

    return revenue[n], cuts
