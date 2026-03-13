"""Word Break Problem

The word break problem asks us to determine if a given string can be segmented into a space-separated sequence of one or more dictionary words. This is a classic dynamic programming problem with applications in natural language processing and spell checking.

**Key Insight:**
Use dynamic programming to build up a solution by checking if the prefix of the string can be broken into words. The key insight is that we only need to check previous DP values to determine the current state.

**String Theory Background:**
A **segmentation** is a way to break a string into substrings that correspond to words in a dictionary.
A string **can be broken** if there exists at least one valid sequence of words.

**Mathematical Foundation:**
Let S = s₁s₂...sₙ be a string of length n.
Let D be the dictionary of valid words.
Let dp[i] be true if the substring S[0:i] can be segmented into dictionary words.

Base cases:
- dp[0] = True (empty string is always segmentable)
- dp[i] for i > 0 is initially False

Recurrence:
dp[i] = OR over all words w in D of (dp[i - len(w)] AND (S[i - len(w):i] == w))

This means: substring S[0:i] is segmentable if any word in the dictionary matches the suffix and the prefix S[0:i-len(w)] is segmentable.

**Algorithm Steps (DP):**
1. Create DP array of size n+1, initialize all to False except dp[0] = True
2. For each position i from 1 to n:
   - For each word in the dictionary:
     - If word matches the suffix of S[0:i]:
       - If dp[i - len(word)] is True:
         - Set dp[i] = True
         - Break
3. Return dp[n]

**Example - Word Break:**

String: S = "catsanddog"
Dictionary: D = ["cat", "cats", "and", "sand", "dog"]

Initialize dp array:
dp[0] = True, dp[1] = False, dp[2] = False, ..., dp[10] = False

Processing:
i=1: "c" - no word matches
i=2: "ca" - no word matches
i=3: "cat" - matches! dp[0] = True, so dp[3] = True
i=4: "cats" - matches! dp[1] = False, so dp[4] remains False
i=5: "catsa" - no word matches
i=6: "catsan" - no word matches
i=7: "catsand" - no word matches
i=8: "catsandd" - no word matches
i=9: "catsanddo" - no word matches
i=10: "catsanddog" - "dog" matches! dp[7] = False, so dp[10] remains False

Wait, let me recalculate:
- dp[3] = True (cat)
- dp[4]: "cats" matches, but dp[1] = False
- dp[7]: "sand" matches with dp[3] = True, so dp[7] = True (cats + sand)
- dp[10]: "dog" matches with dp[7] = True, so dp[10] = True (cats + sand + dog)

Wait, let me re-check:
S = "catsanddog" (10 characters)
Dictionary: ["cat", "cats", "and", "sand", "dog"]

dp[0] = True
dp[1] = False
dp[2] = False
dp[3] = True (cat)
dp[4] = False (cats, but dp[1]=False)
dp[5] = False (catsa)
dp[6] = False (catsan)
dp[7] = True (sand with dp[3]=True) → cats + sand
dp[8] = False (sandd)
dp[9] = False (sanddo)
dp[10] = True (dog with dp[7]=True) → cats + sand + dog

Result: True
Segmentation: "catsanddog" = "cats" + "and" + "dog" or "cats" + "sand" + "dog"

**Time Complexity:**
- O(n × m × k) where n is string length, m is dictionary size, k is average word length
- In worst case, O(n²) when dictionary contains all possible substrings

**Space Complexity:**
- O(n) for the DP array

**Optimization with Trie:**
We can optimize by using a Trie data structure for the dictionary:
- Build a trie of dictionary words
- For each position i, traverse the trie while matching characters
- If we reach a word ending, check if the prefix is segmentable
- Reduces the complexity in many practical cases

**Algorithm Properties:**
The word break problem:
- **NP-complete** in general (determining all segmentations)
- **P-complete** for checking existence
- **DP is optimal** for existence checking
- **Space-optimized** DP uses O(n) space

**Trade-offs:**
**vs. Recursive with Memoization:**
- Recursive: Similar time complexity, simpler recursion
- DP: Explicit iteration, easier to implement
- Both are valid approaches

**vs. BFS:**
- BFS: Also O(n²) in worst case, useful for finding all paths
- DP: O(n²), simpler for single query
- Both work, DP is more common

**vs. Trie + DP:**
- Trie: Faster practical performance, more memory
- Standard DP: Simpler, adequate for most cases
- Trie is better for large dictionaries

**Applications:**
- Spell checking and correction
- Natural language processing
- Sentence segmentation
- Text analysis and text mining
- Input validation
- Code completion
- Database queries

**Dictionary Properties:**
- Can contain duplicates (handled automatically)
- Case sensitivity (usually handled explicitly)
- Empty strings (typically not in dictionary)
- Word length constraints (handled naturally)

**Edge Cases:**
- Empty string: Can always be segmented (empty segmentation)
- String not in dictionary: Needs checking
- Empty dictionary: Can only segment empty string
- String = single dictionary word: Always segmentable

**Implementation Notes:**
The DP approach is preferred because:
1. It's easy to understand and implement
2. It guarantees correctness
3. It's space-efficient
4. It handles all edge cases naturally

**Performance Characteristics:**
- Linear in string length times dictionary size
- Very predictable behavior
- Works well for moderate-sized inputs
- Can be slow for very long strings

**Alternative Approaches:**
1. **Recursive with Memoization:**
   ```
   def wordBreak(s, wordDict):
       @lru_cache(None)
       def canBreak(i):
           if i == len(s): return True
           for j in range(i+1, len(s)+1):
               if s[i:j] in wordDict and canBreak(j):
                   return True
           return False
       return canBreak(0)
   ```

2. **BFS:**
   - Build graph of possible breaks
   - Find path from start to end

3. **Trie + DP:**
   - Use Trie for dictionary lookup
   - More efficient for large dictionaries

**Example - No Solution:**

String: S = "leetcode"
Dictionary: D = ["leet", "code"]

Processing:
dp[0] = True
dp[4] = True (leet)
dp[8] = True (code with dp[4]=True)

Result: True
Segmentation: "leetcode" = "leet" + "code"

**Example - Multiple Solutions:**

String: S = "applepenapple"
Dictionary: D = ["apple", "pen"]

Processing:
dp[0] = True
dp[5] = True (apple)
dp[8] = True (pen with dp[3]=False)
dp[13] = True (apple with dp[8]=True)
dp[18] = True (apple with dp[13]=True)

Result: True
Segmentations: "apple" + "pen" + "apple" or "apple" + "pen" + "apple"

**Example - Edge Case: Empty Dictionary**

String: S = "hello"
Dictionary: D = []

Processing:
dp[0] = True
dp[1] = False
dp[2] = False
dp[3] = False
dp[4] = False
dp[5] = False

Result: False
Only empty string can be segmented with empty dictionary

**Algorithm Variations:**
1. **Return all segmentations:** Use backtracking with memoization
2. **Minimum segments:** Modify DP to track minimum number
3. **Maximum segments:** Track maximum
4. **Count segmentations:** Use combinatorics or DP with counting
5. **With word limits:** Each word can be used at most once

**Optimization Techniques:**
1. **Early termination:** Stop when solution found
2. **Word length pruning:** Skip words longer than remaining string
3. **Character set filtering:** Check character types before matching
4. **Memoization:** Cache expensive computations

**Mathematical Properties:**
The problem relates to:
- **String partitioning:** Finding valid partitions
- **Combinatorics:** Counting number of valid partitions
- **NP-completeness:** General case is hard
- **P-completeness:** Existence problem is hard but in P

This problem is particularly interesting because:
1. It demonstrates DP in action
2. Has practical real-world applications
3. Can be extended in many ways
4. Shows trade-offs between different approaches
"""

from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    """
    Determine if string s can be segmented into a space-separated sequence of words from word_dict.
    
    Args:
        s: Input string
        word_dict: List of valid words
    
    Returns:
        True if s can be segmented, False otherwise
    
    Example:
        >>> word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        True
        >>> word_break("catsandog", ["cat", "cats", "and", "sand", "dog"])
        False
    """
    word_set = set(word_dict)
    n = len(s)
    
    # dp[i] = True if s[0:i] can be segmented
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always segmentable
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]


def word_break_with_segments(s: str, word_dict: List[str]) -> List[str]:
    """
    Find all possible segmentations of s using words from word_dict.
    
    Args:
        s: Input string
        word_dict: List of valid words
    
    Returns:
        List of all possible segmentations
    
    Example:
        >>> word_break_with_segments("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        ['cats and dog', 'cats and dog']
    """
    word_set = set(word_dict)
    n = len(s)
    
    # dp[i] = list of all segmentations of s[0:i]
    dp = [[] for _ in range(n + 1)]
    dp[0] = [""]  # Empty string has one segmentation
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                for seg in dp[j]:
                    if seg:
                        dp[i].append(seg + " " + s[j:i])
                    else:
                        dp[i].append(s[j:i])
    
    return dp[n]


if __name__ == "__main__":
    test_cases = [
        ("catsanddog", ["cat", "cats", "and", "sand", "dog"], True),
        ("catsandog", ["cat", "cats", "and", "sand", "dog"], False),
        ("leetcode", ["leet", "code"], True),
        ("", [], True),
        ("a", [], False),
    ]
    
    for s, word_dict, expected in test_cases:
        result = word_break(s, word_dict)
        print(f"word_break('{s}', {word_dict}): {result}, expected: {expected}")
        assert result == expected
