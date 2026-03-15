# Generate Permutations Recursive Algorithm

## Overview

This module implements the permutation generation algorithm using backtracking to find all possible arrangements (orderings) of elements from a given array. A permutation is a rearrangement of the elements, and for an array of n distinct elements, there are n! (n factorial) possible permutations. The algorithm uses the swapping method with backtracking to systematically generate all permutations by exploring different orderings.

Permutations Algorithm Overview:
    Permutations are fundamental in mathematics and have numerous applications including:
    - Solving puzzles (e.g., Rubik's Cube, Sudoku)
    - Cryptography (generating keys)
    - Optimizing schedules and routes
    - Statistical analysis (derangements, permutations)
    - Game theory (strategy generation)
    - Machine learning (feature permutations)
    - Combinatorial optimization
    - Molecular chemistry (isomer identification)

## Algorithm Steps

1. In the recursive function:
    a. If the current index (start_idx) equals the length of the array:
        - The current arrangement is complete
        - Add a copy of the array to the results
        - Return (base case: permutation is complete)
    b. For each index from start_idx to the end of the array:
        - Swap the element at start_idx with the element at the current index
        - This creates a new permutation by placing the element at index 'i' at position start_idx
        - Recursively call the function with start_idx + 1 to process the next position
        - Swap back (backtrack) the elements to restore the original arrangement
        - This allows exploring other permutations without permanently changing the array

2. The wrapper function:
    a. Create a copy of the input array (to avoid modifying the original)
    b. Initialize an empty results list
    c. If the array is empty, return an empty list
    d. Call the recursive function with start_idx = 0
    e. Return the results list containing all permutations

## Input

arr: A list of strings representing the elements for which permutations will be generated

## Output

Returns a list of all possible permutations, where each permutation is represented as a list of strings. The permutations are returned in lexicographic order based on the input array's order. If the input array is empty, returns an empty list.

## Example

```python
>>> arr = ["a", "b", "c"]
>>> generate_permutations(arr)
[['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']]

>>> arr = ["a"]
>>> generate_permutations(arr)
[['a']]

>>> arr = ["a", "b"]
>>> generate_permutations(arr)
[['a', 'b'], ['b', 'a']]

>>> arr = ["a", "a", "b"]
>>> generate_permutations(arr)
[['a', 'a', 'b'], ['a', 'b', 'a'], ['a', 'a', 'b'], ['a', 'b', 'a'], ['b', 'a', 'a'], ['b', 'a', 'a']]
```

### Step-by-step example for generate_permutations(["a", "b", "c"])

1. Call generate_permutations_recursively(["a", "b", "c"], 0, [])
2. start_idx = 0, arr = ["a", "b", "c"]
3. Loop idx from 0 to 2
4. First iteration: idx = 0
   - Swap arr[0] and arr[0] (no change)
   - arr = ["a", "b", "c"]
   - Recursively call generate_permutations_recursively(["a", "b", "c"], 1, [])
      - start_idx = 1, arr = ["a", "b", "c"]
      - Loop idx from 1 to 2
      - First iteration: idx = 1
         - Swap arr[1] and arr[1] (no change)
         - arr = ["a", "b", "c"]
         - Recursively call generate_permutations_recursively(["a", "b", "c"], 2, [])
            - start_idx = 2, arr = ["a", "b", "c"]
            - Loop idx from 2 to 2
            - First iteration: idx = 2
               - Swap arr[2] and arr[2] (no change)
               - arr = ["a", "b", "c"]
               - Recursively call generate_permutations_recursively(["a", "b", "c"], 3, [])
                  - start_idx = 3 == len(arr) → base case
                  - results.append(["a", "b", "c"])
                  - Return
         - Swap arr[2] and arr[2] (no change)
      - Return
   - Second iteration: idx = 2
      - Swap arr[1] and arr[2]
      - arr = ["a", "c", "b"]
      - Recursively call generate_permutations_recursively(["a", "c", "b"], 2, [])
         - start_idx = 2, arr = ["a", "c", "b"]
         - Loop idx from 2 to 2
         - First iteration: idx = 2
            - Swap arr[2] and arr[2] (no change)
            - arr = ["a", "c", "b"]
            - Recursively call generate_permutations_recursively(["a", "c", "b"], 3, [])
               - start_idx = 3 == len(arr) → base case
               - results.append(["a", "c", "b"])
               - Return
         - Swap arr[2] and arr[2] (no change)
      - Swap arr[1] and arr[2] → arr = ["a", "b", "c"]
   - Return
- Swap arr[0] and arr[0] (no change)
5. Second iteration: idx = 1
   - Swap arr[0] and arr[1]
   - arr = ["b", "a", "c"]
   - Recursively call generate_permutations_recursively(["b", "a", "c"], 1, [])
      - start_idx = 1, arr = ["b", "a", "c"]
      - Loop idx from 1 to 2
      - First iteration: idx = 1
         - Swap arr[1] and arr[1] (no change)
         - arr = ["b", "a", "c"]
         - Recursively call generate_permutations_recursively(["b", "a", "c"], 2, [])
            - start_idx = 2, arr = ["b", "a", "c"]
            - Loop idx from 2 to 2
            - First iteration: idx = 2
               - Swap arr[2] and arr[2] (no change)
               - arr = ["b", "a", "c"]
               - Recursively call generate_permutations_recursively(["b", "a", "c"], 3, [])
                  - start_idx = 3 == len(arr) → base case
                  - results.append(["b", "a", "c"])
                  - Return
         - Swap arr[2] and arr[2] (no change)
      - Return
   - Second iteration: idx = 2
      - Swap arr[1] and arr[2]
      - arr = ["b", "c", "a"]
      - Recursively call generate_permutations_recursively(["b", "c", "a"], 2, [])
         - start_idx = 2, arr = ["b", "c", "a"]
         - Loop idx from 2 to 2
         - First iteration: idx = 2
            - Swap arr[2] and arr[2] (no change)
            - arr = ["b", "c", "a"]
            - Recursively call generate_permutations_recursively(["b", "c", "a"], 3, [])
               - start_idx = 3 == len(arr) → base case
               - results.append(["b", "c", "a"])
               - Return
         - Swap arr[2] and arr[2] (no change)
      - Swap arr[1] and arr[2] → arr = ["b", "a", "c"]
   - Return
- Swap arr[0] and arr[1] → arr = ["a", "b", "c"]
6. Third iteration: idx = 2
   - Swap arr[0] and arr[2]
   - arr = ["c", "b", "a"]
   - Recursively call generate_permutations_recursively(["c", "b", "a"], 1, [])
      - start_idx = 1, arr = ["c", "b", "a"]
      - Loop idx from 1 to 2
      - First iteration: idx = 1
         - Swap arr[1] and arr[1] (no change)
         - arr = ["c", "b", "a"]
         - Recursively call generate_permutations_recursively(["c", "b", "a"], 2, [])
            - start_idx = 2, arr = ["c", "b", "a"]
            - Loop idx from 2 to 2
            - First iteration: idx = 2
               - Swap arr[2] and arr[2] (no change)
               - arr = ["c", "b", "a"]
               - Recursively call generate_permutations_recursively(["c", "b", "a"], 3, [])
                  - start_idx = 3 == len(arr) → base case
                  - results.append(["c", "b", "a"])
                  - Return
         - Swap arr[2] and arr[2] (no change)
      - Return
   - Second iteration: idx = 2
      - Swap arr[1] and arr[2]
      - arr = ["c", "a", "b"]
      - Recursively call generate_permutations_recursively(["c", "a", "b"], 2, [])
         - start_idx = 2, arr = ["c", "a", "b"]
         - Loop idx from 2 to 2
         - First iteration: idx = 2
            - Swap arr[2] and arr[2] (no change)
            - arr = ["c", "a", "b"]
            - Recursively call generate_permutations_recursively(["c", "a", "b"], 3, [])
               - start_idx = 3 == len(arr) → base case
               - results.append(["c", "a", "b"])
               - Return
         - Swap arr[2] and arr[2] (no change)
      - Swap arr[1] and arr[2] → arr = ["c", "b", "a"]
   - Return
- Swap arr[0] and arr[2] → arr = ["a", "b", "c"]
7. Return results = [["a", "b", "c"], ["a", "c", "b"], ["b", "a", "c"], ["b", "c", "a"], ["c", "b", "a"], ["c", "a", "b"]]

## Complexity Analysis

### Time Complexity: O(n!)

- For an array of n elements, there are n! possible permutations
- Each permutation takes O(n) time to copy and add to results
- Total time complexity: O(n! * n)

### Space Complexity: O(n * n!)

- O(n) for the recursion stack depth (in the worst case, it goes n levels deep)
- O(n! * n) for the results list containing all permutations
- O(n) for the temporary arrays used during permutations
- Total space complexity is dominated by the results list

## Notes

The algorithm generates all possible permutations, which grows extremely quickly with n.
For n = 10, there are 3,628,800 permutations; for n = 20, there are 2.4 * 10^18.
For large n, consider using optimized algorithms that generate permutations in a specific order (e.g., lexicographic) or use generators to avoid storing all permutations at once. The algorithm also has a bug when the input contains duplicate elements - it will generate duplicate permutations. For example, with input ["a", "a", "b"], it will generate each valid permutation twice because it doesn't track which elements have been used at each position.

Note:
The algorithm uses the swapping approach which modifies the input array directly.
The wrapper function creates a copy of the input array to avoid modifying the original.
This method is efficient in terms of space but has a disadvantage: it generates duplicate permutations when the input array contains duplicate elements. For input with duplicates, a more advanced algorithm using a visited array or set is recommended to avoid redundant permutations. The recursive implementation explores all possible orderings by systematically placing each element at each position, demonstrating the fundamental nature of permutation generation in combinatorics.
