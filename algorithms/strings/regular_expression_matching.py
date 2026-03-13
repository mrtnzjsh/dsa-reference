"""Regular Expression Matching

The regular expression matching problem asks us to determine if a given string matches a pattern that contains regular expression syntax including '.' (matches any single character) and '*' (matches zero or more of the preceding element). This is a classic dynamic programming problem with applications in text processing.

**Key Insight:**
Use dynamic programming to match the pattern against the string by building up solutions for smaller substrings. The pattern can include '.' for any single character and '*' for repeating the previous character any number of times.

**String Theory Background:**
A **regular expression** contains special characters:
- **'.'** matches any single character
- **'*'** matches zero or more of the preceding element
- Characters match themselves
- '*' means "repeat the previous element 0 or more times"

A string **matches** a pattern if there exists a complete match according to the pattern rules.

**Mathematical Foundation:**
Let S be the string (length m) and P be the pattern (length n).
Let match(i, j) be true if S[i:] matches P[j:].

Base cases:
- match(m, n) = True (both empty)
- match(i, m) = False (non-empty string with empty pattern)
- match(m, j) = match(m, j+1) if P[j] = '*' (empty string can be matched by * elements)

Recurrence:
match(i, j) = 
    if P[j+1] = '*':
        match(i, j+2) OR (match(i+1, j) AND (P[j] = '.' OR P[j] = S[i]))
    else:
        match(i+1, j+1) AND (P[j] = '.' OR P[j] = S[i])

**Algorithm Steps (DP):**
1. Create DP table with dimensions (m+1) × (n+1)
2. Initialize base cases for empty string and empty pattern
3. Fill DP table from bottom-right to top-left using the recurrence
4. Return dp[0][0]

**Example - Regular Expression Matching:**

Pattern: P = "a."
String: S = "aa"

Initialize DP table:
```
        ''   .   a
    +---+---+---+---+
''  | T | F | F | F |
    +---+---+---+---+
a   | F | F | F | T |
    +---+---+---+---+
a   | F | F | F | T |
    +---+---+---+---+
```

Filling the table:
- dp[0][0] = True
- dp[0][1] = False (pattern '.' doesn't match empty)
- dp[1][1] = False (pattern 'a' doesn't match empty)
- dp[1][2] = True (pattern 'a.' matches 'a')
- dp[2][2] = True (pattern 'a.' matches 'aa')

Final result: dp[0][0] = True
Pattern "a." matches string "aa" (a and .)

**Example - With Asterisk:**

Pattern: P = ".*"
String: S = "aa"

Step 1: P[1] = '*', so:
- match empty with "*": match(0, 2) = True (since dp[0][0] = True)
- Or: match(1, 1) AND ('.' = 'a') = True AND True = True

Result: True
Pattern ".*" matches string "aa" (zero or more 'a's)

**Time Complexity:**
- O(m × n) where m and n are the lengths of S and P

**Space Complexity:**
- O(m × n) for the full DP table
- O(n) for space-optimized version

**Space-Optimized Version:**
We only need the current and previous rows:
```
def isMatch(s, p):
    m, n = len(s), len(p)
    dp = [False] * (n + 1)
    dp[0] = True
    
    # Initialize first row
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[j] = dp[j - 1]
    
    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = False
        
        for j in range(1, n + 1):
            temp = dp[j]
            
            if p[j - 1] == '*':
                dp[j] = dp[j - 1] or dp[j]
            elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[j] = prev
            else:
                dp[j] = False
            
            prev = temp
    
    return dp[n]
```

**Algorithm Properties:**
The regex matching problem is:
- **Deterministic:** Clear rules for matching
- **Powerful:** Supports complex patterns
- **Computationally expensive:** Requires full DP for guaranteed correctness

**Trade-offs:**
**vs. Wildcard Matching:**
- Wildcard: '?' matches any single, '*' matches any sequence
- Regex: '.' matches any single, '*' matches repetition of previous element
- Regex is more powerful but more complex

**vs. Standard String Matching:**
- Standard: Exact character matching
- Regex: Pattern matching with wildcards
- Regex is more flexible

**Applications:**
- Text searching and validation
- URL pattern matching
- Code editor search
- Database queries
- Configuration validation
- Input validation systems

**Pattern Properties:**
- Patterns can be complex with nested constructs
- '*' always applies to the previous element
- Patterns can be optimized (e.g., remove redundant parts)
- Some patterns are equivalent in matching behavior

**Edge Cases:**
- Empty pattern: Matches only empty string
- Empty string: Matches if pattern can represent empty string (like "a*")
- Multiple consecutive '*' patterns: Must follow previous element
- Pattern with only '.' and '*': Can match any string

**Implementation Notes:**
The DP approach is the standard solution because:
1. It guarantees correct matching
2. It's easier to implement than backtracking
3. It's predictable in performance
4. It handles all edge cases correctly

**Performance Characteristics:**
- Linear in product of string and pattern lengths
- Handles moderate-sized inputs efficiently
- Can be slow for very large patterns
- Space-optimized version reduces memory usage

**Example - Complex Pattern:**

Pattern: P = "c*a*b"
String: S = "cb"

Step 1: Check pattern
- c* can match empty
- a* can match empty
- b must match 'c'

Result: False

Pattern "c*a*b" matches "aab" (c*→empty, a*→aa, b→b) but not "cb".

**Algorithm Variations:**
1. **Character classes:** Support [a-z], [A-Z], etc.
2. **Anchors:** Start (^) and end ($) patterns
3. **Alternation:** Support pattern matching with '|'
4. **Groups:** Support capturing groups
5. **Escaping:** Support escaping special characters

**Optimization Techniques:**
1. **Pattern preprocessing:** Remove redundant patterns
2. **Early termination:** Stop if pattern doesn't match remaining string
3. **Memoization:** Cache results for repeated substrings
4. **Backtracking:** Alternative approach for some patterns

**Example - Edge Case: Empty Pattern**

Pattern: P = ""
String: S = "a"

Step 1: Empty pattern
- Can only match empty string

Result: False

**Example - Edge Case: Multiple Star Patterns**

Pattern: P = "a*a*"
String: S = "aaa"

Step 1: Check pattern
- a* can match "aaa"
- a* can match empty

Result: True

**Comparison with Wildcard Matching:**
The key difference is how '*' is interpreted:
- Wildcard: '*' matches any sequence of characters
- Regex: '*' matches repetition of the previous character

This makes regex more precise and powerful but also more complex.

**Mathematical Properties:**
The regex matching problem is:
- **Undecidable** in general for arbitrary regular expressions (requires full regex engines)
- **Decidable** for our simplified version ('*' and '.' only)
- **P-complete** for our specific case

This is one of the few string problems that connects to computational complexity theory.
"""

from typing import List


def is_match(s: str, p: str) -> bool:
    """
    Determine if string s matches pattern p with '.' and '*' wildcards.
    
    Args:
        s: Input string
        p: Pattern with '.' (matches any single character) and '*' (matches zero or more of preceding element)
    
    Returns:
        True if s matches p, False otherwise
    
    Example:
        >>> is_match("aa", "a")
        False
        >>> is_match("aa", "a*")
        True
        >>> is_match("ab", ".*")
        True
        >>> is_match("aab", "c*a*b")
        True
    """
    m, n = len(s), len(p)
    
    # Create DP table
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty string matches empty pattern
    dp[0][0] = True
    
    # Base case: empty string matches pattern that can be reduced to empty by '*'
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' matches zero or more of the preceding element
                # Zero occurrences: skip the pattern
                dp[i][j] = dp[i][j - 2]
                # One or more occurrences: check if current character matches
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # '.' matches any single character, or exact match
                dp[i][j] = dp[i - 1][j - 1]
    
    return dp[m][n]


def is_match_space_optimized(s: str, p: str) -> bool:
    """
    Determine if string s matches pattern p with space-optimized DP.
    
    Args:
        s: Input string
        p: Pattern with '.' and '*' wildcards
    
    Returns:
        True if s matches p, False otherwise
    
    Example:
        >>> is_match_space_optimized("aa", "a")
        False
    """
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
                # '*' matches zero or more of the preceding element
                curr[j] = curr[j - 2] or prev[j]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    curr[j] = curr[j] or prev[j - 1]
            elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # '.' matches any single character, or exact match
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
