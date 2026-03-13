"""Wildcard Matching

The wildcard matching problem asks us to determine if a given string matches a pattern that contains wildcard characters ('?' matches any single character, '*' matches any sequence of characters). This is a classic string matching problem with important applications.

**Key Insight:**
Use dynamic programming to match the pattern against the string character by character, leveraging the fact that '*' can match any sequence. The DP approach builds up solutions from smaller subproblems, where we consider whether the first part of the pattern matches the first part of the string.

**String Theory Background:**
A **pattern** P contains characters and two special wildcards:
- **'?'** matches exactly one character (any character)
- **'*'** matches any sequence of characters (including empty sequence)

A string S **matches** pattern P if there exists a way to replace '?' with any character and '*' with any sequence so that P becomes S.

**Mathematical Foundation:**
Let S be the string (length m) and P be the pattern (length n).
Let match(i, j) be true if S[i:] matches P[j:].

Base cases:
- match(m, n) = True (both empty)
- match(m, j) = True only if all remaining P characters are '*'
- match(i, n) = False (non-empty S with empty P)

Recurrence:
match(i, j) = 
    if P[j] == '*': match(i, j+1) OR match(i+1, j)
    elif P[j] == '?': match(i+1, j+1)
    elif S[i] == P[j]: match(i+1, j+1)
    else: False

**Algorithm Steps (DP):**
1. Create DP table with dimensions (m+1) × (n+1)
2. Initialize base cases:
   - dp[m][n] = True (empty pattern matches empty string)
   - dp[i][n] = False for i < m (non-empty string can't match empty pattern)
   - dp[m][j] = dp[m][j+1] if P[j] = '*' (empty string matches only '*' sequences)
3. Fill DP table from bottom-right to top-left using the recurrence
4. Return dp[0][0]

**Example - Wildcard Matching:**

Pattern: P = "ad*c" 
String: S = "ahbgdc"

Initialize DP table:
```
        ''   a   d   *   c
    +---+---+---+---+---+
''  | T | F | F | F | F |
    +---+---+---+---+---+
a   | F | T | F | F | F |
    +---+---+---+---+---+
h   | F | F | F | T | F |
    +---+---+---+---+---+
b   | F | F | F | T | F |
    +---+---+---+---+---+
g   | F | F | F | T | F |
    +---+---+---+---+---+
d   | F | F | T | T | F |
    +---+---+---+---+---+
c   | F | F | F | T | T |
    +---+---+---+---+---+
```

Filling the table:
- dp[0][0] = True
- dp[0][1] = False (a doesn't match empty)
- ...
- dp[1][1] = True (a matches a)
- dp[1][2] = False (d doesn't match a)
- dp[2][4] = True (first * matches empty sequence, then a matches h)
- ... continues filling

Final result: dp[0][0] = True
Pattern "ad*c" matches string "ahbgdc" (via * matching "hb")

**Time Complexity:**
- DP: O(m × n) where m and n are the lengths of S and P
- Greedy with backtracking: O(m × n) worst case, O(m + n) average case

**Space Complexity:**
- DP: O(m × n) for the full table
- Greedy with backtracking: O(1) or O(n) for tracking

**Greedy Algorithm (Optimal Approach):**
For patterns with many '*' characters, greedy with backtracking performs better:
1. Track positions: s_pos = 0, p_pos = 0, last_star = 0, match = 0
2. Move p_pos forward matching characters
3. If '*' encountered, record its position and save current match position
4. If mismatch and there's a recorded '*', backtrack to last star and advance match
5. If no backtrack possible and no '*', return False
6. Continue until pattern or string is exhausted

**Example - Greedy Matching:**

Pattern: P = "*ad*c", String: S = "ahbgdc"

Step 1: s_pos = 0, p_pos = 0
- P[0] = '*', record last_star = 0, save match = 0

Step 2: p_pos = 1 (a)
- S[0] = 'a' matches P[1] = 'a'
- match = 0 (backtrack position)

Step 3: p_pos = 2 (d)
- S[1] = 'h' doesn't match P[2] = 'd'
- Backtrack: match = 1, p_pos = last_star = 0
- P[0] = '*', s_pos = match = 1

Step 4: p_pos = 1 (a)
- S[1] = 'h' doesn't match P[1] = 'a'
- No more '*' to backtrack
- Return False

Result: False

**Trade-offs:**
**vs. DP:**
- DP: Guaranteed O(m×n), handles all cases
- Greedy: Better average performance, handles some cases O(m+n)
- DP is simpler, greedy is faster in practice

**vs. Regular Expressions:**
- Wildcard: '?' and '*' only
- Regex: Full power of regex, more complex
- Wildcard is simpler, regex is more powerful

**Applications:**
- File path matching (shell wildcards)
- Search algorithms
- Data validation
- Text processing
- Configuration file parsing
- Game logic

**Pattern Properties:**
- A pattern with only '?' characters has exactly one match (each '?' = each char)
- A pattern with only '*' characters matches any string
- Patterns with multiple '*' can have multiple interpretations
- The greedy approach works well for patterns with few '*'

**Edge Cases:**
- Empty pattern: Matches only empty string
- Empty string: Matches if pattern is empty or all '*' characters
- Only '?': Length must match exactly
- Only '*': Always matches
- Consecutive '*' characters: Redundant (can be compressed)

**Implementation Notes:**
The greedy algorithm with backtracking is preferred for:
1. Better average performance
2. Lower memory usage
3. Easier to implement efficiently

The DP approach is useful for:
1. Simpler logic
2. Guaranteeing correctness
3. When '*' is rare

**Space-Optimized DP:**
We can optimize the DP table using only two rows:
- Keep track of the current and previous rows
- Space complexity reduces from O(m×n) to O(n)

**Performance Characteristics:**
- Very predictable O(m×n) worst case
- Often performs much better in practice
- Handles large patterns efficiently
- Linear space for greedy version

**Example - Edge Case: Empty String**

Pattern: P = "*"
String: S = ""

Step 1: p_pos = 0, P[0] = '*'
- Record last_star = 0, save match = 0

Step 2: p_pos = 1 (end of pattern)
- Both pattern and string exhausted
- Return True

Result: True

**Example - Edge Case: No Wildcards**

Pattern: P = "abc"
String: S = "abd"

Step 1: Compare characters
- 'a' == 'a'
- 'b' == 'b'
- 'c' != 'd'

Result: False

**Example - Complex Pattern:**

Pattern: P = "a?b*?c"
String: S = "abcd"

Step 1: 'a' matches 'a'
Step 2: '?' matches 'b'
Step 3: 'b' matches 'c' (but 'b' != 'c')

Result: False

The pattern requires 'b' to match 'c', but pattern says '?b*', not 'ab*'.

**Algorithm Variations:**
1. **Multiple wildcards:** Support other wildcard characters
2. **Wildcard restrictions:** '*' matches only non-empty sequences
3. **Pattern compression:** Remove consecutive '*' characters
4. **Partial matching:** Return longest match instead of boolean

**Optimization Techniques:**
1. **Pattern compression:** Remove consecutive '*' characters
2. **Early termination:** Stop matching early if impossible
3. **Character set filtering:** Check character types before matching
4. **Memoization:** Cache DP results for repeated patterns

This problem is particularly interesting because:
1. It demonstrates the power of dynamic programming
2. Shows trade-offs between different algorithms
3. Has practical applications in real-world systems
4. Can be solved multiple ways with different trade-offs
"""

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
