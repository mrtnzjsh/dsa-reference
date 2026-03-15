from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    """
    Determine if string s can be segmented into a space-separated sequence of words from word_dict.

    Args:
        s: Input string
        word_dict: List of valid words

    Returns:
        True if s can be segmented, False otherwise

    Example:
        >>> word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        True
        >>> word_break("catsandog", ["cat", "cats", "and", "sand", "dog"])
        False
    """
    word_set = set(word_dict)
    n = len(s)

    # dp[i] = True if s[0:i] can be segmented
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always segmentable

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


def word_break_with_segments(s: str, word_dict: List[str]) -> List[str]:
    """
    Find all possible segmentations of s using words from word_dict.

    Args:
        s: Input string
        word_dict: List of valid words

    Returns:
        List of all possible segmentations

    Example:
        >>> word_break_with_segments("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        ['cats and dog', 'cats and dog']
    """
    word_set = set(word_dict)
    n = len(s)

    # dp[i] = list of all segmentations of s[0:i]
    dp = [[] for _ in range(n + 1)]
    dp[0] = [""]  # Empty string has one segmentation

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                for seg in dp[j]:
                    if seg:
                        dp[i].append(seg + " " + s[j:i])
                    else:
                        dp[i].append(s[j:i])

    return dp[n]


if __name__ == "__main__":
    test_cases = [
        ("catsanddog", ["cat", "cats", "and", "sand", "dog"], True),
        ("catsandog", ["cat", "cats", "and", "sand", "dog"], False),
        ("leetcode", ["leet", "code"], True),
        ("", [], True),
        ("a", [], False),
    ]

    for s, word_dict, expected in test_cases:
        result = word_break(s, word_dict)
        print(f"word_break('{s}', {word_dict}): {result}, expected: {expected}")
        assert result == expected
