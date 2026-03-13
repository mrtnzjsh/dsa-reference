"""
Palindrome Partitioning Algorithm Implementation

This module implements the palindrome partitioning algorithm using backtracking to find all
possible partitions of a string such that every substring in the partition is a palindrome.
A palindrome partitioning of a string is a way to split the string into several substrings
where each substring reads the same forwards and backwards. The algorithm uses backtracking
to systematically explore all possible valid partitions of the input string.

Palindrome Partitioning Algorithm Overview:
    Palindrome partitioning has numerous applications including:
    - String analysis and pattern recognition
    - Cryptography (generating palindrome sequences)
    - Puzzle solving (palindrome puzzle reconstruction)
    - Text processing (finding all palindromic substrings)
    - Dynamic programming (optimizing partitioning decisions)
    - Computational linguistics (language structure analysis)
    - Genetic sequence analysis (DNA palindrome recognition)
    - Data compression (finding palindromic patterns)

Backtracking Algorithm Steps:
    The algorithm uses backtracking to systematically find all valid palindrome partitions:

    1. Initialize an empty list to store results and an empty list to track the current partition
    2. Start the recursive process with the given string and starting index 0
    3. In the recursive function:
       a. If the starting index equals the length of the string:
          - The current partition is complete
          - Add a copy of the current partition to the results
          - Return (base case: valid partition found)
       b. For each index from the starting point to the end of the string:
          - Extract the substring from start_idx to i
          - Check if the substring is a palindrome
          - If the substring is a palindrome:
             - Add the substring to the current partition
             - Recursively call the function with the next starting index (i + 1)
             - Remove (backtrack) the last substring from the current partition
             - This allows exploring other possible partitions without the current substring

    4. The wrapper function:
       a. Initialize an empty results list
       b. Call the recursive function with the string and starting index 0
       c. Return the results list containing all valid palindrome partitions

Input:
    s: A string for which palindrome partitions will be generated

Output:
    Returns a list of all possible palindrome partitions, where each partition is
    represented as a list of strings. The partitions are returned in lexicographic
    order based on the input string. The empty string returns an empty list.

Example:
    >>> s = "aab"
    >>> partition_palindrome(s)
    [["a", "a", "b"], ["aa", "b"]]

    >>> s = "google"
    >>> partition_palindrome(s)
    [["g", "o", "o", "g", "l", "e"], ["g", "o", "o", "gle"], ["g", "oo", "g", "l", "e"], ["g", "oo", "gle"]]

    >>> s = "a"
    >>> partition_palindrome(s)
    [["a"]]

    >>> s = "aabb"
    >>> partition_palindrome(s)
    [["a", "a", "b", "b"], ["a", "a", "bb"], ["a", "abb"], ["aa", "b", "b"], ["aa", "bb"], ["aabb"]]

    Step-by-step example for partition_palindrome("aab"):
    1. Call partition_palindrome_recursive("aab", 0, [], results)
    2. start_idx = 0, s = "aab", partition = [], results = []
    3. Loop i from 0 to 2
    4. First iteration: i = 0
       - substring = "a" from index 0 to 0
       - Check if "a" is a palindrome → yes (single character)
       - partition.append("a") → partition = ["a"]
       - Call partition_palindrome_recursive("aab", 1, ["a"], results)
          - start_idx = 1, s = "aab", partition = ["a"], results = []
          - Loop i from 1 to 2
          - First iteration: i = 1
             - substring = "a" from index 1 to 1
             - Check if "a" is a palindrome → yes
             - partition.append("a") → partition = ["a", "a"]
             - Call partition_palindrome_recursive("aab", 2, ["a", "a"], results)
                - start_idx = 2, s = "aab", partition = ["a", "a"], results = []
                - Loop i from 2 to 2
                - First iteration: i = 2
                   - substring = "b" from index 2 to 2
                   - Check if "b" is a palindrome → yes
                   - partition.append("b") → partition = ["a", "a", "b"]
                   - Call partition_palindrome_recursive("aab", 3, ["a", "a", "b"], results)
                      - start_idx = 3 == len(s) (3) → base case
                      - results.append(["a", "a", "b"]) → results = [["a", "a", "b"]]
                      - Return
                   - partition.pop() → partition = ["a", "a"]
                - partition.pop() → partition = ["a"]
             - partition.pop() → partition = ["a"]
          - Second iteration: i = 2
             - substring = "ab" from index 1 to 2
             - Check if "ab" is a palindrome → no (reads "ab" backwards is "ba")
             - Continue loop
       - partition.pop() → partition = []
    5. Second iteration: i = 1
       - substring = "aa" from index 0 to 1
       - Check if "aa" is a palindrome → yes
       - partition.append("aa") → partition = ["aa"]
       - Call partition_palindrome_recursive("aab", 2, ["aa"], results)
          - start_idx = 2, s = "aab", partition = ["aa"], results = [["a", "a", "b"]]
          - Loop i from 2 to 2
          - First iteration: i = 2
             - substring = "b" from index 2 to 2
             - Check if "b" is a palindrome → yes
             - partition.append("b") → partition = ["aa", "b"]
             - Call partition_palindrome_recursive("aab", 3, ["aa", "b"], results)
                - start_idx = 3 == len(s) (3) → base case
                - results.append(["aa", "b"]) → results = [["a", "a", "b"], ["aa", "b"]]
                - Return
             - partition.pop() → partition = ["aa"]
          - partition.pop() → partition = []
       - partition.pop() → partition = []
    6. Third iteration: i = 2
       - substring = "aab" from index 0 to 2
       - Check if "aab" is a palindrome → no (reads "aab" backwards is "baa")
       - Continue loop
    7. Loop completes, return results = [["a", "a", "b"], ["aa", "b"]]

Complexity Analysis:
    Time Complexity: O(n * 2^n)
    - For a string of length n, there are 2^n possible partitions
    - Each partition takes O(n) time to copy and add to results (worst case)
    - Checking if each substring is a palindrome takes O(n) time
    - Total time complexity: O(n * 2^n)
    - Space Complexity: O(n) for the current partition
    - O(n * 2^n) for storing all partitions in results

    Space Complexity:
    - O(n) for the current partition being built
    - O(n * 2^n) for the results list containing all partitions
    - O(n) for the recursion stack depth (in the worst case, it goes n levels deep)
    - O(n) for the temporary palindrome checks
    - Total space complexity is dominated by the results list

    Note:
    The space complexity grows exponentially with n, which makes this algorithm
    impractical for large strings (e.g., n > 15). For n = 15, the number of
    partitions can be in the hundreds. For large n, consider using dynamic
    programming to optimize the palindrome checking process, which can reduce
    the time complexity to O(n^2) for checking all possible partitions.

Note:
    The algorithm demonstrates the fundamental nature of backtracking for finding
    all valid solutions to a combinatorial problem. The key insight is that each
    decision point (at each index) represents a choice to include or not include
    a particular substring in the current partition. The recursion explores all
    possible combinations of these choices, but only keeps those where every
    chosen substring is a palindrome. The implementation has potential optimization
    opportunities:
    - Precompute a palindrome table using dynamic programming to avoid
      redundant palindrome checks
    - Use memoization to cache already computed results
    - Prune the search space by removing branches that cannot possibly form
      valid partitions
    Palindrome partitioning is a classic problem in algorithmic interviews and
    demonstrates the power of backtracking for constraint satisfaction problems.
    It's also related to more advanced topics like the partition problem,
    string manipulation algorithms, and dynamic programming optimization.
"""

def partition_palindrome(s: str) -> list[str]:
    """
    Wrapper function to partition a string into all possible palindrome substrings.

    Args:
        s: The input string to partition

    Returns:
        A list of all possible palindrome partitions, where each partition is
        represented as a list of strings
    """
    results = []
    current_partition = []

    partition_palindrome_recursive(s, 0, current_partition, results)

    return results


def partition_palindrome_recursive(s: str, start_idx: int, current_partition: list[str], results: list[list[str]]) -> None:
    """
    Recursive helper function to partition a string into palindrome substrings.

    Args:
        s: The input string to partition
        start_idx: The current starting index for exploration
        current_partition: The current list of substrings forming the palindrome partition
        results: The list to store all valid partitions
    """
    # Base case: we've reached the end of the string
    if start_idx == len(s):
        results.append(current_partition.copy())
        return

    # Try all possible substrings starting from start_idx
    for i in range(start_idx, len(s)):
        substring = s[start_idx:i + 1]

        # Check if the substring is a palindrome
        if is_palindrome(substring):
            # Include the substring in the current partition
            current_partition.append(substring)

            # Recursively partition the remaining string
            partition_palindrome_recursive(s, i + 1, current_partition, results)

            # Backtrack: remove the substring to try other possibilities
            current_partition.pop()


def is_palindrome(substring: str) -> bool:
    """
    Helper function to check if a string is a palindrome.

    Args:
        substring: The string to check

    Returns:
        True if the string is a palindrome, False otherwise
    """
    return substring == substring[::-1]
