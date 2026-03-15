# Word Break Algorithm

## Overview

This module implements the word break algorithm, which determines if a given string can be segmented into a space-separated sequence of one or more dictionary words. The solution uses dynamic programming to efficiently check if a string can be broken into valid words.

## Algorithm Steps

1. Create a DP array of size n+1 where n is the length of the input string, initialized with False
2. Set dp[0] = True (empty string is always segmentable)
3. For each position i from 1 to n:
   - For each position j from 0 to i-1:
     - If dp[j] is True and the substring s[j:i] is in the dictionary:
       - Set dp[i] = True
       - Break

4. Return dp[n]

## Input

- `s`: The input string to check
- `word_dict`: A list of valid words from which to segment the string

## Output

Returns `True` if the string can be segmented into dictionary words, `False` otherwise

## Example

```python
>>> word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"])
True
>>> word_break("catsandog", ["cat", "cats", "and", "sand", "dog"])
False
>>> word_break("", [])
True
>>> word_break("a", [])
False
```

### Step-by-step example for word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"]):

1. Initialize dp array: [True, False, False, False, False, False, False, False, False, False, False]

2. Processing:
   - i=1: "c" - no word matches, dp[1] remains False
   - i=2: "ca" - no word matches, dp[2] remains False
   - i=3: "cat" - matches! dp[0] = True, so dp[3] = True
   - i=4: "cats" - matches, but dp[1] = False, so dp[4] remains False
   - i=5: "catsa" - no word matches, dp[5] remains False
   - i=6: "catsan" - no word matches, dp[6] remains False
   - i=7: "catsand" - no word matches, dp[7] remains False
   - i=8: "catsandd" - no word matches, dp[8] remains False
   - i=9: "catsanddo" - no word matches, dp[9] remains False
   - i=10: "catsanddog" - "dog" matches! dp[7] = False, so dp[10] remains False

3. Recalculate with correct dp values:
   - dp[3] = True (cat)
   - dp[4] = False (cats, but dp[1]=False)
   - dp[7] = True (sand with dp[3]=True) → cats + sand
   - dp[10] = True (dog with dp[7]=True) → cats + sand + dog

4. Final result: dp[10] = True

5. Valid segmentations: "cats and dog" or "cats sand dog"

## Complexity Analysis

### Time Complexity: O(n × m)

Where:
- n is the length of the input string
- m is the dictionary size

In the worst case, we check all substrings for each position.

### Space Complexity: O(n)

- O(n) for the DP array
- O(m) for the word set (converting list to set)

## Notes

The word break problem has several important properties and considerations:

**Algorithm Properties:**
- NP-complete for determining all segmentations
- P-complete for checking existence
- DP is optimal for existence checking

**Trade-offs:**
- **vs. Recursive with Memoization:** Both have O(n²) time complexity, DP is often simpler to implement
- **vs. BFS:** Both have O(n²) worst case, DP is more common for single queries
- **vs. Trie + DP:** Trie is faster for large dictionaries but uses more memory

**Applications:**
- Spell checking and correction
- Natural language processing
- Sentence segmentation
- Text analysis and text mining
- Input validation
- Code completion
- Database queries

**Edge Cases:**
- Empty string: Can always be segmented (empty segmentation)
- Single dictionary word: Always segmentable
- Empty dictionary: Can only segment empty string

**Optimization Techniques:**
- Early termination when solution found
- Word length pruning (skip words longer than remaining string)
- Character set filtering before matching
- Memoization for recursive approaches

**Mathematical Foundation:**
The problem relates to string partitioning, combinatorics, and NP-completeness theory. The DP recurrence is:
dp[i] = OR over all words w in D of (dp[i - len(w)] AND (S[i - len(w):i] == w))
