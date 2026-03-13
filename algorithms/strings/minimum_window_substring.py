"""Minimum Window Substring

The minimum window substring problem asks us to find the minimum substring of one string (S) that contains all characters of another string (T), including duplicates. This is a classic sliding window problem with applications in text processing and pattern matching.

**Key Insight:**
Use a sliding window approach to find the minimum substring containing all required characters. Maintain a count of required characters and expand/contract the window as needed to find the optimal solution.

**String Theory Background:**
A **window** is a contiguous substring of the original string.
A **minimum window** is the shortest window that contains all required characters.
**T contains all required characters** means: every character in T appears in the window with at least the same frequency.

**Mathematical Foundation:**
Let S be the string of length m, and T be the string of length n.
We need to find the minimum window S[i:j] such that:
- For every character c in T, frequency(c, S[i:j]) ≥ frequency(c, T)

**Algorithm Steps (Sliding Window):**
1. Build a frequency map of required characters in T
2. Initialize left pointer at 0, right pointer at 0
3. Expand the window by moving right pointer until we have all required characters
4. When we have all required characters, try to contract the window from the left
5. Track the minimum window length found
6. Continue until right pointer reaches the end of S

**Example - Minimum Window Substring:**

S = "ADOBECODEBANC", T = "ABC"

Required frequencies: {'A': 1, 'B': 1, 'C': 1}

Initialize: left = 0, right = 0
Map: {'A': 1, 'B': 1, 'C': 1}
Window: "A"

Step 1: right = 0, char = 'A'
- Map contains 'A', add to current map
- Current: {'A': 1}
- Required: {'A': 1, 'B': 1, 'C': 1}
- Not all required

Step 2: right = 1, char = 'D'
- Current: {'A': 1, 'D': 1}
- Not all required

Step 3: right = 2, char = 'O'
- Current: {'A': 1, 'D': 1, 'O': 1}
- Not all required

Step 4: right = 3, char = 'B'
- Current: {'A': 1, 'D': 1, 'O': 1, 'B': 1}
- Current: {'A': 1, 'B': 1}
- Still need 'C'

Step 5: right = 4, char = 'E'
- Current: {'A': 1, 'B': 1, 'E': 1}
- Still need 'C'

Step 6: right = 5, char = 'C'
- Current: {'A': 1, 'B': 1, 'C': 1, 'E': 1}
- Have all required: 'A', 'B', 'C'
- Try to contract from left
- Left = 0 ('A'): remove 'A', don't have all required
- Left = 1 ('D'): remove 'D', still have 'A', 'B', 'C'
- Check minimum: "ADOBEC" length 6, update minimum

Step 7: right = 6, char = 'O'
- Current: {'A': 1, 'B': 1, 'C': 1, 'E': 1, 'O': 1}
- Still have all required
- Try to contract
- Left = 2 ('O'): remove 'O', still have all required
- Left = 3 ('B'): remove 'B', don't have all required
- Check minimum: "OBECO" length 5, but need all required

Step 8: right = 7, char = 'D'
- Current: {...}
- Still have all required
- Try to contract
- Left = 4 ('E'): remove 'E', still have all required
- Left = 5 ('C'): remove 'C', don't have all required

Step 9: right = 8, char = 'E'
- Current: {...}
- Still have all required
- Try to contract
- Left = 6 ('O'): remove 'O', still have all required
- Left = 7 ('D'): remove 'D', still have all required
- Check minimum: "DEBECO" etc.

Step 10: right = 9, char = 'B'
- Current: {...}
- Still have all required
- Try to contract
- Left = 8 ('E'): remove 'E', still have all required
- Left = 9 ('B'): remove 'B', don't have all required

Step 11: right = 10, char = 'A'
- Current: {...}
- Have all required: 'A', 'B', 'C'
- Try to contract
- Left = 9 ('B'): remove 'B', still have 'A', 'B', 'C'
- Left = 10 ('A'): remove 'A', don't have all required
- Check minimum: "ODEBA" length 5

Step 12: right = 11, char = 'N'
- Current: {...}
- Still have all required
- Try to contract
- Left = 10 ('A'): remove 'A', still have all required
- Left = 11 ('N'): remove 'N', still have all required
- Check minimum: "DEBA" length 4

Step 13: right = 12, char = 'C'
- Current: {...}
- Have all required: 'A', 'B', 'C'
- Try to contract
- Left = 11 ('N'): remove 'N', still have all required
- Left = 12 ('C'): remove 'C', don't have all required

Final result: "BANC" length 4

**Time Complexity:**
- O(m + n) where m is the length of S and n is the length of T
- Each character is processed at most twice (once when expanding, once when contracting)

**Space Complexity:**
- O(1) for frequency maps (fixed size based on character set)
- O(n) in worst case for required frequency map

**Algorithm Properties:**
The sliding window approach ensures:
1. Each character is processed a constant number of times
2. The window always contains the required characters
3. We efficiently find the minimum window

**Trade-offs:**
**vs. Brute Force:**
- Brute Force: O(m × n) time, enumerates all possible windows
- Sliding Window: O(m + n) time, more efficient

**vs. Binary Search:**
- Binary Search: Not applicable for substring finding
- Sliding Window: Direct and efficient

**Applications:**
- Text processing and searching
- Pattern matching
- Data validation
- Content filtering
- Network packet inspection
- File searching

**Window Properties:**
- Always contains all required characters
- May contain extra characters
- The algorithm finds the minimal such window
- Multiple windows may exist, algorithm finds the shortest

**Edge Cases:**
- T longer than S: Return empty string (no possible window)
- No valid window: Return empty string
- T is empty: Return empty string (trivially satisfied)
- S is empty: Return empty string (can't find any window)
- Single character window: Return that character if it matches

**Implementation Notes:**
The sliding window approach is optimal because:
1. It processes each character exactly twice
2. It maintains the invariant that the current window is valid
3. It's easy to understand and implement
4. It handles all edge cases naturally

**Performance Characteristics:**
- Linear time complexity
- Very predictable behavior
- Works well for all reasonable string sizes
- Optimal for this problem type

**Example - Edge Case: T longer than S**

S = "ABC", T = "ABCDE"
- T has 5 characters, S has 3 characters
- Impossible to contain all characters
- Return: ""

**Example - Edge Case: Empty T**

S = "ABC", T = ""
- Empty T is trivially satisfied by any window
- By definition, return: ""

**Example - Edge Case: No Solution**

S = "ABC", T = "D"
- No window contains 'D'
- Return: ""

**Example - Multiple Valid Windows:**

S = "ABCDEF", T = "AC"
- Multiple windows contain 'A' and 'C': "ABC", "ADC", "AEC", "ABCDEF"
- Algorithm returns "ABC" (length 3)

**Optimization Techniques:**
1. **Character set filtering:** Check if all required characters exist in S first
2. **Length pruning:** Skip windows that can't be better than current minimum
3. **Frequency map reuse:** Track remaining required characters
4. **Early termination:** Stop if window length equals required length

**Mathematical Properties:**
The problem can be formulated as:
- Finding the minimal i, j such that ∀c: freq(c, S[i:j]) ≥ freq(c, T)
- This is a constrained optimization problem
- The sliding window provides an optimal solution

**Algorithm Variations:**
1. **Return all minimum windows:** Use sliding window with backtracking
2. **Count minimum occurrences:** Return count of distinct minimum windows
3. **Return position:** Return indices of minimum window
4. **Case insensitive:** Treat 'A' and 'a' as equivalent
5. **Custom match function:** Allow custom matching rules

**Alternative Approaches:**
1. **Sliding Window (shown above):** Optimal O(m + n) time
2. **Two-pointer with frequency counts:** Similar to sliding window
3. **Binary Search with matching test:** Not optimal
4. **Dynamic Programming:** Not optimal for this problem

**Performance Characteristics:**
- Excellent for most practical use cases
- Handles very large inputs efficiently
- Consistently linear time complexity
- Very predictable and reliable

This problem is particularly interesting because:
1. It demonstrates sliding window technique
2. Shows trade-offs between different approaches
3. Has practical applications
4. Can be extended in many ways
"""

from typing import List, Dict


def min_window(s: str, t: str) -> str:
    """
    Find the minimum substring of s that contains all characters of t.
    
    Args:
        s: Input string
        t: Target string
    
    Returns:
        The minimum window substring of s that contains all characters of t.
        Returns empty string if no such window exists.
    
    Example:
        >>> min_window("ADOBECODEBANC", "ABC")
        "BANC"
        >>> min_window("a", "a")
        "a"
        >>> min_window("a", "aa")
        ""
    """
    if not s or not t or len(t) > len(s):
        return ""
    
    # Count required characters
    required: Dict[str, int] = {}
    for char in t:
        required[char] = required.get(char, 0) + 1
    
    # Current window character counts
    window: Dict[str, int] = {}
    
    # Track how many required characters we have
    have = 0
    need = len(required)
    
    # Sliding window pointers
    left = 0
    min_length = float('inf')
    min_left = 0
    
    for right, char in enumerate(s):
        # Add current character to window
        if char in required:
            window[char] = window.get(char, 0) + 1
            if window[char] == required[char]:
                have += 1
        
        # Try to contract window
        while have == need:
            # Update minimum window
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_left = left
            
            # Remove leftmost character
            left_char = s[left]
            if left_char in required:
                if window[left_char] == required[left_char]:
                    have -= 1
                window[left_char] -= 1
            
            left += 1
    
    return "" if min_length == float('inf') else s[min_left:min_left + min_length]


def min_window_with_positions(s: str, t: str) -> Tuple[str, int, int]:
    """
    Find the minimum window substring with its start and end positions.
    
    Args:
        s: Input string
        t: Target string
    
    Returns:
        Tuple of (minimum_window, start_index, end_index)
    
    Example:
        >>> min_window_with_positions("ADOBECODEBANC", "ABC")
        ("BANC", 9, 12)
    """
    if not s or not t or len(t) > len(s):
        return ("", 0, 0)
    
    required: Dict[str, int] = {}
    for char in t:
        required[char] = required.get(char, 0) + 1
    
    window: Dict[str, int] = {}
    have = 0
    need = len(required)
    
    left = 0
    min_length = float('inf')
    min_left = 0
    min_right = 0
    
    for right, char in enumerate(s):
        if char in required:
            window[char] = window.get(char, 0) + 1
            if window[char] == required[char]:
                have += 1
        
        while have == need:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_left = left
                min_right = right
            
            left_char = s[left]
            if left_char in required:
                if window[left_char] == required[left_char]:
                    have -= 1
                window[left_char] -= 1
            
            left += 1
    
    if min_length == float('inf'):
        return ("", 0, 0)
    
    return (s[min_left:min_right + 1], min_left, min_right)


if __name__ == "__main__":
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("a", "", ""),
        ("", "a", ""),
        ("aa", "aa", "aa"),
        ("aa", "a", "a"),
        ("ab", "b", "b"),
        ("ab", "a", "a"),
        ("abc", "ac", "abc"),
    ]
    
    for s, t, expected in test_cases:
        result = min_window(s, t)
        print(f"min_window('{s}', '{t}'): '{result}', expected: '{expected}'")
        assert result == expected
