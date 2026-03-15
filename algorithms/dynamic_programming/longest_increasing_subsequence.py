"""Longest Increasing Subsequence algorithm implementation"""


def longest_increasing_subsequence(arr: list[int]) -> int:
    """
    Find the length of the longest increasing subsequence using dynamic programming.

    Args:
        arr: List of integers

    Returns:
        Length of the longest increasing subsequence
    """
    n = len(arr)
    # Create DP array
    dp = [1] * n

    # Fill the DP array
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp) if dp else 0


def longest_increasing_subsequence_with_array(arr: list[int]) -> tuple[int, list[int]]:
    """
    Find the length and actual longest increasing subsequence.

    Args:
        arr: List of integers

    Returns:
        A tuple of (length_of_LIS, LIS_array)
    """
    n = len(arr)
    if n == 0:
        return 0, []

    # Create DP array and predecessor array
    dp = [1] * n
    predecessor = [-1] * n

    # Fill the DP array
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    predecessor[i] = j

    # Find the index of the maximum value
    max_idx = max(range(n), key=lambda x: dp[x])
    max_length = dp[max_idx]

    # Backtrack to find the LIS
    lis = []
    curr = max_idx
    while curr != -1:
        lis.append(arr[curr])
        curr = predecessor[curr]

    return max_length, lis[::-1]
