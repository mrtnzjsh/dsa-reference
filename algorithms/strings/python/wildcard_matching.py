"""Wildcard Matching Module"""

from typing import List


def is_match(s: str, p: str) -> bool:
    """
    Determine if string s matches pattern p with '?' and '*' wildcards.

    Args:
        s: Input string
        p: Pattern with '?' (matches any single character) and '*' (matches any sequence)

    Returns:
        True if s matches p, False otherwise

    Example:
        >>> is_match("aa", "a")
        False
        >>> is_match("aa", "*")
        True
        >>> is_match("cb", "?a")
        False
        >>> is_match("adceb", "*a*b")
        True
    """
    m, n = len(s), len(p)

    # Remove consecutive '*' characters for optimization
    optimized_p = []
    for char in p:
        if optimized_p and char == '*':
            continue
        optimized_p.append(char)
    p = ''.join(optimized_p)

    # Create DP table
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty string matches empty pattern
    dp[0][0] = True

    # Base case: empty string matches pattern of only '*' characters
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' matches empty or extends match
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                # '?' matches any character, or exact match
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]


def is_match_greedy(s: str, p: str) -> bool:
    """
    Determine if string s matches pattern p using greedy algorithm with backtracking.

    Args:
        s: Input string
        p: Pattern with '?' and '*' wildcards

    Returns:
        True if s matches p, False otherwise

    Example:
        >>> is_match_greedy("aa", "*")
        True
        >>> is_match_greedy("cb", "?a")
        False
    """
    m, n = len(s), len(p)

    # Remove consecutive '*' for optimization
    optimized_p = []
    for char in p:
        if optimized_p and char == '*':
            continue
        optimized_p.append(char)
    p = ''.join(optimized_p)
    n = len(p)

    # Track positions for backtracking
    s_pos = p_pos = 0
    star_pos = -1
    match_pos = 0

    while s_pos < m:
        if p_pos < n and (p[p_pos] == '?' or p[p_pos] == s[s_pos]):
            # Current characters match or '?' matches any
            s_pos += 1
            p_pos += 1
        elif p_pos < n and p[p_pos] == '*':
            # Record '*' position and match position
            star_pos = p_pos
            match_pos = s_pos
            p_pos += 1
        elif star_pos != -1:
            # Backtrack: use '*' to match more characters
            star_pos += 1
            match_pos += 1
            s_pos = match_pos
            p_pos = star_pos
        else:
            # No match and no '*' to backtrack
            return False

    # Skip remaining '*' in pattern
    while p_pos < n and p[p_pos] == '*':
        p_pos += 1

    return p_pos == n


if __name__ == "__main__":
    test_cases = [
        ("aa", "a", False),
        ("aa", "*", True),
        ("cb", "?a", False),
        ("adceb", "*a*b", True),
        ("acdcb", "a*c?b", False),
        ("", "*", True),
        ("", "", True),
        ("abc", "?*?*?", True),
        ("abc", "?*?*?b", False),
    ]

    for s, p, expected in test_cases:
        result1 = is_match(s, p)
        result2 = is_match_greedy(s, p)
        print(f"is_match('{s}', '{p}'): {result1}, greedy: {result2}, expected: {expected}")
        assert result1 == expected
        assert result2 == expected
