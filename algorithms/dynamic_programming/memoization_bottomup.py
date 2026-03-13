"""
Memoization (Top-Down) & Bottom-Up Dynamic Programming Algorithm Implementation

This module provides implementations of memoization (top-down dynamic programming)
and bottom-up dynamic programming approaches for solving optimization problems.
Memoization is a technique where we store the results of expensive function calls
and return the cached result when the same inputs occur again. Bottom-up dynamic
programming involves solving all subproblems starting from the smallest to the
largest, filling a table progressively.

Memoization Algorithm Overview:
    Memoization (Top-Down):
    - Starts with the original problem and breaks it down into smaller subproblems
    - Uses recursion with caching of results to avoid redundant calculations
    - Each function call is checked against a cache before computation
    - The cache is typically implemented as a dictionary or array

    Bottom-Up (Iterative):
    - Starts with the base cases and builds up solutions to larger problems
    - Fills a DP table progressively from smaller to larger inputs
    - Does not use recursion, making it more memory efficient
    - The cache is explicitly implemented as a table

Both Approaches:
    Time Complexity: O(n) or O(n^2) or O(n^3) depending on the problem
    Space Complexity: O(n) or O(n^2) or O(n^3) for the cache/table
    Common Characteristics:
    - Avoid redundant calculations
    - Build solutions incrementally
    - Break problems into smaller subproblems
    - Exhibit optimal substructure

Memoization Implementation Steps:
    1. Define a recursive function that solves the problem
    2. Create a cache (dictionary or array) to store computed results
    3. In the recursive function, first check if the result is in cache
    4. If in cache, return the cached value
    5. If not in cache, compute the result recursively and store it in cache
    6. Return the computed result

Bottom-Up Implementation Steps:
    1. Create a table (array or 2D array) for storing intermediate results
    2. Initialize the base cases (usually when input is 0 or 1)
    3. Fill the table for increasing input sizes (iterative approach)
    4. The solution is in the table at the target index
    5. Backtrack if needed to reconstruct the actual solution

Example: Fibonacci Number Calculation
    Input: n = 10

    Memoization (Top-Down):
    - fib(10) → fib(9) + fib(8)
    - fib(9) → fib(8) + fib(7)
    - ... (redundant calculations)
    - Cache stores all computed values
    - Total time: O(n) with space: O(n)

    Bottom-Up (Iterative):
    - fib(0) = 0, fib(1) = 1
    - fib(2) = fib(1) + fib(0) = 1
    - fib(3) = fib(2) + fib(1) = 2
    - ...
    - fib(10) = fib(9) + fib(8)
    - Total time: O(n) with space: O(n)

    Both approaches have the same time complexity but different space usage
    and implementation styles.

Input:
    problem_type: String specifying the problem ("fibonacci", "n_queens", "knapsack", etc.)
    parameters: Dictionary containing the input parameters for the problem

Output:
    Returns the solution using the specified approach (memoization or bottom-up)

Example:
    >>> memoization_fibonacci(10)
    55

    >>> bottom_up_fibonacci(10)
    55

    >>> memoization_knapsack([2, 3, 4], [3, 4, 5], 5)
    7

    >>> bottom_up_knapsack([2, 3, 4], [3, 4, 5], 5)
    7

    Step-by-step example for memoization_fibonacci(10):
    1. Call memoization_fibonacci(10)
    2. Check cache[10] → not in cache
    3. Compute: memoization_fibonacci(10) = memoization_fibonacci(9) + memoization_fibonacci(8)
    4. Check cache[9] → not in cache
    5. Compute: memoization_fibonacci(9) = memoization_fibonacci(8) + memoization_fibonacci(7)
    6. Check cache[8] → not in cache
    7. Compute: memoization_fibonacci(8) = memoization_fibonacci(7) + memoization_fibonacci(6)
    8. Continue recursively...
    9. Eventually reach base cases: memoization_fibonacci(0) = 0, memoization_fibonacci(1) = 1
    10. Cache now contains: {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}
    11. Return 55

    Step-by-step example for bottom_up_fibonacci(10):
    1. Create array dp of size 11
    2. Initialize base cases: dp[0] = 0, dp[1] = 1
    3. Fill the array iteratively:
       - dp[2] = dp[1] + dp[0] = 1 + 0 = 1
       - dp[3] = dp[2] + dp[1] = 1 + 1 = 2
       - dp[4] = dp[3] + dp[2] = 2 + 1 = 3
       - dp[5] = dp[4] + dp[3] = 3 + 2 = 5
       - dp[6] = dp[5] + dp[4] = 5 + 3 = 8
       - dp[7] = dp[6] + dp[5] = 8 + 5 = 13
       - dp[8] = dp[7] + dp[6] = 13 + 8 = 21
       - dp[9] = dp[8] + dp[7] = 21 + 13 = 34
       - dp[10] = dp[9] + dp[8] = 34 + 21 = 55
    4. Return dp[10] = 55

Complexity Analysis:
    Time Complexity: O(n) or O(n^2) or O(n^3) depending on the problem
    - For linear problems: O(n) time for both approaches
    - For quadratic problems: O(n^2) time for both approaches
    - For cubic problems: O(n^3) time for both approaches

    Space Complexity:
    - Memoization: O(n) for the recursion stack + O(n) for the cache
    - Bottom-Up: O(n) for the DP array
    - Both approaches have similar space complexity for the cache/table

    Note:
    Both memoization and bottom-up dynamic programming are powerful techniques for
    solving optimization problems. Memoization is often more intuitive for recursive
    solutions and is closer to the mathematical definition of dynamic programming.
    However, it uses implicit recursion and may cause stack overflow for very large
    inputs. Bottom-up is more efficient in terms of space (no recursion stack) and
    is generally preferred for problems with large inputs. The choice between the
    two approaches depends on the specific problem, input size, and implementation
    preferences. Both techniques avoid the exponential time complexity of the naive
    recursive approach, reducing it to polynomial time by exploiting the overlapping
    subproblems property of the problem.
"""

from functools import lru_cache


def memoization_fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using memoization (top-down DP).

    Args:
        n: The Fibonacci number to calculate

    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n

    return memoization_fibonacci(n - 1) + memoization_fibonacci(n - 2)


@lru_cache(maxsize=None)
def memoization_fibonacci_with_cache(n: int) -> int:
    """
    Calculate the nth Fibonacci number using memoization with LRU cache.

    Args:
        n: The Fibonacci number to calculate

    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n

    return memoization_fibonacci_with_cache(n - 1) + memoization_fibonacci_with_cache(n - 2)


def bottom_up_fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using bottom-up DP.

    Args:
        n: The Fibonacci number to calculate

    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n

    # Create DP array
    dp = [0] * (n + 1)
    dp[1] = 1

    # Fill the DP array
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def memoization_knapsack_01(weights: list[int], values: list[int], W: int) -> int:
    """
    Solve the 0/1 Knapsack problem using memoization.

    Args:
        weights: List of item weights
        values: List of item values
        W: Maximum knapsack capacity

    Returns:
        Maximum value achievable with the given capacity
    """
    n = len(weights)

    @lru_cache(maxsize=None)
    def dfs(i, remaining):
        # Base case: no more items or no capacity left
        if i == n or remaining == 0:
            return 0

        # Skip the current item
        skip = dfs(i + 1, remaining)

        # Take the current item if it fits
        take = 0
        if weights[i] <= remaining:
            take = values[i] + dfs(i + 1, remaining - weights[i])

        return max(skip, take)

    return dfs(0, W)


def bottom_up_knapsack_01(weights: list[int], values: list[int], W: int) -> int:
    """
    Solve the 0/1 Knapsack problem using bottom-up DP.

    Args:
        weights: List of item weights
        values: List of item values
        W: Maximum knapsack capacity

    Returns:
        Maximum value achievable with the given capacity
    """
    n = len(weights)

    # Create DP table
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    return dp[n][W]


def memoization_coin_change(coins: list[int], amount: int) -> int:
    """
    Solve the Coin Change problem using memoization.

    Args:
        coins: List of available coin denominations
        amount: Target amount to make change for

    Returns:
        Minimum number of coins needed to make the exact amount
        If it's not possible, returns -1
    """
    @lru_cache(maxsize=None)
    def dfs(remaining):
        if remaining == 0:
            return 0

        if remaining < 0:
            return float('inf')

        min_coins = float('inf')
        for coin in coins:
            result = dfs(remaining - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)

        return min_coins

    result = dfs(amount)
    return result if result != float('inf') else -1


def bottom_up_coin_change(coins: list[int], amount: int) -> int:
    """
    Solve the Coin Change problem using bottom-up DP.

    Args:
        coins: List of available coin denominations
        amount: Target amount to make change for

    Returns:
        Minimum number of coins needed to make the exact amount
        If it's not possible, returns -1
    """
    # Create DP array
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    # Fill the DP array
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1
