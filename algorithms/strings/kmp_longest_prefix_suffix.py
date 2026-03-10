"""
Knuth-Morris-Pratt (KMP) algorithm for pattern matching using LPS (Longest Prefix Suffix) preprocessing.

Algorithm Overview:
- KMP efficiently finds all occurrences of pattern in text by preprocessing the pattern
- Uses LPS array to store the length of longest proper prefix which is also suffix
- Avoids re-examining characters by using previously computed LPS values

LPS Array Construction (preprocess function):
- lps[i] represents length of longest proper prefix of pattern[0..i] which is also suffix
- Proper prefix: prefix that is not equal to the whole string
- Two cases:
  1. Characters match (process_string[i] == process_string[max_lps]):
     * Extend longest prefix-suffix by 1
     * max_lps increases, store in lps[i]
  2. Characters don't match:
     * If max_lps > 0: use previous longest prefix-suffix value (pattern[max_lps-1..i-1])
     * If max_lps == 0: no proper prefix-suffix, set lps[i] = 0

Matching Process (kmp_algorithm function):
1. Initialize indices: i = 0 (text index), j = 0 (pattern index)
2. While i < n (end of text):
   - If pattern[j] == text[i]: characters match
     * Advance both indices (i++, j++)
     * If j reaches pattern length (j == m): pattern found
       - Store match position: i - j
       * Use LPS to allow overlapping matches: j = lps[j - 1]
   - Else: characters don't match
     * If j > 0: use LPS value to skip characters (j = lps[j - 1])
     * Else: advance text index (i++)

Key Insights:
- LPS array gives longest prefix-suffix for each position
- During matching, mismatches are handled by using LPS instead of restarting from beginning
- Time complexity: O(n + m) where n = text length, m = pattern length
- Space complexity: O(m) for LPS array
- Handles overlapping patterns correctly
- No backtracking in text comparison

KMP Advantage:
- Traditional brute force: O(n × m) worst case
- KMP: O(n + m) guaranteed
- LPS preprocessing makes each character of text examined at most once

Pattern: "ABABDABACDABABCABAB"
LPS array:
- lps[0] = 0 (no proper prefix)
- lps[1] = 0 (AB vs B)
- lps[2] = 1 (ABA vs A)
- lps[3] = 2 (ABAB vs AB)
- lps[4] = 0 (ABABD vs D)
- lps[5] = 1 (ABABDA vs A)
- lps[6] = 2 (ABABDAB vs AB)
- lps[7] = 0 (ABABDABA vs C)
- lps[8] = 0 (ABABDABAC vs D)
- lps[9] = 1 (ABABDABACD vs A)
- lps[10] = 2 (ABABDABACDA vs AB)
- lps[11] = 3 (ABABDABACDAB vs ABC)
- lps[12] = 0 (ABABDABACDABA vs C)
- lps[13] = 1 (ABABDABACDABAB vs B)
- lps[14] = 2 (ABABDABACDABABC vs AB)

Used for:
- Pattern matching in strings
- DNA sequence analysis
- Text editors (find/replace)
- Data compression algorithms
"""

def preprocess(process_string: str) -> list:
    m = len(process_string)
    lps = [0] * m
    max_lps = 0
    i = 1

    while i < m:
        if process_string[i] == process_string[max_lps]:
            max_lps += 1
            lps[i] = max_lps
            i += 1
        else:
            if max_lps != 0:
                max_lps = lps[max_lps - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_algorithm(pattern: str, text: str):
    m = len(pattern)
    n = len(text)

    lps = preprocess(pattern)

    i, j = 0, 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
            if j == m:
                print("Pattern found at index", (i - j))
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
