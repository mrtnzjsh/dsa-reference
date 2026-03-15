from typing import List, Tuple


def edit_distance(s: str, t: str) -> int:
    """
    Compute the Levenshtein distance between two strings.
    
    Args:
        s: First string
        t: Second string
    
    Returns:
        The minimum number of insertions, deletions, and substitutions
        required to transform s into t
    
    Example:
        >>> edit_distance("kitten", "sitting")
        3
        >>> edit_distance("", "")
        0
        >>> edit_distance("flaw", "lawn")
        2
    """
    m, n = len(s), len(t)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # Deletions
    for j in range(n + 1):
        dp[0][j] = j  # Insertions
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, no substitution needed
            if s[i - 1] == t[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            
            # Three operations:
            dp[i][j] = min(
                dp[i - 1][j] + 1,        # Deletion
                dp[i][j - 1] + 1,        # Insertion
                dp[i - 1][j - 1] + substitution_cost  # Substitution
            )
    
    return dp[m][n]


def edit_distance_optimized(s: str, t: str) -> int:
    # Ensure s is the longer string for space efficiency
    if len(s) < len(t):
        s, t = t, s
    
    # previous_row represents distances from empty string
    previous_row = list(range(len(t) + 1))
    
    for i in range(1, len(s) + 1):
        current_row = [i]  # Distance from s[:i] to empty string
        
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            
            current_row.append(min(
                previous_row[j] + 1,           # Deletion
                current_row[j - 1] + 1,        # Insertion
                previous_row[j - 1] + substitution_cost  # Substitution
            ))
        
        previous_row = current_row
    
    return previous_row[len(t)]


def edit_distance_with_operations(s: str, t: str) -> Tuple[int, List[Tuple[int, int, int]]]:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + substitution_cost
            )
    
    distance = dp[m][n]
    
    # Reconstruct operations
    operations = []
    i, j = m, n
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s[i - 1] == t[j - 1]:
            # Match
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            # Insertion
            operations.append(('insert', i + 1, t[j - 1]))
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            # Deletion
            operations.append(('delete', i, s[i - 1]))
            i -= 1
        else:
            # Substitution
            operations.append(('substitute', i, t[j - 1]))
            i -= 1
            j -= 1
    
    operations.reverse()
    return distance, operations


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("kitten", "sitting", 3),
        ("flaw", "lawn", 2),
        ("hello", "hello", 0),
        ("", "", 0),
        ("", "abc", 3),
        ("abc", "", 3),
        ("intention", "execution", 5),
    ]
    
    for s, t, expected in test_cases:
        result1 = edit_distance(s, t)
        result2 = edit_distance_optimized(s, t)
        print(f"edit_distance('{s}', '{t}'): {result1} (full), {result2} (opt)")
        assert result1 == expected
        assert result2 == expected
