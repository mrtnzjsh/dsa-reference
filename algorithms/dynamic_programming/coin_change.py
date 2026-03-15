def coin_change(coins: list[int], amount: int) -> int:
    """Solve the Coin Change problem using dynamic programming.

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
                dp[i] = min(dp[i], 1 + dp[i - coin])

    # Return result
    return dp[amount] if dp[amount] != amount + 1 else -1


def coin_change_with_coins(coins: list[int], amount: int) -> tuple[int, list[int]]:
    """Solve the Coin Change problem and return the specific coins used.

    Args:
        coins: List of available coin denominations
        amount: Target amount to make change for

    Returns:
        A tuple of (minimum_number_of_coins, list_of_coins_used)
        If it's not possible, returns (-1, [])
    """
    # Create DP array
    dp = [amount + 1] * (amount + 1)
    prev_index = [-1] * (amount + 1)
    dp[0] = 0

    # Fill the DP array
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    prev_index[i] = coin

    # Check if change is possible
    if dp[amount] == amount + 1:
        return -1, []

    # Backtrack to find the coins used
    result_coins = []
    remaining = amount
    while remaining > 0:
        coin = prev_index[remaining]
        result_coins.append(coin)
        remaining -= coin

    return dp[amount], result_coins
