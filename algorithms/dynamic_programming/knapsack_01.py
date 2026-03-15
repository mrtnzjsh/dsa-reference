def knapsack_01(weights: list[int], values: list[int], W: int) -> int:
    n = len(weights)
    # Create DP table
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] > w:
                # Item can't fit in knapsack, skip it
                dp[i][w] = dp[i - 1][w]
            else:
                # Take max of not taking or taking the item
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )

    return dp[n][W]


def knapsack_01_with_items(weights: list[int], values: list[int], W: int) -> tuple[int, list[int]]:
    n = len(weights)
    # Create DP table
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )

    # Backtrack to find selected items
    selected_items = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    return dp[n][W], selected_items[::-1]
