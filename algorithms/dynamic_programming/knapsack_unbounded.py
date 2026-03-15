def knapsack_unbounded(weights: list[int], values: list[int], W: int) -> int:
    """Solve the Unbounded Knapsack problem using dynamic programming.

    Args:
        weights: List of item weights
        values: List of item values
        W: Maximum knapsack capacity

    Returns:
        Maximum value achievable with the given capacity
    """
    # Create DP array
    dp = [0] * (W + 1)

    # Fill the DP array
    for w in range(1, W + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[W]


def knapsack_unbounded_with_items(weights: list[int], values: list[int], W: int) -> tuple[int, list[int]]:
    """Solve the Unbounded Knapsack problem and return the selected items.

    Args:
        weights: List of item weights
        values: List of item values
        W: Maximum knapsack capacity

    Returns:
        A tuple of (maximum_value, list_of_item_counts)
    """
    # Create DP array
    dp = [0] * (W + 1)

    # Fill the DP array
    for w in range(1, W + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    # Backtrack to find item counts
    item_counts = [0] * len(weights)
    w = W
    while w > 0:
        for i in range(len(weights)):
            if weights[i] <= w:
                if dp[w] == values[i] + dp[w - weights[i]]:
                    item_counts[i] += 1
                    w -= weights[i]
                    break

    return dp[W], item_counts
