"""Longest Palindromic Substring

# Algorithm: Expand around center
# Time: O(n²), Space: O(1)
# Alternative: Dynamic programming (O(n²) space)
# Notes: Find longest substring that reads the same forward and backward
"""

from typing import List


def longest_palindromic_substring(s: str) -> str:
    """Find longest palindromic substring using expand around center."""
    # Handle edge cases
    if not s or len(s) == 1:
        return s
    
    start = 0
    max_length = 1
    
    def expand_around_center(left: int, right: int) -> int:
        # Expand while characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return palindrome length
        return right - left - 1
    
    # Check each position as center
    for i in range(len(s)):
        # Check odd-length palindromes
        length1 = expand_around_center(i, i)
        # Check even-length palindromes
        length2 = expand_around_center(i, i + 1)
        
        # Track longest palindrome found
        current_max = max(length1, length2)
        if current_max > max_length:
            max_length = current_max
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_length]


def longest_palindromic_substring_dp(s: str) -> str:
    """Find longest palindromic substring using dynamic programming."""
    if not s:
        return s
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    start = 0
    max_length = 1
    
    # Initialize single-character palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check longer palindromes
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_length = length
    
    return s[start:start + max_length]


if __name__ == "__main__":
    # Test cases
    test_cases = [
        "babad",
        "cbbd",
        "a",
        "",
        "aaaaa",
        "racecar",
        "abcdef",
        "bbbab",
    ]
    
    for test in test_cases:
        result1 = longest_palindromic_substring(test)
        result2 = longest_palindromic_substring_dp(test)
        print(f"'{test}': '{result1}' (expand), '{result2}' (dp)")
