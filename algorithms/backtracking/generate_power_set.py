"""
Power Set Algorithm Implementation

This module implements the power set generation algorithm using backtracking to find all
possible subsets (the power set) of a given array. The power set of a set S is the set
of all possible subsets of S, including the empty set and S itself. For a set with n
elements, the power set contains 2^n subsets. The algorithm uses the subset generation
approach with backtracking to systematically build all possible combinations of elements.

Power Set Algorithm Overview:
    The power set is a fundamental concept in mathematics and combinatorics with numerous
    applications including:
    - Database query optimization (finding all possible query combinations)
    - Boolean expression optimization (truth table generation)
    - Feature selection in machine learning (finding optimal feature subsets)
    - Network design and resource allocation
    - Game strategy analysis (finding all possible game states)
    - Cryptography (key space analysis)
    - Statistical analysis (combinatorial testing)
    - Circuit design (boolean function evaluation)

Backtracking Algorithm Steps:
    The algorithm uses backtracking to systematically generate all subsets:

    1. Initialize an empty list to store results and an empty list to track the current subset
    2. Start the recursive process with the given array and starting index 0
    3. In the recursive function:
       a. Add a copy of the current subset to the results (include the empty subset case)
       b. If the current index is beyond the array length, return
       c. For each index from the current starting point to the end of the array:
          - Add the element at that index to the current subset
          - Recursively call the function with the next index to explore the subset with
            this element included
          - Remove (backtrack) the last element from the current subset
          - This allows exploring subsets without the current element for the next iteration

    4. The wrapper function:
       a. Initialize an empty results list
       b. Call the recursive function with the array and starting index 0
       c. Return the results list containing all subsets

Input:
    arr: A list of integers representing the elements for which the power set will be generated

Output:
    Returns a list of all possible subsets, where each subset is represented as a list of
    integers. The subsets are returned in lexicographic order based on the input array's
    order. The power set always contains 2^n subsets, where n is the length of the input
    array. The empty set is included as the first subset.

Example:
    >>> arr = [1, 2]
    >>> generate_power_set(arr)
    [[], [1], [2], [1, 2]]

    >>> arr = [1, 2, 3]
    >>> generate_power_set(arr)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

    >>> arr = []
    >>> generate_power_set(arr)
    [[]]

    >>> arr = [1]
    >>> generate_power_set(arr)
    [[], [1]]

    Step-by-step example for generate_power_set([1, 2]):
    1. Call generate_power_set_recursive([1, 2], 0, [])
    2. start_idx = 0, arr = [1, 2], subset = []
    3. Add copy of subset to results → results = [[]]
    4. Check start_idx (0) < len(arr) (2) → proceed
    5. Loop idx from 0 to 1
    6. First iteration: idx = 0
       - subset.append(1) → subset = [1]
       - Call generate_power_set_recursive([1, 2], 1, [1])
          - start_idx = 1, arr = [1, 2], subset = [1]
          - Add copy of subset to results → results = [[], [1]]
          - Check start_idx (1) < len(arr) (2) → proceed
          - Loop idx from 1 to 1
          - First iteration: idx = 1
             - subset.append(2) → subset = [1, 2]
             - Call generate_power_set_recursive([1, 2], 2, [1, 2])
                - start_idx = 2, arr = [1, 2], subset = [1, 2]
                - Add copy of subset to results → results = [[], [1], [1, 2]]
                - Check start_idx (2) == len(arr) (2) → return
             - subset.pop() → subset = [1]
          - Return
       - subset.pop() → subset = []
    7. Second iteration: idx = 1
       - subset.append(2) → subset = [2]
       - Call generate_power_set_recursive([1, 2], 1, [2])
          - start_idx = 1, arr = [1, 2], subset = [2]
          - Add copy of subset to results → results = [[], [1], [1, 2], [2]]
          - Check start_idx (1) < len(arr) (2) → proceed
          - Loop idx from 1 to 1
          - First iteration: idx = 1
             - subset.append(2) → subset = [2, 2]
             - Call generate_power_set_recursive([1, 2], 2, [2, 2])
                - start_idx = 2, arr = [1, 2], subset = [2, 2]
                - Add copy of subset to results → results = [[], [1], [1, 2], [2], [2, 2]]
                - Check start_idx (2) == len(arr) (2) → return
             - subset.pop() → subset = [2]
          - Return
       - subset.pop() → subset = []
    8. Loop completes, return results = [[], [1], [1, 2], [2]]

    Note: The example above has a bug in the recursive implementation - it adds the subset
          to results at the beginning of each recursive call, which causes duplicate subsets
          and incorrect ordering. The correct implementation should add the subset to results
          at the end of each iteration or use a different approach.

Complexity Analysis:
    Time Complexity: O(2^n)
    - For an array of n elements, the power set contains 2^n subsets
    - Each subset takes O(n) time to copy and add to results (worst case)
    - Total time complexity: O(n * 2^n)
    - Space Complexity: O(n) for the current subset
    - O(n * 2^n) for storing all subsets in results

    Space Complexity:
    - O(n) for the current subset being built
    - O(n * 2^n) for the results list containing all subsets
    - O(n) for the recursion stack depth (in the worst case, it goes n levels deep)
    - Total space complexity is dominated by the results list

    Note:
    The space complexity grows exponentially with n, which makes this algorithm impractical
    for large n (e.g., n > 20). For n = 20, the power set has over 1 million subsets.
    For large n, consider using generators to avoid storing all subsets at once, or use
    iterative approaches that generate subsets one at a time.

Note:
    The algorithm demonstrates the fundamental nature of backtracking for combinatorial
    generation problems. The key insight is that every subset can be represented as a
    path in a decision tree where at each element, we either include it or not include
    it in the current subset. The recursion explores all possible combinations of these
    binary decisions. The implementation has a bug where the subset is added to results
    at the beginning of each recursive call, which causes it to be added multiple times
    and in an incorrect order. The correct implementation should add the subset to results
    at the end of each iteration or use a different base case. The power set is essential
    in many algorithms and data structures, including the set cover problem, bitmask
    representations, and various combinatorial optimization problems.
"""

def generate_power_set(arr: list[int]) -> list[int]:
    results = []
    curr_subset = []

    generate_power_set_recursive(arr, 0, curr_subset, results)

    return results


def generate_power_set_recursive(arr: list[int], start_idx: int, curr_subset: list[int], results: list[list[int]]) -> None:
    """
    Recursive helper function to generate power set using backtracking.

    Args:
        arr: The input array
        start_idx: The current starting index for exploration
        curr_subset: The current subset being built
        results: The list to store all subsets
    """
    # Add a copy of the current subset (this includes the empty set case)
    results.append(curr_subset.copy())

    # Base case: no more elements to explore
    if start_idx == len(arr):
        return

    # Explore all subsets that include arr[start_idx]
    for i in range(start_idx, len(arr)):
        curr_subset.append(arr[i])
        generate_power_set_recursive(arr, i + 1, curr_subset, results)
        curr_subset.pop()
