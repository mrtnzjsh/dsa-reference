
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
