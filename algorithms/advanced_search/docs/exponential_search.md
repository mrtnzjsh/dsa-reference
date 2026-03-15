# Exponential Search Algorithm

## Overview

This module implements the exponential search algorithm, which efficiently finds a target element in a sorted array by exponentially increasing the search range. The algorithm combines the exponential technique with binary search to achieve optimal performance for sorted datasets where the target might be near the beginning or the end of the array.

## Algorithm Steps

1. Check if the target is equal to the first element (arr[0])
   - If yes, return 0 immediately

2. Start with i = 1 and check if arr[i] equals the target

3. While i < n and arr[i] <= target, double the index i (i *= 2)
   - This finds the range [low, high] where the target might be present

4. Set low = i // 2 (half of the last successful index)
   Set high = min(i, n - 1) (last valid index or the end of array)

5. Perform binary search within the range [low, high] to find the target

6. If found, return the index; otherwise return -1

## Input

- `arr`: A sorted list of integers
- `target`: The integer value to search for in the array

## Output

Returns the index of the target if found, otherwise returns -1

## Example

```python
>>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> exponential_search(arr, 5)
4
>>> exponential_search(arr, 1)
0
>>> exponential_search(arr, 9)
8
>>> exponential_search(arr, 10)
-1
```

### Step-by-step example for exponential_search(arr, 5):

1. Check arr[0] = 1 != target (5) → proceed
2. i = 1, arr[1] = 2 < target (5) → i = 2
3. i = 2, arr[2] = 3 < target (5) → i = 4
4. i = 4, arr[4] = 5 == target → return 4

### Step-by-step example for exponential_search(arr, 3):

1. Check arr[0] = 1 != target (3) → proceed
2. i = 1, arr[1] = 2 < target (3) → i = 2
3. i = 2, arr[2] = 3 == target → return 2

### Step-by-step example for exponential_search(arr, 10):

1. Check arr[0] = 1 != target (10) → proceed
2. i = 1, arr[1] = 2 < target (10) → i = 2
3. i = 2, arr[2] = 3 < target (10) → i = 4
4. i = 4, arr[4] = 5 < target (10) → i = 8
5. i = 8, arr[8] = 9 < target (10) → i = 16
6. i = 16 >= n = 9 → exit loop
7. low = 8 // 2 = 4, high = min(16, 8) = 8
8. Binary search in arr[4:8] for target (10)
9. Target not found → return -1

## Complexity Analysis

### Time Complexity: O(log n)

- Best case: O(1) when target is at the first position
- Average case: O(log n) when target is somewhere in the array
- Worst case: O(log n) when target is not present
- The exponential search finds the range [low, high] in O(log i) steps
- Binary search then finds the target in O(log n) steps
- Overall complexity is O(log n)

### Space Complexity: O(1)

- Only uses constant extra space for pointers and variables
- No recursion or additional data structures

## Notes

Exponential search is particularly useful for unbounded or very large arrays where the index of the target is not known in advance. It can also be used with infinite sorted sequences when the target is likely to be near the beginning. When the target is near the beginning, exponential search is more efficient than traditional binary search which always starts from the middle.
