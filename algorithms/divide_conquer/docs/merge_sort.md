"""Merge Sort Algorithm Implementation

This module implements the merge sort algorithm, which is a divide and conquer sorting
algorithm that recursively divides the input array into halves, sorts them, and then
merges the sorted halves back together. This implementation is stable and has
predictable performance characteristics.

Algorithm Steps:
    1. Divide Phase:
       a. Calculate the middle index of the array segment
       b. Recursively call merge_sort on the left half (from l to m)
       c. Recursively call merge_sort on the right half (from m+1 to r)
    2. Conquer Phase:
       a. Each recursive call reaches the base case where the segment has 1 element
       b. The function returns as the array is considered sorted
    3. Merge Phase:
       a. Create temporary arrays to hold left and right sorted halves
       b. Compare elements from both halves and merge them back into the original array
       c. Fill in the remaining elements from either half
       d. The merge operation uses the stable property (<= comparison)

Input:
    arr: The list of integers to be sorted (will be sorted in-place)
    l: The starting index of the segment to sort (default -1 means entire array)
    r: The ending index of the segment to sort (default -1 means entire array)

Output:
    The function sorts the array in-place and returns None

Example:
    >>> arr = [38, 27, 43, 3, 9, 82, 10]
    >>> merge_sort(arr)
    >>> arr
    [3, 9, 10, 27, 38, 43, 82]

    Step-by-step example for merge_sort([38, 27, 43, 3, 9, 82, 10]):
    1. Initial: arr = [38, 27, 43, 3, 9, 82, 10]
       l = 0, r = 6, m = 3
       Left: merge_sort([38, 27, 43, 3])
       Right: merge_sort([9, 82, 10])

    2. Left recursive call: arr = [38, 27, 43, 3]
       m = 1
       Left: merge_sort([38, 27])
       Right: merge_sort([43, 3])

    3. Left-Left recursive call: arr = [38, 27]
       m = 0
       Left: merge_sort([38])
       Right: merge_sort([27])
       Base cases return immediately (single elements are sorted)

    4. First merge: merge([38, 27], 0, 0, 1)
       left_arr = [38], right_arr = [27]
       Merge: [27, 38]

    5. Right-Left recursive call: arr = [43, 3]
       m = 0
       Left: merge_sort([43])
       Right: merge_sort([3])

    6. Second merge: merge([43, 3], 2, 2, 3)
       left_arr = [43], right_arr = [3]
       Merge: [3, 43]

    7. First merge of original: merge([27, 38, 3, 43], 0, 1, 3)
       left_arr = [27, 38], right_arr = [3, 43]
       Step 1: 27 <= 43, arr\[0\] = 27, i=1, j=0, k=1
       Step 2: 38 > 3, arr\[1\] = 3, i=1, j=1, k=2
       Step 3: 38 <= 43, arr\[2\] = 38, i=2, j=1, k=3
       Step 4: 38 > 3, arr\[3\] = 3, i=2, j=2, k=4
       Copy remaining: left_arr\[2\] = 43, arr\[4\] = 43
       Result: [3, 27, 38, 43, 9]

    8. Right recursive call: merge_sort([9, 82, 10])
       Similar recursive process results in [9, 10, 82]

    9. Final merge: merge([3, 27, 38, 43, 9, 10, 82], 0, 4, 6)
       left_arr = [3, 27, 38, 43], right_arr = [9, 10, 82]
       Merge all: [3, 9, 10, 27, 38, 43, 82]

Complexity Analysis:
    Time Complexity: O(n log n)
    - Each level of recursion processes all n elements
    - Number of levels: log(n) (dividing array into halves each time)
    - Total time: n × log(n)
    - Best case: O(n log n) (unlike quick sort which has O(n) best case)
    - Average case: O(n log n)
    - Worst case: O(n log n) (very stable performance)

    Space Complexity: O(n)
    - Temporary arrays used during merge: O(n) total
    - Recursion stack depth: O(log n)
    - Combined: O(n) for the merge arrays, which is the dominant factor

    Note: This implementation uses O(n) auxiliary space, which is the standard
    space complexity for merge sort implementations. Some optimized versions
    can use O(1) space but are more complex to implement.
"""
