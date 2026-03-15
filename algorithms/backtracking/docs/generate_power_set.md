# Generate Power Set Algorithm

## Overview

This module implements the power set generation algorithm using backtracking to find all possible subsets (the power set) of a given array. The power set of a set S is the set of all possible subsets of S, including the empty set and S itself. For a set with n elements, the power set contains 2^n subsets. The algorithm uses the subset generation approach with backtracking to systematically build all possible combinations of elements.

## Algorithm Steps

1. Initialize an empty list to store results and an empty list to track the current subset
2. Start the recursive process with the given array and starting index 0
3. In the recursive function:
   a. Add a copy of the current subset to the results (include the empty subset case)
   b. If the current index is beyond the array length, return
   c. For each index from the current starting point to the end of the array:
      - Add the element at that index to the current subset
      - Recursively call the function with the next index to explore the subset with this element included
      - Remove (backtrack) the last element from the current subset
      - This allows exploring subsets without the current element for the next iteration
4. The wrapper function:
   a. Initialize an empty results list
   b. Call the recursive function with the array and starting index 0
   c. Return the results list containing all subsets

## Input

`arr`: A list of integers representing the elements for which the power set will be generated

## Output

Returns a list of all possible subsets, where each subset is represented as a list of integers. The subsets are returned in lexicographic order based on the input array's order. The power set always contains 2^n subsets, where n is the length of the input array. The empty set is included as the first subset.

## Example

```python
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
```

### Step-by-step example for generate_power_set([1, 2]):

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

## Complexity Analysis

### Time Complexity: O(n * 2^n)

- For an array of n elements, the power set contains 2^n subsets
- Each subset takes O(n) time to copy and add to results (worst case)
- Total time complexity: O(n * 2^n)

### Space Complexity: O(n * 2^n)

- O(n) for the current subset being built
- O(n * 2^n) for the results list containing all subsets
- O(n) for the recursion stack depth (in the worst case, it goes n levels deep)
- Total space complexity is dominated by the results list

## Notes

The space complexity grows exponentially with n, which makes this algorithm impractical for large n (e.g., n > 20). For n = 20, the power set has over 1 million subsets. For large n, consider using generators to avoid storing all subsets at once, or use iterative approaches that generate subsets one at a time.

The algorithm demonstrates the fundamental nature of backtracking for combinatorial generation problems. The key insight is that every subset can be represented as a path in a decision tree where at each element, we either include it or not include it in the current subset. The recursion explores all possible combinations of these binary decisions.

The power set is essential in many algorithms and data structures, including the set cover problem, bitmask representations, and various combinatorial optimization problems.
