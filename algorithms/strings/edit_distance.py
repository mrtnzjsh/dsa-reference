"""Edit Distance / Levenshtein Distance

The edit distance (also known as Levenshtein distance) measures the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into another. It's a fundamental metric for string similarity and has numerous applications.

**Key Insight:**
The edit distance can be computed using dynamic programming by building a matrix where each cell represents the distance between substrings of the two strings. The solution builds up from smaller substrings to the full strings.

**String Theory Background:**
Let S and T be two strings of lengths m and n.
The **Levenshtein distance** is the minimum number of operations needed to transform S into T.
Three operations are allowed:
1. **Insertion:** Insert a character into S
2. **Deletion:** Remove a character from S
3. **Substitution:** Replace a character in S with another

**Mathematical Foundation:**
Let d(i,j) represent the edit distance between the first i characters of S and first j characters of T.

Base cases:
- d(0,0) = 0 (empty string to empty string)
- d(i,0) = i (i deletions to transform S[:i] to empty)
- d(0,j) = j (j insertions to transform empty to T[:j])

Recurrence:
d(i,j) = min(
    d(i-1,j) + 1,        # deletion
    d(i,j-1) + 1,        # insertion
    d(i-1,j-1) + cost    # substitution (cost = 0 if S[i-1] == T[j-1], else 1)
)

**Algorithm Steps:**
1. Create a (m+1) × (n+1) DP matrix
2. Initialize the first row and column (base cases)
3. Fill the matrix using the recurrence relation
4. Return the value at d(m,n)

**Example - Computing Edit Distance:**

Strings: S = "kitten", T = "sitting"

Initialize DP table:
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

Filling the table:
- d(1,1): min(1, 2, 1+1) = 1
- d(1,2): min(2, 1+1, 2+1) = 2
- ... continues filling

Final result: d(6,7) = 3

**Operations to transform:**
kitten → sitten (substitute k→s)
sitten → sittin (substitute e→i)
sittin → sitting (insert g)

**Time Complexity:**
- O(m × n) where m and n are the lengths of the two strings

**Space Complexity:**
- O(m × n) for the full DP table
- O(min(m, n)) for space-optimized version

**Space Optimized Version:**
We only need the previous row to compute the current row, so we can reduce space to O(min(m, n)).

**Algorithm Properties:**
The edit distance is:
- **Metric:** Satisfies identity, symmetry, and triangle inequality
- **Translation invariant:** Inserting same characters at start/end doesn't change distance
- **Penalty-based:** Different penalties for different operations

**Trade-offs:**
**vs. Hamming Distance:**
- Hamming: Only substitutions, requires equal length
- Edit Distance: All operations, works for different lengths
- Edit Distance is more general

**vs. Damerau-Levenshtein:**
- Damerau: Also includes transposition (adjacent swap)
- Edit Distance: Simpler, doesn't handle swaps
- Damerau is more accurate for some cases

**Applications:**
- Spell checking and correction
- DNA sequence comparison
- Text diff tools
- Fuzzy string matching
- Natural language processing
- Music and audio comparison
- Data deduplication

**Distance Properties:**
- d(S,T) = 0 if and only if S = T
- d(S,T) = d(T,S) (symmetric)
- d(S,T) ≥ |d(S,U) - d(T,U)| (triangle inequality)

**Dynamic Programming vs. Recursive:**
- Recursive: Exponential time without memoization, O(m×n) with memoization
- DP: Always O(m×n) time and space
- DP is preferred for implementation

**Prefix vs. General Edit Distance:**
- **General:** Full strings, O(m×n) time
- **Prefix:** Find longest common prefix, can be optimized
- **General** is the standard formulation

**Implementation Notes:**
The DP approach is optimal because:
1. It builds up from simple subproblems
2. It avoids redundant calculations
3. It's easy to implement and understand

**Space-Optimized Version:**
```
def edit_distance_optimized(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    
    # s1 is longer string, s2 is shorter
    previous_row = list(range(len(s2) + 1))
    
    for i in range(1, len(s1) + 1):
        current_row = [i]
        
        for j in range(1, len(s2) + 1):
            insertions = previous_row[j] + 1
            deletions = current_row[j-1] + 1
            substitutions = previous_row[j-1] + (s1[i-1] != s2[j-1])
            
            current_row.append(min(insertions, deletions, substitutions))
        
        previous_row = current_row
    
    return previous_row[len(s2)]
```

This uses O(min(m,n)) space by always keeping only two rows.

**Example - Empty String:**

S = "hello", T = ""

Initial: previous_row = [0, 1, 2, 3, 4, 5]

After processing:
- All insertions, final distance = 5

**Example - Identical Strings:**

S = "hello", T = "hello"

Final distance = 0

**Example - Substrings:**

S = "abcdefgh", T = "aceg"

This is not a direct application of edit distance, but can be computed as if padding with matches.

**Algorithm Variations:**
1. **Weighted operations:** Different costs for insertions vs. deletions
2. **Case sensitivity:** Treat 'A' and 'a' as equal or different
3. **Phonetic similarity:** Specialized algorithms for word similarity
4. **Block-level edits:** Consider whole words or phrases as units

**Performance Characteristics:**
- Linear in product of string lengths
- Very predictable and reproducible
- Works well for strings of moderate length
- Can be slow for very large strings (≥10⁵ characters)
"""

from typing import List


def edit_distance(s: str, t: str) -> int:
    """
    Compute the Levenshtein distance between two strings.
    
    Args:
        s: First string
        t: Second string
    
    Returns:
        The minimum number of insertions, deletions, and substitutions
        required to transform s into t
    
    Example:
        >>> edit_distance("kitten", "sitting")
        3
        >>> edit_distance("", "")
        0
        >>> edit_distance("flaw", "lawn")
        2
    """
    m, n = len(s), len(t)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # Deletions
    for j in range(n + 1):
        dp[0][j] = j  # Insertions
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, no substitution needed
            if s[i - 1] == t[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            
            # Three operations:
            dp[i][j] = min(
                dp[i - 1][j] + 1,        # Deletion
                dp[i][j - 1] + 1,        # Insertion
                dp[i - 1][j - 1] + substitution_cost  # Substitution
            )
    
    return dp[m][n]


def edit_distance_optimized(s: str, t: str) -> int:
    """
    Compute the Levenshtein distance using space-optimized DP.
    
    Args:
        s: First string
        t: Second string
    
    Returns:
        The Levenshtein distance
    
    Example:
        >>> edit_distance_optimized("kitten", "sitting")
        3
    """
    # Ensure s is the longer string for space efficiency
    if len(s) < len(t):
        s, t = t, s
    
    # previous_row represents distances from empty string
    previous_row = list(range(len(t) + 1))
    
    for i in range(1, len(s) + 1):
        current_row = [i]  # Distance from s[:i] to empty string
        
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            
            current_row.append(min(
                previous_row[j] + 1,           # Deletion
                current_row[j - 1] + 1,        # Insertion
                previous_row[j - 1] + substitution_cost  # Substitution
            ))
        
        previous_row = current_row
    
    return previous_row[len(t)]


def edit_distance_with_operations(s: str, t: str) -> Tuple[int, List[Tuple[int, int, int]]]:
    """
    Compute the Levenshtein distance and track the operations.
    
    Args:
        s: First string
        t: Second string
    
    Returns:
        Tuple of (distance, operations) where operations are tuples of (type, position)
    
    Example:
        >>> edit_distance_with_operations("kitten", "sitting")
        (3, [...])
    """
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + substitution_cost
            )
    
    distance = dp[m][n]
    
    # Reconstruct operations
    operations = []
    i, j = m, n
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s[i - 1] == t[j - 1]:
            # Match
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            # Insertion
            operations.append(('insert', i + 1, t[j - 1]))
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            # Deletion
            operations.append(('delete', i, s[i - 1]))
            i -= 1
        else:
            # Substitution
            operations.append(('substitute', i, t[j - 1]))
            i -= 1
            j -= 1
    
    operations.reverse()
    return distance, operations


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("kitten", "sitting", 3),
        ("flaw", "lawn", 2),
        ("hello", "hello", 0),
        ("", "", 0),
        ("", "abc", 3),
        ("abc", "", 3),
        ("intention", "execution", 5),
    ]
    
    for s, t, expected in test_cases:
        result1 = edit_distance(s, t)
        result2 = edit_distance_optimized(s, t)
        print(f"edit_distance('{s}', '{t}'): {result1} (full), {result2} (opt)")
        assert result1 == expected
        assert result2 == expected
