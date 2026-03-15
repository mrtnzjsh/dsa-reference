# Search in Rotated Sorted Array Algorithm

## Overview

This module implements the search algorithm for finding a target element in a rotated sorted array. A rotated sorted array is a sorted array that has been rotated at some pivot point, meaning the array has been shifted such that the elements are no longer in their original order, but still maintain a sorted property. The algorithm uses a modified binary search approach to efficiently locate the target in O(log n) time.

## Algorithm Steps

1. Initialize two pointers: low at the start (0) and high at the end (n-1) of the array

2. While low <= high:
   - a. Calculate the mid index as low + (high - low) // 2 (avoids potential integer overflow)
   - b. If the element at mid equals the target, return the mid index
   - c. Check which half of the array is properly sorted:
      - If arr[low] <= arr[mid]: This means the left half [low, mid] is properly sorted
        - If target lies within the sorted left half (arr[low] <= target < arr[mid]):
          Set high = mid - 1 to search the left half
        - Else:
          Set low = mid + 1 to search the right half
      - Else: This means the right half [mid, high] is properly sorted
        - If target lies within the sorted right half (arr[mid] < target <= arr[high]):
          Set low = mid + 1 to search the right half
        - Else:
          Set high = mid - 1 to search the left half

3. If the target is not found after the loop completes, return -1

## Input

- `arr`: A rotated sorted list of integers (a sorted array that has been rotated at some pivot)
- `target`: The integer value to search for in the array

## Output

Returns the index of the target if found, otherwise returns -1

## Example

```python
>>> arr = [4, 5, 6, 7, 0, 1, 2]
>>> search_rotated_array(arr, 0)
4
>>> search_rotated_array(arr, 3)
-1
>>> search_rotated_array(arr, 5)
1
>>> search_rotated_array(arr, 7)
3
```

### Step-by-step example for search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0):

1. Initial: arr = [4, 5, 6, 7, 0, 1, 2], target = 0
   low = 0, high = 6, mid = 3
   arr[3] = 7 != target (0)
   arr[low] = 4 <= arr[mid] = 7 → left half is sorted
   target (0) < arr[low] = 4 → not in left half, search right
   low = mid + 1 = 4

2. low = 4, high = 6, mid = 5
   arr[5] = 1 != target (0)
   arr[low] = 0 <= arr[mid] = 1 → left half is sorted
   target (0) == arr[low] = 0 → not in left half (need > arr[low])
   target (0) > arr[mid] = 1 → not in right half, search left
   high = mid - 1 = 4

3. low = 4, high = 4, mid = 4
   arr[4] = 0 == target → return 4

### Step-by-step example for search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3):

1. Initial: arr = [4, 5, 6, 7, 0, 1, 2], target = 3
   low = 0, high = 6, mid = 3
   arr[3] = 7 != target (3)
   arr[low] = 4 <= arr[mid] = 7 → left half is sorted
   target (3) < arr[low] = 4 → not in left half, search right
   low = mid + 1 = 4

2. low = 4, high = 6, mid = 5
   arr[5] = 1 != target (3)
   arr[low] = 0 <= arr[mid] = 1 → left half is sorted
   target (3) > arr[mid] = 1 → check right half
   arr[mid] = 1 < target (3) <= arr[high] = 2 → not in right half
   high = mid - 1 = 4

3. low = 4, high = 4, mid = 4
   arr[4] = 0 != target (3)
   arr[low] = 0 <= arr[mid] = 0 → left half is sorted
   target (3) > arr[mid] = 0 → check right half
   arr[mid] = 0 < target (3) <= arr[high] = 0 → not in right half
   high = mid - 1 = 3

4. low = 4, high = 3 → loop ends
   Target not found → return -1

### Step-by-step example for search_rotated_array([5, 1, 3], 5):

1. Initial: arr = [5, 1, 3], target = 5
   low = 0, high = 2, mid = 1
   arr[1] = 1 != target (5)
   arr[low] = 5 <= arr[mid] = 1 → This is False, so right half is sorted
   arr[mid] = 1 < target (5) <= arr[high] = 3 → not in right half
   high = mid - 1 = 0

2. low = 0, high = 0, mid = 0
   arr[0] = 5 == target → return 0

## Complexity Analysis

### Time Complexity: O(log n)

- Each iteration reduces the search space by half
- The algorithm identifies which half of the array is properly sorted
- Then it determines if the target lies in that sorted half
- If not, it searches the other half
- After at most log(n) iterations, the target is found or the search space is exhausted

### Space Complexity: O(1)

- Only uses constant extra space for low, high, and mid pointers
- No recursion or additional data structures

## Notes

This algorithm assumes the array contains distinct elements (no duplicates). With duplicates present, worst-case time complexity can degrade to O(n). The key insight is that at least one half of the array [low, mid] or [mid, high] will always be sorted in a rotated sorted array, allowing binary search to be used effectively without knowing the rotation point in advance.
