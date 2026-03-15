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
