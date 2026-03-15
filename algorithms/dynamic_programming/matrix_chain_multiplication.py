
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
