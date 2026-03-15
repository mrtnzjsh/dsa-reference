"""Regular Expression Matching

# Algorithm: Dynamic programming
# Pattern: '.' matches any single char, '*' matches zero or more of preceding element
# Time: O(m × n), Space: O(m × n) or O(n) optimized
# Goal: Determine if string matches pattern according to rules
"""

from typing import List


def is_match(s: str, p: str) -> bool:
    """Check if string matches pattern with '.' and '*' wildcards."""
    m, n = len(s), len(p)
    
    # Initialize DP table
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Empty string matches empty pattern
    dp[0][0] = True
    
    # Empty string matches patterns that can be reduced to empty by '*'
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # Zero occurrences: skip pattern
                dp[i][j] = dp[i][j - 2]
                # One or more occurrences: check if current char matches
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # Match single character
                dp[i][j] = dp[i - 1][j - 1]
    
    return dp[m][n]


def is_match_space_optimized(s: str, p: str) -> bool:
    """Check if string matches pattern with space-optimized DP."""
    m, n = len(s), len(p)
    
    # Previous and current rows
    prev = [False] * (n + 1)
    prev[0] = True
    
    # Initialize first row
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            prev[j] = prev[j - 1]
    
    for i in range(1, m + 1):
        curr = [False] * (n + 1)
        
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # Zero or more occurrences
                curr[j] = curr[j - 2] or prev[j]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    curr[j] = curr[j] or prev[j - 1]
            elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # Match single character
                curr[j] = prev[j - 1]
        
        prev = curr
    
    return prev[n]


if __name__ == "__main__":
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("", "", True),
        ("", ".*", True),
        ("aaa", "aaaa", False),
        ("aaa", "a*a", True),
    ]
    
    for s, p, expected in test_cases:
        result1 = is_match(s, p)
        result2 = is_match_space_optimized(s, p)
        print(f"is_match('{s}', '{p}'): {result1}, optimized: {result2}, expected: {expected}")
        assert result1 == expected
        assert result2 == expected
