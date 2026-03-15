def partition_palindrome(s: str) -> list[str]:
    """
    Wrapper function to partition a string into all possible palindrome substrings.

    Args:
        s: The input string to partition

    Returns:
        A list of all possible palindrome partitions, where each partition is
        represented as a list of strings
    """
    results = []
    current_partition = []

    partition_palindrome_recursive(s, 0, current_partition, results)

    return results


def partition_palindrome_recursive(s: str, start_idx: int, current_partition: list[str], results: list[list[str]]) -> None:
    """
    Recursive helper function to partition a string into palindrome substrings.

    Args:
        s: The input string to partition
        start_idx: The current starting index for exploration
        current_partition: The current list of substrings forming the palindrome partition
        results: The list to store all valid partitions
    """
    # Base case: we've reached the end of the string
    if start_idx == len(s):
        results.append(current_partition.copy())
        return

    # Try all possible substrings starting from start_idx
    for i in range(start_idx, len(s)):
        substring = s[start_idx:i + 1]

        # Check if the substring is a palindrome
        if is_palindrome(substring):
            # Include the substring in the current partition
            current_partition.append(substring)

            # Recursively partition the remaining string
            partition_palindrome_recursive(s, i + 1, current_partition, results)

            # Backtrack: remove the substring to try other possibilities
            current_partition.pop()


def is_palindrome(substring: str) -> bool:
    """
    Helper function to check if a string is a palindrome.

    Args:
        substring: The string to check

    Returns:
        True if the string is a palindrome, False otherwise
    """
    return substring == substring[::-1]
