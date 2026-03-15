
from typing import List, Dict, Tuple


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
