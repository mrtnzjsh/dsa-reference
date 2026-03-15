# Robin-Karp Algorithm

## Overview

This module implements the Robin-Karp algorithm for pattern matching using a rolling hash technique. The algorithm efficiently searches for a pattern in a text by comparing hash values instead of characters, making it particularly useful for multiple pattern matching tasks. When hash values match, a direct character comparison is performed to verify the match.

## Algorithm Steps

1. **Precompute the highest power of the base modulo the prime**
   - Calculate `h = base^(m-1) mod prime`
   - This value is used for rolling hash computation

2. **Compute hash of the pattern and the initial text window**
   - Initialize `pattern_hash` and `text_hash` to 0
   - For each character in the pattern (length m):
     - `pattern_hash = (base × pattern_hash + char) mod prime`
   - For the first m characters of the text:
     - `text_hash = (base × text_hash + char) mod prime`

3. **Slide the window across the text**
   - For each possible starting position s from 0 to n-m:
     - Compare `pattern_hash` with `text_hash`
     - If they are equal:
       - Perform direct character comparison of all m characters
       - If all characters match: print "Pattern found at index", s
     - Calculate rolling hash for the next position:
       - `text_hash = (base × (text_hash - text[s] × h) + text[s+m]) mod prime`
       - This subtracts the contribution of the outgoing character
       - Multiplies by base to shift remaining hash
       - Adds the contribution of the new character

4. **Handle negative hash values**
   - If `text_hash` becomes negative after the modulo operation, add prime to correct it

## Input

- `pattern`: The string to search for
- `text`: The text in which to search for the pattern
- `base`: The base value for the rolling hash (typically 101 or 256)
- `prime`: The prime number for modulo operation (typically 10^9+7)

## Output

- Prints the indices where the pattern is found in the text
- Returns None (function executes for side effect of printing matches)

## Example

```python
>>> pattern = "abc"
>>> text = "xyzabcabcabc"
>>> robin_karp(pattern, text, base=101, prime=1000000007)
Pattern found at index 3
Pattern found at index 6
Pattern found at index 9
```

### Step-by-step example for pattern "abc" in text "xyzabcabcabc":

**Hash computation:**
- pattern = "abc", m = 3
- text = "xyzabcabcabc", n = 12
- base = 101, prime = 1000000007
- Precompute h = 101^(2) mod 1000000007 = 10201

**Initial hash values:**
- pattern_hash = (101 × (101 × (101 × 0 + 97)) + 98) mod 1000000007 = 989903
- text_hash = (101 × (101 × (101 × 0 + 120)) + 121) mod 1000000007 = 1233422

**First position s = 0:**
- Compare pattern_hash (989903) with text_hash (1233422) → not equal
- No direct comparison needed

**Second position s = 1:**
- Compare pattern_hash (989903) with text_hash (1331444) → not equal
- No direct comparison needed

**Third position s = 2:**
- Compare pattern_hash (989903) with text_hash (1439429) → not equal
- No direct comparison needed

**Fourth position s = 3:**
- Compare pattern_hash (989903) with text_hash (989903) → equal!
- Direct comparison: text[3]='a' == 'a', text[4]='b' == 'b', text[5]='c' == 'c'
- **Print "Pattern found at index 3"**

**Fifth position s = 4:**
- Update rolling hash:
  - text_hash = (101 × (989903 - 120 × 10201) + 97) mod 1000000007 = 1013926
- Compare pattern_hash (989903) with text_hash (1013926) → not equal

**Sixth position s = 5:**
- Update rolling hash:
  - text_hash = (101 × (1013926 - 121 × 10201) + 98) mod 1000000007 = 1021903
- Compare pattern_hash (989903) with text_hash (1021903) → not equal

**Seventh position s = 6:**
- Update rolling hash:
  - text_hash = (101 × (1021903 - 122 × 10201) + 97) mod 1000000007 = 1029912
- Compare pattern_hash (989903) with text_hash (1029912) → not equal

**Eighth position s = 7:**
- Update rolling hash:
  - text_hash = (101 × (1029912 - 97 × 10201) + 98) mod 1000000007 = 1028103
- Compare pattern_hash (989903) with text_hash (1028103) → not equal

**Ninth position s = 8:**
- Update rolling hash:
  - text_hash = (101 × (1028103 - 98 × 10201) + 97) mod 1000000007 = 1036226
- Compare pattern_hash (989903) with text_hash (1036226) → not equal

**Tenth position s = 9:**
- Update rolling hash:
  - text_hash = (101 × (1036226 - 99 × 10201) + 98) mod 1000000007 = 1034357
- Compare pattern_hash (989903) with text_hash (1034357) → not equal

**Eleventh position s = 10:**
- Update rolling hash:
  - text_hash = (101 × (1034357 - 100 × 10201) + 97) mod 1000000007 = 1042500
- Compare pattern_hash (989903) with text_hash (1042500) → not equal

**Twelfth position s = 11:**
- Update rolling hash:
  - text_hash = (101 × (1042500 - 101 × 10201) + 98) mod 1000000007 = 1050673
- Compare pattern_hash (989903) with text_hash (1050673) → not equal

**Pattern found at indices 3, 6, and 9**
- The rolling hash technique efficiently skips positions where hash values don't match
- Direct comparison only happens when hash values match

## Complexity Analysis

### Time Complexity: O(n + m)

- **Best case**: O(m) when the pattern is found at the very beginning
- **Average case**: O(n + m) when most hash comparisons are O(1) and hash collisions are rare
- **Worst case**: O(n × m) when there are many hash collisions requiring full character comparison

**Breakdown:**
- Hash computation for pattern: O(m)
- Initial hash computation for text: O(m)
- Rolling hash updates: O(1) per position × O(n) = O(n)
- Hash comparisons: O(n) comparisons
- Verification (when hashes match): O(m) per match

### Space Complexity: O(1)

- Only stores hash values (`pattern_hash`, `text_hash`, `h`)
- Precomputed power values
- No additional data structures proportional to input size

## Notes

**Rolling Hash Technique:**
- Hash of string s = (s[0] × b^(m-1) + s[1] × b^(m-2) + ... + s[m-1] × b^0) mod p
- Where b = base, p = prime
- Precomputed value h = b^(m-1) mod p allows efficient hash updates
- Rolling hash formula: `text_hash = (base × (text_hash - text[s] × h) + text[s+m]) mod prime`

**Why Use Different Base and Prime:**
- **Base**: Typically 101 or 256 (number of characters in alphabet)
- **Prime**: Large prime (10^9+7) to reduce hash collisions
- Choice affects collision frequency and speed
- A good base and prime combination makes hash collisions extremely rare

**Collision Handling:**
- Hash collisions can occur but are unlikely with good base and prime
- Direct character comparison resolves collisions
- Raising base and prime reduces collision probability

**Advantages:**
- Faster than naive O(n × m) when most hash comparisons are O(1)
- Handles multiple patterns efficiently (compare hashes first)
- Rolling hash makes hash updates O(1)
- No backtracking needed

**Disadvantages:**
- Hash collisions can degrade performance to O(n × m)
- Requires careful choice of base and prime
- Not as efficient as KMP for single pattern matching
- More complex implementation

**Use Cases:**
- Multiple pattern matching (e.g., find many words in text)
- DNA sequence matching
- File content detection (similar files have similar hashes)
- When hash comparison is expected to be much faster than direct comparison

**Typical Parameters:**
- base = 101 or 256 (number of characters)
- prime = 10^9+7 or 2^31-1 (large prime)
- Works well for lowercase English letters
