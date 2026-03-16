# Longest Common Subsequence

## Overview

The Longest Common Subsequence (LCS) algorithm finds the length of the longest sequence that appears in the same order in two given sequences, but not necessarily contiguously. A subsequence is a sequence that can be derived from another sequence by deleting zero or more elements without changing the order of the remaining elements.

## Applications

- Bioinformatics (comparing DNA or protein sequences)
- Version control systems (diff and merge operations)
- Text analysis and plagiarism detection
- Computer vision and image comparison
- Data compression (string matching)
- Compiler design (syntax analysis)
- Network protocols (packet sequencing)
- Cryptography (pattern matching and sequence comparison)

## Algorithm Steps

The algorithm uses a 2D DP table to store solutions to subproblems:

1. Create a 2D array dp\[m+1\][n+1] where:
   - dp\[i\][j] represents the length of the LCS of X[0..i-1] and Y[0..j-1]

2. Initialize dp\[0\][j] = 0 for all j (empty X → LCS length 0)

3. Initialize dp\[i\][0] = 0 for all i (empty Y → LCS length 0)

4. Fill the DP table:
   - For i from 1 to m:
     - For j from 1 to n:
       - If X[i-1] == Y[j-1]:
         - dp\[i\][j] = dp\[i-1\][j-1] + 1 (characters match, include in LCS)
       - Else:
         - dp\[i\][j] = max(dp\[i-1\][j], dp\[i\][j-1]) (take max of ignoring one character)

5. The answer is dp\[m\][n] - the length of the LCS

## Input

- text1: A string representing the first sequence
- text2: A string representing the second sequence

## Output

Returns the length of the longest common subsequence

## Example

### Example 1:
```python
text1 = "abcde"
text2 = "ace"
longest_common_subsequence(text1, text2)
```
Output: `3`
Explanation: "ace" is the LCS

### Example 2:
```python
text1 = "abc"
text2 = "abc"
longest_common_subsequence(text1, text2)
```
Output: `3`
Explanation: The entire strings match

### Example 3:
```python
text1 = "abc"
text2 = "def"
longest_common_subsequence(text1, text2)
```
Output: `0`
Explanation: No common characters

### Example 4:
```python
text1 = "mtux"
text2 = "tuc"
longest_common_subsequence(text1, text2)
```
Output: `3`
Explanation: "tuc" is the LCS

## Step-by-Step Breakdown

### Example: longest_common_subsequence("abcde", "ace")

Create dp table of size 6×6 (indices 0-5)

**Initialize:**
```
dp\[0\][j] = 0 for all j
dp\[i\][0] = 0 for all i
```

**Fill the table:**

**Row 1 (text1\[0\] = 'a'):**
- j=1: text2\[0\] = 'a' == 'a' → dp\[1\][1] = dp\[0\][0] + 1 = 1
- j=2: text2\[1\] = 'c' != 'a' → dp\[1\][2] = max(dp\[0\][2]=0, dp\[1\][1]=1) = 1
- j=3: text2\[2\] = 'e' != 'a' → dp\[1\][3] = max(dp\[0\][3]=0, dp\[1\][2]=1) = 1
- j=4: text2\[3\] = '' → dp\[1\][4] = 0 (no match)
- j=5: text2\[4\] = '' → dp\[1\][5] = 0

**Row 2 (text1\[1\] = 'b'):**
- j=1: text2\[0\] = 'a' != 'b' → dp\[2\][1] = max(dp\[1\][1]=1, dp\[2\][0]=0) = 1
- j=2: text2\[1\] = 'c' != 'b' → dp\[2\][2] = max(dp\[1\][2]=1, dp\[2\][1]=1) = 1
- j=3: text2\[2\] = 'e' != 'b' → dp\[2\][3] = max(dp\[1\][3]=1, dp\[2\][2]=1) = 1
- j=4: text2\[3\] = '' → dp\[2\][4] = 0
- j=5: text2\[4\] = '' → dp\[2\][5] = 0

**Row 3 (text1\[2\] = 'c'):**
- j=1: text2\[0\] = 'a' != 'c' → dp\[3\][1] = max(dp\[2\][1]=1, dp\[3\][0]=0) = 1
- j=2: text2\[1\] = 'c' == 'c' → dp\[3\][2] = dp\[2\][1] + 1 = 2
- j=3: text2\[2\] = 'e' != 'c' → dp\[3\][3] = max(dp\[2\][3]=1, dp\[3\][2]=2) = 2
- j=4: text2\[3\] = '' → dp\[3\][4] = 0
- j=5: text2\[4\] = '' → dp\[3\][5] = 0

**Row 4 (text1\[3\] = 'd'):**
- j=1: text2\[0\] = 'a' != 'd' → dp\[4\][1] = max(dp\[3\][1]=1, dp\[4\][0]=0) = 1
- j=2: text2\[1\] = 'c' != 'd' → dp\[4\][2] = max(dp\[3\][2]=2, dp\[4\][1]=1) = 2
- j=3: text2\[2\] = 'e' != 'd' → dp\[4\][3] = max(dp\[3\][3]=2, dp\[4\][2]=2) = 2
- j=4: text2\[3\] = '' → dp\[4\][4] = 0
- j=5: text2\[4\] = '' → dp\[4\][5] = 0

**Row 5 (text1\[4\] = 'e'):**
- j=1: text2\[0\] = 'a' != 'e' → dp\[5\][1] = max(dp\[4\][1]=1, dp\[5\][0]=0) = 1
- j=2: text2\[1\] = 'c' != 'e' → dp\[5\][2] = max(dp\[4\][2]=2, dp\[5\][1]=1) = 2
- j=3: text2\[2\] = 'e' == 'e' → dp\[5\][3] = dp\[4\][2] + 1 = 3
- j=4: text2\[3\] = '' → dp\[5\][4] = 0
- j=5: text2\[4\] = '' → dp\[5\][5] = 0

**Final result:** dp\[5\][3] = 3

The LCS is "ace"

## Complexity Analysis

### Time Complexity: O(m × n)
- m: Length of the first sequence
- n: Length of the second sequence
- We fill an (m+1) × (n+1) table, performing O(1) work per cell

### Space Complexity: O(m × n)
- The 2D DP table requires O(m × n) space
- Space can be optimized to O(min(m, n)) using space optimization

#### Space Optimization
We can optimize the space complexity from O(m × n) to O(min(m, n)) by using:
- A 1D DP array that we update iteratively
- The key insight is that dp\[i\][j] only depends on dp\[i-1\][j] and dp\[i\][j-1]
- By iterating j from n to 1, we ensure we always use the previous iteration's value

#### Additional Space
- For finding the actual LCS string: O(m + n) additional space
- Total space complexity is O(m × n) in the standard implementation

## Notes

The LCS problem is a classic dynamic programming problem that demonstrates the principle of optimal substructure and overlapping subproblems. The key insight is that the optimal solution for length i,j can be built from optimal solutions for smaller lengths. The algorithm is efficient for comparing sequences of moderate size, but the time and space complexity grow quadratically with the sequence lengths. For very large sequences, consider using the meet-in-the-middle algorithms or using Hirschberg's algorithm for finding the actual LCS string.

The LCS problem has numerous real-world applications including bioinformatics, version control, text analysis, and compiler design. It's also related to the edit distance problem, which measures the minimum number of operations needed to transform one string into another.
