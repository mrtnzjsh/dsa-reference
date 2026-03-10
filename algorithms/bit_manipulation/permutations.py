"""
Algorithm: Generate Unique Permutations Using Bitmask

Time Complexity:
    is_idx_in_current_perm: O(1) - single bitwise AND operation
    print_all_unique_permutations: O(n * n!) where n is the length of the string
        - We generate n! unique permutations
        - For each permutation, we process n characters

Space Complexity:
    is_idx_in_current_perm: O(1) - only uses bitmask and temporary variables
    print_all_unique_permutations: O(n * n!) - O(n) for recursion stack depth,
        plus O(n!) for storing all permutations in the output list
"""


def is_idx_in_current_perm(idx: int, bitmask: int) -> bool:
    """
    Check if a specific index is already used in the current permutation.
    
    Algorithm:
        1. Create a mask with only the bit at idx position set to 1
        2. AND this mask with the current bitmask
        3. If result is non-zero, the index is already used
    """
    return (bitmask & (1 << idx)) != 0


def print_all_unique_permutations(remaining_str: str, perm: list[str], bitmask: int, perms: list[str]) -> None:
    """
    Generate all unique permutations of a string using backtracking with bitmask.
    
    This algorithm works step-by-step:
    1. Base case: When remaining_str is empty, we have a complete permutation
    2. For each character in remaining_str:
       a. Check if this index is already used in current permutation (bitmask)
       b. Skip if used
        c. Skip if character is duplicate of previous one and previous index was not used in this branch
           (this prevents duplicate recursive branches by ensuring we only follow one path for consecutive duplicates)
       d. Add character to current permutation
       e. Create new mask with this index bit set
       f. Recursively call with remaining characters
       g. Backtrack by removing the character from permutation
    3. Each unique combination creates one permutation string
    
    Args:
        remaining_str: String of characters still available to use
        perm: Current permutation being built (list of characters)
        bitmask: Integer bitmask tracking which indices are already used
        perms: List to collect all completed permutations
    
    Returns:
        None (results collected in perms list)
    """
    if not remaining_str:
        perms.append(''.join(perm))
        return

    for idx in range(len(remaining_str)):
        if is_idx_in_current_perm(idx, bitmask):
            continue

        if idx > 0 and remaining_str[idx] == remaining_str[idx - 1] and not is_idx_in_current_perm(idx - 1, bitmask):
            continue

        char = remaining_str[idx]
        new_mask = bitmask | (1 << idx)

        perm.append(char)
        print_all_unique_permutations(remaining_str[:idx] + remaining_str[idx+1:], perm, new_mask, perms)
        perm.pop()


input_str = "AAB"
sorted_str = sorted(input_str)
perms: list[str] = []
print_all_unique_permutations(''.join(sorted_str), [], 0, perms)
print(perms)
