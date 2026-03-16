# Wildcard Matching

## Overview

The wildcard matching problem asks us to determine if a given string matches a pattern that contains wildcard characters ('?' matches any single character, '*' matches any sequence of characters). This is a classic string matching problem with important applications.

## Algorithm Steps

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

**DP Algorithm Steps:**

1. Create DP table with dimensions (m+1) × (n+1)
2. Initialize base cases:
   - dp\[m\][n] = True (empty pattern matches empty string)
   - dp\[i\][n] = False for i < m (non-empty string can't match empty pattern)
   - dp\[m\][j] = dp\[m\][j+1] if P[j] = '*' (empty string matches only '*' sequences)
3. Fill DP table from bottom-right to top-left using the recurrence
4. Return dp\[0\][0]

**Greedy Algorithm (Optimal Approach):**

For patterns with many '*' characters, greedy with backtracking performs better:

1. Track positions: s_pos = 0, p_pos = 0, last_star = 0, match = 0
2. Move p_pos forward matching characters
3. If '*' encountered, record its position and save current match position
4. If mismatch and there's a recorded '*', backtrack to last star and advance match
5. If no backtrack possible and no '*', return False
6. Continue until pattern or string is exhausted

## Input

- **s**: Input string to match
- **p**: Pattern with '?' (matches any single character) and '*' (matches any sequence)

## Output

- **bool**: True if s matches p, False otherwise

## Example

**Pattern:** P = "ad*c"
**String:** S = "ahbgdc"

**DP Table Initialization:**

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

**Filling the table:**
- dp\[0\][0] = True
- dp\[0\][1] = False (a doesn't match empty)
- dp\[1\][1] = True (a matches a)
- dp\[1\][2] = False (d doesn't match a)
- dp\[2\][4] = True (first * matches empty sequence, then a matches h)
- Final result: dp\[0\][0] = True

Pattern "ad*c" matches string "ahbgdc" (via * matching "hb")

**Greedy Matching Example:**

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

## Complexity Analysis

**Time Complexity:**
- DP: O(m × n) where m and n are the lengths of S and P
- Greedy with backtracking: O(m × n) worst case, O(m + n) average case

**Space Complexity:**
- DP: O(m × n) for the full table
- Greedy with backtracking: O(1) or O(n) for tracking

## Notes

**Edge Cases:**
- Empty pattern: Matches only empty string
- Empty string: Matches if pattern is empty or all '*' characters
- Only '?': Length must match exactly
- Only '*': Always matches
- Consecutive '*' characters: Redundant (can be compressed)

**Trade-offs:**
vs. DP:
- DP: Guaranteed O(m×n), handles all cases
- Greedy: Better average performance, handles some cases O(m+n)
- DP is simpler, greedy is faster in practice

vs. Regular Expressions:
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

**Optimization Techniques:**
1. Pattern compression: Remove consecutive '*' characters
2. Early termination: Stop matching early if impossible
3. Character set filtering: Check character types before matching
4. Memoization: Cache DP results for repeated patterns
