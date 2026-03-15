

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
