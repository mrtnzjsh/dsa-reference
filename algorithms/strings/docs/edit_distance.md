# Edit Distance Algorithm

## Overview

This module implements the edit distance (Levenshtein distance) algorithm, which computes the minimum number of single-character edits (insertions, deletions, or substitutions) required to transform one string into another. The solution uses dynamic programming to efficiently compute this distance by building a matrix of subproblem solutions.

## Algorithm Steps

1. Create a (m+1) × (n+1) DP matrix where m and n are the lengths of the two input strings

2. Initialize the first row and column with base cases:
   - dp\[i\][0] = i (i deletions to transform s\[:i\] to empty string)
   - dp\[0\][j] = j (j insertions to transform empty string to t[:j])

3. Fill the matrix using the recurrence relation:
   - If s\[i-1\] == t[j-1], substitution_cost = 0, else substitution_cost = 1
   - dp\[i\][j] = min(
       dp\[i-1\][j] + 1,           # Deletion
       dp\[i\][j-1] + 1,           # Insertion
       dp\[i-1\][j-1] + substitution_cost  # Substitution
     )

4. Return the value at dp\[m\][n]

## Input

- `s`: First string of length m
- `t`: Second string of length n

## Output

Returns the minimum number of insertions, deletions, and substitutions required to transform s into t

## Example

```python
>>> edit_distance("kitten", "sitting")
3
>>> edit_distance("", "")
0
>>> edit_distance("flaw", "lawn")
2
```

### Step-by-step example for edit_distance("kitten", "sitting"):

1. Initialize DP table:

```
      ""  s   i   t   t   i   n   g
    +---+---+---+---+---+---+---+---+
""  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    +---+---+---+---+---+---+---+---+
k   | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    +---+---+---+---+---+---+---+---+
i   | 2 | 2 | 1 | 2 | 3 | 4 | 5 | 6 |
    +---+---+---+---+---+---+---+---+
t   | 3 | 3 | 2 | 1 | 2 | 3 | 4 | 5 |
    +---+---+---+---+---+---+---+---+
t   | 4 | 4 | 3 | 2 | 1 | 2 | 3 | 4 |
    +---+---+---+---+---+---+---+---+
e   | 5 | 5 | 4 | 3 | 2 | 2 | 3 | 4 |
    +---+---+---+---+---+---+---+---+
n   | 6 | 6 | 5 | 4 | 3 | 3 | 2 | 3 |
    +---+---+---+---+---+---+---+---+
```

2. Fill the table:

- d(1,1): min(1, 2, 1+1) = 1
- d(1,2): min(2, 1+1, 2+1) = 2
- Continue filling all cells using the recurrence

3. Final result: d(6,7) = 3

4. Operations to transform:
   - kitten → sitten (substitute k→s)
   - sitten → sittin (substitute e→i)
   - sittin → sitting (insert g)

## Complexity Analysis

### Time Complexity: O(m × n)

- Where m and n are the lengths of the two input strings
- The algorithm fills a matrix of size (m+1) × (n+1)
- Each cell requires constant time computation

### Space Complexity: O(m × n)

- O(m × n) for the full DP table
- O(min(m, n)) for the space-optimized version
- The optimized version only keeps two rows of the DP table

## Notes

The edit distance is a fundamental metric for string similarity with numerous applications:

- **Metrics Properties Satisfies identity, symmetry, and triangle inequality
- **Operations**: Supports insertion, deletion, and substitution of single characters
- **Variations**: Can be extended to weighted operations or different operation costs

**Trade-offs vs. Hamming Distance:**
- Hamming distance: Only works, requires equal length
- Edit distance: All operations, works for different lengths
- Edit distance is more general

**Space Optimization:**
The optimized version uses O(min(m, n)) space by keeping only the previous row of the DP table, reducing memory usage while maintaining the same time complexity.

**Applications:**
- Spell checking and correction
- DNA sequence comparison
- Text diff tools
- Fuzzy string matching
- Natural language processing
- Data deduplication