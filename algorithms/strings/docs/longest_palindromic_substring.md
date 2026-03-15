# Longest Palindromic Substring

The longest palindromic substring problem asks us to find the longest contiguous substring of a given string that reads the same forward and backward. This is a classic string manipulation problem with multiple efficient solutions.

## Key Insight

A palindrome reads the same forwards and backwards, so its characters are symmetric around the center. By expanding around each possible center, we can efficiently find the longest palindrome without checking every substring.

## String Theory Background

A **palindrome** is a string that reads the same forward and backward: S[i] = S[n-1-i] for all i.
A **palindromic substring** is a contiguous sequence of characters within a string that forms a palindrome.

## Algorithm Steps (Expand Around Center)

For each position i in the string:
1. Consider two centers: the single character at position i (odd-length palindrome)
2. Consider the gap between characters i and i+1 (even-length palindrome)
3. Expand outwards from the center as long as characters match
4. Track the maximum length palindrome found

## Example - Finding Longest Palindrome

String: "babad"

Center at index 0 ('b'):
- Expand: (b) - no left or right to expand
- Length: 1

Center at index 1 ('a'):
- Odd expansion: (a) → (bab) → stop
  - Found palindrome "bab"
- Even expansion: (b,a) → no match
  - Length: 0

Center at index 2 ('b'):
- Odd expansion: (b) → (aba) → stop
  - Found palindrome "aba"
- Even expansion: (a,b) → no match

Center at index 3 ('a'):
- Odd expansion: (a) - no left or right
- Even expansion: (b,a) → no match

Center at index 4 ('d'):
- Odd expansion: (d) - no left or right

Result: Longest palindrome is "bab" or "aba" (both length 3)

## Algorithm Steps (Dynamic Programming)

1. Create a 2D DP table where dp[i][j] = True if S[i:j+1] is a palindrome
2. Base cases: Single characters are palindromes (dp[i][i] = True)
3. For length 2: Check if S[i] == S[i+1] (dp[i][i+1] = True if equal)
4. For length > 2: dp[i][j] = (S[i] == S[j]) AND dp[i+1][j-1]
5. Track the maximum length palindrome found

## Example - DP Approach

String: "racecar"

Initialize dp table (empty):

```
       r  a  c  e  c  a  r
    0: T  F  F  F  F  F  F
    1:   T  F  F  F  F  F
    2:     T  F  F  F  F
    3:       T  F  F  F
    4:         T  F  F
    5:           T  F
    6:             T
```

Fill table:
- Single characters: all True
- Length 2: (r,a) F, (a,c) F, (c,e) F, (e,c) F, (c,a) F, (a,r) F
- Length 3: (r,a,c) F, (a,c,e) F, (c,e,c) F, (e,c,a) F, (c,a,r) F
- Length 4: (r,a,c,e) F, (a,c,e,c) F, (c,e,c,a) F, (e,c,a,r) F
- Length 5: (r,a,c,e,c) F, (a,c,e,c,a) T (found "aceca")
- Length 6: (r,a,c,e,c,a) F
- Length 7: (r,a,c,e,c,a,r) T (found "racecar")

Result: "racecar" (length 7)

## Time Complexity

- Expand Around Center: O(n²) time, O(1) space
- Dynamic Programming: O(n²) time, O(n²) space

## Space Complexity

- Expand Around Center: O(1)
- Dynamic Programming: O(n²)

## Algorithm Comparison

### Expand Around Center
- Time: O(n²)
- Space: O(1)
- Pros: More memory efficient, simpler implementation
- Cons: Slower constant factors

### Dynamic Programming
- Time: O(n²)
- Space: O(n²)
- Pros: Easier to extend, useful for related problems
- Cons: Higher memory usage

### Manacher's Algorithm
- Time: O(n)
- Space: O(n)
- Pros: Linear time, optimal
- Cons: Complex implementation, not commonly used in interviews

## Trade-offs

### vs. DP
- Expand Around Center: Better for interviews, less memory
- DP: Better for optimization problems, easier to understand

### vs. Manacher's
- Expand Around Center: Good for interview scenarios
- Manacher's: Production use, linear time
- Manacher's is overkill for most practical purposes

## Algorithm Properties

If there are multiple palindromes of the same maximum length:
- Return any one (the problem doesn't specify which)
- In Expand Around Center, the first found is returned
- In DP, you need to track maximum indices

## Edge Cases

- Empty string: Return empty string
- Single character: Return the character
- All same characters: Return entire string
- No palindromes (length 1): Return any single character

## Applications

- Bioinformatics (DNA sequence analysis)
- Pattern matching and validation
- Text processing and search
- Game development (palindrome-related puzzles)
- Data compression
- Speech recognition

## String Properties

- A palindrome is symmetric around its center
- Odd-length palindromes have a single center character
- Even-length palindromes have a center between two characters
- The center expansion naturally handles both cases

## Implementation Notes

The Expand Around Center approach is preferred for interviews because:
1. O(n²) time is acceptable for typical string lengths
2. O(1) space is optimal
3. Simple implementation
4. Easy to explain and understand

Dynamic Programming is useful when:
1. You need DP solutions for related problems
2. Space constraints are less important
3. You want to see both approaches in an interview

## Example - Edge Case: Empty String

Input: ""
- No centers to expand
- Result: ""

## Example - Edge Case: All Same Characters

Input: "aaaaa"
- Expand from each center
- Center 0: "a", "aaaa" (max from left), "aaaaa"
- Center 2: "aaaaa"
- Center 4: "a", "aaaa" (max from right)
- Result: "aaaaa" (entire string)
