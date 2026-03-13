"""
Combinations Generation Algorithm Implementation

This module implements the combination generation algorithm using backtracking to find all
possible combinations of elements from a given array of a specified size. A combination is
a selection of elements where order does not matter. The algorithm explores all possible
combinations by recursively building subsets of the desired size, following the backtracking
pattern of making a choice, exploring its consequences, and then undoing the choice.

Combinations Algorithm Overview:
    Combinations are fundamental in combinatorics and have numerous applications including:
    - Cryptography (generating keys)
    - Resource allocation
    - Game theory
    - Data mining and pattern recognition
    - Machine learning feature selection
    - Statistical sampling
    - Genetic algorithms
    - Network design and optimization

Backtracking Algorithm Steps:
    The algorithm uses backtracking to systematically explore all possible combinations:
    1. Initialize an empty list to store results and an empty list to track the current combination
    2. Start the recursive process with the given array, target combination size, and starting index 0
    3. In the recursive function:
       a. If the current combination size equals the target size:
          - Add a copy of the current combination to the results
          - Return (base case: combination is complete)
       b. For each index from the current starting point to the end of the array:
          - Add the element at that index to the current combination
          - Recursively call the function with:
            * The array, target size - 1, and next index (i + 1)
            * The current combination with the new element
            * The results list
          - Remove (backtrack) the last element from the current combination
          - This allows exploring other combinations without affecting previous choices

Input:
    arr: A list of integers representing the source elements from which combinations will be generated
    size: An integer representing the desired size (length) of each combination

Output:
    Returns a list of all possible combinations, where each combination is represented as a list
    of integers. The combinations are returned in lexicographic order based on the input array's order.

Example:
    >>> arr = [1, 2, 3]
    >>> generate_combinations(arr, 2)
    [[1, 2], [1, 3], [2, 3]]

    >>> arr = [1, 2, 3]
    >>> generate_combinations(arr, 3)
    [[1, 2, 3]]

    >>> arr = [1, 2, 3, 4]
    >>> generate_combinations(arr, 2)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

    >>> arr = [1, 2, 3]
    >>> generate_combinations(arr, 1)
    [[1], [2], [3]]

    Step-by-step example for generate_combinations([1, 2, 3], 2):
    1. Initialize results = [], curr_combo = []
    2. Call generate_combinations_recursive([1, 2, 3], 2, 0, [], results)
    3. size = 2, start_index = 0, curr = [], results = []
    4. Loop i from 0 to 2 (len(arr) - 1)
    5. First iteration: i = 0
       - curr.add(1) → curr = [1]
       - Call generate_combinations_recursive([1, 2, 3], 1, 1, [1], results)
          - size = 1, start_index = 1, curr = [1], results = []
          - Loop i from 1 to 2
          - First iteration: i = 1
             - curr.add(2) → curr = [1, 2]
             - Call generate_combinations_recursive([1, 2, 3], 0, 2, [1, 2], results)
                - size = 0 → base case reached
                - results.add([1, 2]) → results = [[1, 2]]
                - return
             - curr.pop() → curr = [1]
          - Second iteration: i = 2
             - curr.add(3) → curr = [1, 3]
             - Call generate_combinations_recursive([1, 2, 3], 0, 3, [1, 3], results)
                - size = 0 → base case reached
                - results.add([1, 3]) → results = [[1, 2], [1, 3]]
                - return
             - curr.pop() → curr = [1]
       - curr.pop() → curr = []
    6. Second iteration: i = 1
       - curr.add(2) → curr = [2]
       - Call generate_combinations_recursive([1, 2, 3], 1, 2, [2], results)
          - size = 1, start_index = 2, curr = [2], results = [[1, 2], [1, 3]]
          - Loop i from 2 to 2
          - First iteration: i = 2
             - curr.add(3) → curr = [2, 3]
             - Call generate_combinations_recursive([1, 2, 3], 0, 3, [2, 3], results)
                - size = 0 → base case reached
                - results.add([2, 3]) → results = [[1, 2], [1, 3], [2, 3]]
                - return
             - curr.pop() → curr = [2]
       - curr.pop() → curr = []
    7. Third iteration: i = 2
       - curr.add(3) → curr = [3]
       - Call generate_combinations_recursive([1, 2, 3], 1, 3, [3], results)
          - size = 1, start_index = 3, curr = [3], results = [[1, 2], [1, 3], [2, 3]]
          - Loop from 3 to 2 (empty range) → no iterations
       - curr.pop() → curr = []
    8. Return results = [[1, 2], [1, 3], [2, 3]]

Complexity Analysis:
    Time Complexity: O(C(n, k) * k)
    - C(n, k) = n! / (k! * (n-k)!) = number of combinations of n elements taken k at a time
    - The algorithm generates exactly C(n, k) combinations
    - Each combination takes O(k) time to copy and add to results
    - Space Complexity: O(k) for the current combination
    - O(C(n, k) * k) for storing all combinations in results

    Space Complexity:
    - O(k) for the current combination being built
    - O(C(n, k) * k) for the results list containing all combinations
    - O(log n) for recursion stack depth (in the worst case)
    - Total space complexity is dominated by the results list

    Note:
    The space complexity is heavily dependent on k. For k = n, the space complexity
    is O(n), which is optimal. For k = n/2 (the worst case), the space complexity
    becomes O(C(n, n/2) * n/2), which can be enormous for large n.

Note:
    The algorithm has a bug on line 12 where `results.add()` is incorrectly used.
    It should be `results.append()` since results is a list, not a set.
    This causes a TypeError when trying to add a list to an integer object (if results
    started empty) or causes the method call to be ignored entirely if results
    was initialized as an empty list. For correct functionality, the fix should be:
    `results.append([i for i in curr])`. Also note that the combination generation
    produces combinations in lexicographic order based on the input array's order,
    making it suitable for generating combinatorial objects systematically.
"""

def generate_combinations(arr: list[int], size: int) -> list[int]:
    results = []
    curr_combo = []

    generate_combinations_recursive(arr, size, 0, curr_combo, results)

    return results


def generate_combinations_recursive(arr, size, start_index, curr, results) -> None:
    if size == 0:
        results.append([i for i in curr])
        return

    for i in range(start_index, len(arr)):
        curr.append(arr[i])
        generate_combinations_recursive(arr, size - 1, i + 1, curr, results)
        curr.pop()
