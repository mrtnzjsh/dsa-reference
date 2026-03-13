"""Longest Substring Without Repeating Characters

The longest substring without repeating characters problem asks us to find the length of the longest substring of a given string that contains no repeating characters. This is a classic sliding window problem that can be solved efficiently.

**Key Insight:**
Use a sliding window approach to track the longest substring without duplicates. The window expands as we move the right pointer and contracts when we encounter a duplicate character. This ensures we only need O(n) time with a hash map for constant-time lookups.

**String Theory Background:**
A **substring** is a contiguous sequence of characters within a string.
A **repeating character** appears more than once in the substring.
The **longest substring without repeating characters** is the maximum length substring where all characters are distinct.

**Mathematical Foundation:**
Let S = s₁s₂...sₙ be a string of length n.
A substring S[i:j] (exclusive) has no repeating characters if:
∀<tool_call>write<arg_key>content</arg_key><arg_value>"""Longest Substring Without Repeating Characters

The longest substring without repeating characters problem asks us to find the maximum length of a contiguous substring that contains no repeating characters.

**Key Insight:**
Use a sliding window approach with a hash map to track character positions. As we move through the string, maintain a window [left, right] that contains all unique characters. When we find a duplicate, move the left pointer to after the previous occurrence of that character.

**Algorithm Steps:**
1. Use a sliding window with two pointers: left and right
2. Use a hash map to store the most recent position of each character
3. Expand the window by moving right pointer:
   - If character at right is not in the map or is outside the window, continue
   - If character is in the window, move left pointer to max(left, position+1)
4. Update the maximum length found
5. Continue until right reaches the end of the string

**Example - Finding Longest Unique Substring:**

String: "abcabcbb"

Initial: left = 0, max_len = 0
Map: {}

Step 1: right = 0, char = 'a'
- 'a' not in map, update max_len = 1
- Map: {'a': 0}

Step 2: right = 1, char = 'b'
- 'b' not in map, update max_len = 2
- Map: {'a': 0, 'b': 1}

Step 3: right = 2, char = 'c'
- 'c' not in map, update max_len = 3
- Map: {'a': 0, 'b': 1, 'c': 2}

Step 4: right = 3, char = 'a'
- 'a' is in map at position 0
- Move left to max(0, 0+1) = 1
- Update max_len = max(3, 3-1) = 3
- Map: {'a': 3, 'b': 1, 'c': 2}

Step 5: right = 4, char = 'b'
- 'b' is in map at position 1
- Move left to max(1, 1+1) = 2
- Update max_len = max(3, 4-2) = 3
- Map: {'a': 3, 'b': 4, 'c': 2}

Step 6: right = 5, char = 'c'
- 'c' is in map at position 2
- Move left to max(2, 2+1) = 3
- Update max_len = max(3, 5-3) = 3
- Map: {'a': 3, 'b': 4, 'c': 5}

Step 7: right = 6, char = 'b'
- 'b' is in map at position 4
- Move left to max(3, 4+1) = 5
- Update max_len = max(3, 6-5) = 3
- Map: {'a': 3, 'b': 6, 'c': 5}

Step 8: right = 7, char = 'b'
- 'b' is in map at position 6
- Move left to max(5, 6+1) = 7
- Update max_len = max(3, 7-7) = 3
- Map: {'a': 3, 'b': 7, 'c': 5}

Result: Longest substring without repeating characters is "abc" (length 3)

**Time Complexity:**
- O(n) where n is the length of the string
- Each character is processed exactly twice (left and right pointers)

**Space Complexity:**
- O(min(n, m)) where m is the size of the character set
- Hash map stores at most one entry per unique character

**Algorithm Properties:**
The sliding window approach ensures:
1. Each character is visited at most twice
2. The window always contains unique characters
3. We track the maximum window size efficiently

**Trade-offs:**
**vs. Brute Force:**
- Brute Force: O(n²) time, O(n) space
- Sliding Window: O(n) time, O(min(n, m)) space
- Sliding window is significantly faster

**vs. Dynamic Programming:**
- DP: O(n²) time, O(n) space
- Sliding Window: O(n) time, O(min(n, m)) space
- Sliding window is more efficient

**Character Set Considerations:**
- ASCII: O(1) space (256 possible characters)
- Unicode: O(n) space in worst case
- Using a fixed-size array for ASCII is more efficient

**Edge Cases:**
- Empty string: Return 0
- All unique characters: Return length of string
- All same characters: Return 1
- String with no duplicates until end: Return full length

**Applications:**
- String analysis and validation
- Data compression
- Text processing
- Pattern recognition
- Authentication systems
- Password validation

**Implementation Notes:**
The sliding window approach is optimal because:
1. It maintains the invariant that the window [left, right] contains unique characters
2. Each character is added and removed at most once
3. The hash map provides O(1) lookups

This makes it one of the few string problems that can achieve O(n) time complexity.

**Alternative Approaches:**
1. **Brute Force:** Generate all substrings and check for uniqueness
   - Time: O(n²), Space: O(n)
   - Simple but slow

2. **Dynamic Programming:** dp[i] = length of longest substring ending at i
   - Time: O(n²), Space: O(n)
   - More complex than needed

3. **Set-based sliding window:** Use a set instead of hash map
   - Time: O(n) amortized, Space: O(min(n, m))
   - Similar to hash map but slightly slower

**Example - Edge Case: All Same Characters**

Input: "aaaaa"

Step 1: right = 0, char = 'a'
- Add to window, max_len = 1
- Map: {'a': 0}

Step 2: right = 1, char = 'a'
- 'a' in window at position 0
- Move left to 1
- max_len = max(1, 1-1) = 1

Step 3: right = 2, char = 'a'
- 'a' in window at position 1
- Move left to 2
- max_len = max(1, 2-2) = 1

... continues until the end

Result: 1 (single 'a')
"""

from typing import Dict


def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
    
    Returns:
        Maximum length of substring without repeating characters
    
    Example:
        >>> length_of_longest_substring("abcabcbb")
        3
        >>> length_of_longest_substring("bbbbb")
        1
        >>> length_of_longest_substring("pwwkew")
        3
        >>> length_of_longest_substring("")
        0
    """
    char_map: Dict[str, int] = {}
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        # If character is in the window, move left pointer
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        
        # Update character position
        char_map[char] = right
        
        # Update maximum length
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
    
    return max_length


def length_of_longest_substring_set(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters using a set.
    
    Args:
        s: Input string
    
    Returns:
        Maximum length of substring without repeating characters
    
    Example:
        >>> length_of_longest_substring_set("abcabcbb")
        3
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        # If character is already in the set, remove from left until it's gone
        while char in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to set
        char_set.add(char)
        
        # Update maximum length
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
    
    return max_length


if __name__ == "__main__":
    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
        "abcdef",
        "dvdf",
        "abba",
    ]
    
    for test in test_cases:
        result1 = length_of_longest_substring(test)
        result2 = length_of_longest_substring_set(test)
        print(f"'{test}': {result1} (map), {result2} (set)")
