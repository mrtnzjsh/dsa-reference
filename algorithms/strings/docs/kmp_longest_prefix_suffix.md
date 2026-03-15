# KMP Longest Prefix Suffix (LPS) Algorithm

## Overview

Knuth-Morris-Pratt (KMP) algorithm efficiently finds all occurrences of pattern in text using LPS preprocessing. The algorithm uses an LPS array to store the length of the longest proper prefix which is also a suffix, avoiding re-examination of characters by using previously computed LPS values.

## Algorithm Steps

### LPS Array Construction
- `lps[i]` represents the length of the longest proper prefix of pattern[0..i] which is also a suffix
- Proper prefix: prefix that is not equal to the whole string
- Two cases during construction:
  1. Characters match (`process_string[i] == process_string[max_lps]`): Extend longest prefix-suffix by 1
  2. Characters don't match:
     - If `max_lps > 0`: use previous longest prefix-suffix value
     - If `max_lps == 0`: no proper prefix-suffix, set `lps[i] = 0`

### Matching Process
1. Initialize indices: `i = 0` (text index), `j = 0` (pattern index)
2. While `i < n` (end of text):
   - If `pattern[j] == text[i]`: characters match
     - Advance both indices (`i++`, `j++`)
     - If `j == m` (pattern length): pattern found
       - Store match position: `i - j`
       - Use LPS to allow overlapping matches: `j = lps[j - 1]`
   - Else: characters don't match
     - If `j > 0`: use LPS value to skip characters (`j = lps[j - 1]`)
     - Else: advance text index (`i++`)

## Input

- `pattern` (str): The pattern to search for
- `text` (str): The text to search in

## Output

- Prints positions where the pattern is found in the text
- Returns the LPS array for the pattern

## Example

**Pattern:** "ABABDABACDABABCABAB"
**Text:** "ABABDABACDABABCABAB"

**LPS array construction:**
- `lps[0] = 0` (no proper prefix)
- `lps[1] = 0` (AB vs B)
- `lps[2] = 1` (ABA vs A)
- `lps[3] = 2` (ABAB vs AB)
- `lps[4] = 0` (ABABD vs D)
- `lps[5] = 1` (ABABDA vs A)
- `lps[6] = 2` (ABABDAB vs AB)
- `lps[7] = 0` (ABABDABA vs C)
- `lps[8] = 0` (ABABDABAC vs D)
- `lps[9] = 1` (ABABDABACD vs A)
- `lps[10] = 2` (ABABDABACDA vs AB)
- `lps[11] = 3` (ABABDABACDAB vs ABC)
- `lps[12] = 0` (ABABDABACDABA vs C)
- `lps[13] = 1` (ABABDABACDABAB vs B)
- `lps[14] = 2` (ABABDABACDABABC vs AB)

**Matching example:**
- Index 0: Match ABAB (found at position 0)
- Use LPS to continue: `j = lps[3] = 2`
- Continue matching until another occurrence found

## Complexity Analysis

**Time Complexity:** O(n + m)
- Preprocessing: O(m) to build LPS array
- Matching: O(n) to scan the text
- Each character of text is examined at most once

**Space Complexity:** O(m)
- LPS array requires m space
- No additional space proportional to input size

## Notes

- LPS array gives longest prefix-suffix for each position
- During matching, mismatches are handled by using LPS instead of restarting from beginning
- Handles overlapping patterns correctly
- No backtracking in text comparison
- Traditional brute force: O(n × m) worst case
- KMP: O(n + m) guaranteed
