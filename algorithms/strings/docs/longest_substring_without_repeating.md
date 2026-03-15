# Longest Substring Without Repeating Characters

## Overview

This module implements the longest substring without repeating characters algorithm, which finds the maximum length of a contiguous substring containing no duplicate characters. The solution uses a sliding window approach with hash map tracking for optimal performance.

## Algorithm Steps

1. Initialize two pointers: `left` = 0, `max_length` = 0
2. Initialize an empty hash map to store character positions
3. Iterate through the string with right pointer:
   - If the character is already in the window (position >= left), move left pointer to position+1
   - Update the character's position in the hash map
   - Calculate current window length and update max_length
4. Return max_length when iteration completes

## Input

- `s`: Input string

## Output

Returns the maximum length of a substring without repeating characters

## Example

```python
>>> length_of_longest_substring("abcabcbb")
3
>>> length_of_longest_substring("bbbbb")
1
>>> length_of_longest_substring("pwwkew")
3
>>> length_of_longest_substring("")
0
```

### Step-by-step example for "abcabcbb"

Initial state: left = 0, max_len = 0, Map: {}

**Step 1:** right = 0, char = 'a'
- 'a' not in map, update max_len = 1
- Map: {'a': 0}

**Step 2:** right = 1, char = 'b'
- 'b' not in map, update max_len = 2
- Map: {'a': 0, 'b': 1}

**Step 3:** right = 2, char = 'c'
- 'c' not in map, update max_len = 3
- Map: {'a': 0, 'b': 1, 'c': 2}

**Step 4:** right = 3, char = 'a'
- 'a' is in map at position 0
- Move left to max(0, 0+1) = 1
- Update max_len = max(3, 3-1) = 3
- Map: {'a': 3, 'b': 1, 'c': 2}

**Step 5:** right = 4, char = 'b'
- 'b' is in map at position 1
- Move left to max(1, 1+1) = 2
- Update max_len = max(3, 4-2) = 3
- Map: {'a': 3, 'b': 4, 'c': 2}

**Step 6:** right = 5, char = 'c'
- 'c' is in map at position 2
- Move left to max(2, 2+1) = 3
- Update max_len = max(3, 5-3) = 3
- Map: {'a': 3, 'b': 4, 'c': 5}

**Step 7:** right = 6, char = 'b'
- 'b' is in map at position 4
- Move left to max(3, 4+1) = 5
- Update max_len = max(3, 6-5) = 3
- Map: {'a': 3, 'b': 6, 'c': 5}

**Step 8:** right = 7, char = 'b'
- 'b' is in map at position 6
- Move left to max(5, 6+1) = 7
- Update max_len = max(3, 7-7) = 3
- Map: {'a': 3, 'b': 7, 'c': 5}

**Result:** Longest substring without repeating characters is "abc" (length 3)

## Complexity Analysis

### Time Complexity: O(n)

- Each character is processed exactly twice
- Once when expanding the right pointer
- Once when potentially moving the left pointer
- The hash map provides O(1) average-time complexity for lookups

### Space Complexity: O(min(n, m))

- m is the size of the character set
- Hash map stores at most one entry per unique character
- O(1) for ASCII (256 possible characters)
- O(n) for Unicode in worst case

## Notes

The sliding window approach ensures:
1. Each character is visited at most twice
2. The window always contains unique characters
3. Maximum window size is tracked efficiently

### Trade-offs

**vs. Brute Force:**
- Brute Force: O(n²) time, O(n) space
- Sliding Window: O(n) time, O(min(n, m)) space
- Sliding window is significantly faster

**vs. Dynamic Programming:**
- DP: O(n²) time, O(n) space
- Sliding Window: O(n) time, O(min(n, m)) space
- Sliding window is more efficient

### Applications

- String analysis and validation
- Data compression
- Text processing
- Pattern recognition
- Authentication systems
- Password validation

### Edge Cases

- Empty string: Return 0
- All unique characters: Return length of string
- All same characters: Return 1
- String with no duplicates until end: Return full length
