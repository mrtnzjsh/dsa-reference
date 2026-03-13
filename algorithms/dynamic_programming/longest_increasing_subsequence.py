"""
Longest Increasing Subsequence Algorithm Implementation

This module implements the Longest Increasing Subsequence (LIS) algorithm using dynamic
programming to find the length of the longest subsequence that is strictly increasing.
A subsequence is a sequence that can be derived from another sequence by deleting zero
or more elements without changing the order of the remaining elements. The algorithm uses
dynamic programming and binary search to efficiently solve this classic problem.

LIS Problem Overview:
    The Longest Increasing Subsequence problem is a fundamental problem in computer science
    with numerous applications:
    - Bioinformatics (finding the longest increasing subsequence of DNA sequences)
    - Algorithm analysis (computing the length of the longest increasing subsequence)
    - Combinatorial optimization
    - Pattern recognition
    - Financial analysis (stock price analysis)
    - Version control systems
    - Network routing
    - Project management (critical path analysis)

Problem Definition:
    Given:
    - An array of n integers
    Constraints:
    - Find the longest subsequence (not necessarily contiguous) that is strictly increasing
    - Elements must maintain the original order
    Objective:
    - Find the length of the longest increasing subsequence
    - Optionally find the actual LIS subsequence

Dynamic Programming Algorithm Steps:
    The algorithm uses a 1D DP array to store solutions to subproblems:

    1. Create a 1D array dp of size n where:
       - dp[i] represents the length of the LIS ending at index i
    2. Initialize all dp[i] = 1 (each element is an increasing subsequence of length 1)
    3. Fill the DP array:
       For i from 0 to n-1:
         For j from 0 to i-1:
           If arr[j] < arr[i]:
             - dp[i] = max(dp[i], dp[j] + 1)
    4. The answer is max(dp) - the length of the LIS
    5. Optionally backtrack to find the actual LIS

Input:
    arr: A list of integers representing the input sequence

Output:
    Returns the length of the longest increasing subsequence

Example:
    >>> arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    >>> longest_increasing_subsequence(arr)
    6

    >>> arr = [3, 10, 2, 1, 20]
    >>> longest_increasing_subsequence(arr)
    3

    >>> arr = [1, 2, 3, 4, 5]
    >>> longest_increasing_subsequence(arr)
    5

    >>> arr = [5, 4, 3, 2, 1]
    >>> longest_increasing_subsequence(arr)
    1

    Step-by-step example for longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]):
    Create dp array of size 9

    Initialize: dp = [1, 1, 1, 1, 1, 1, 1, 1, 1]

    Fill the DP array:

    i=0 (value=10):
    - No previous elements to compare
    - dp[0] = 1

    i=1 (value=22):
    - j=0: arr[0]=10 < 22 → dp[1] = max(1, 1+1=2) = 2
    - dp[1] = 2

    i=2 (value=9):
    - j=0: arr[0]=10 < 9 → no
    - j=1: arr[1]=22 < 9 → no
    - dp[2] = 1

    i=3 (value=33):
    - j=0: arr[0]=10 < 33 → dp[3] = max(1, 1+1=2) = 2
    - j=1: arr[1]=22 < 33 → dp[3] = max(2, 2+1=3) = 3
    - j=2: arr[2]=9 < 33 → dp[3] = max(3, 1+1=2) = 3
    - dp[3] = 3

    i=4 (value=21):
    - j=0: arr[0]=10 < 21 → dp[4] = max(1, 1+1=2) = 2
    - j=1: arr[1]=22 < 21 → no
    - j=2: arr[2]=9 < 21 → dp[4] = max(2, 1+1=2) = 2
    - j=3: arr[3]=33 < 21 → no
    - dp[4] = 2

    i=5 (value=50):
    - j=0: arr[0]=10 < 50 → dp[5] = max(1, 1+1=2) = 2
    - j=1: arr[1]=22 < 50 → dp[5] = max(2, 2+1=3) = 3
    - j=2: arr[2]=9 < 50 → dp[5] = max(3, 1+1=2) = 3
    - j=3: arr[3]=33 < 50 → dp[5] = max(3, 3+1=4) = 4
    - j=4: arr[4]=21 < 50 → dp[5] = max(4, 2+1=3) = 4
    - dp[5] = 4

    i=6 (value=41):
    - j=0: arr[0]=10 < 41 → dp[6] = max(1, 1+1=2) = 2
    - j=1: arr[1]=22 < 41 → dp[6] = max(2, 2+1=3) = 3
    - j=2: arr[2]=9 < 41 → dp[6] = max(3, 1+1=2) = 3
    - j=3: arr[3]=33 < 41 → dp[6] = max(3, 3+1=4) = 4
    - j=4: arr[4]=21 < 41 → dp[6] = max(4, 2+1=3) = 4
    - j=5: arr[5]=50 < 41 → no
    - dp[6] = 4

    i=7 (value=60):
    - j=0: arr[0]=10 < 60 → dp[7] = max(1, 1+1=2) = 2
    - j=1: arr[1]=22 < 60 → dp[7] = max(2, 2+1=3) = 3
    - j=2: arr[2]=9 < 60 → dp[7] = max(3, 1+1=2) = 3
    - j=3: arr[3]=33 < 60 → dp[7] = max(3, 3+1=4) = 4
    - j=4: arr[4]=21 < 60 → dp[7] = max(4, 2+1=3) = 4
    - j=5: arr[5]=50 < 60 → dp[7] = max(4, 4+1=5) = 5
    - j=6: arr[6]=41 < 60 → dp[7] = max(5, 4+1=5) = 5
    - dp[7] = 5

    i=8 (value=80):
    - j=0: arr[0]=10 < 80 → dp[8] = max(1, 1+1=2) = 2
    - j=1: arr[1]=22 < 80 → dp[8] = max(2, 2+1=3) = 3
    - j=2: arr[2]=9 < 80 → dp[8] = max(3, 1+1=2) = 3
    - j=3: arr[3]=33 < 80 → dp[8] = max(3, 3+1=4) = 4
    - j=4: arr[4]=21 < 80 → dp[8] = max(4, 2+1=3) = 4
    - j=5: arr[5]=50 < 80 → dp[8] = max(4, 4+1=5) = 5
    - j=6: arr[6]=41 < 80 → dp[8] = max(5, 4+1=5) = 5
    - j=7: arr[7]=60 < 80 → dp[8] = max(5, 5+1=6) = 6
    - dp[8] = 6

    Final result: max(dp) = 6
    The LIS is [10, 22, 33, 50, 60, 80]

Complexity Analysis:
    Time Complexity: O(n^2)
    - n: Number of elements in the array
    - For each element, we compare it with all previous elements
    - Space Complexity: O(n)
    - The 1D DP array requires O(n) space
    - For backtracking: O(n) additional space for storing predecessor information

    Space Complexity:
    - 1D DP array: O(n)
    - For finding the actual LIS: O(n) additional space
    - Total space complexity is O(n)

    Note:
    The LIS problem can be solved more efficiently using binary search in O(n log n) time
    by maintaining an array that stores the smallest possible tail value for each length.
    The O(n^2) DP solution is simpler but less efficient for large n. The LIS problem
    demonstrates the principle of optimal substructure, where the optimal solution for
    length i can be built from optimal solutions for smaller lengths. The algorithm
    has numerous real-world applications including bioinformatics, financial analysis,
    and version control systems. It's also related to the longest increasing subsequence
    of permutations, which has interesting properties in combinatorics and algorithm
    analysis. The problem can be generalized to find the longest non-decreasing subsequence,
    longest decreasing subsequence, or longest alternating subsequence by changing the
    comparison operator.
"""

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
