"""
Merge Sort Algorithm Implementation

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
       Step 1: 27 <= 43, arr[0] = 27, i=1, j=0, k=1
       Step 2: 38 > 3, arr[1] = 3, i=1, j=1, k=2
       Step 3: 38 <= 43, arr[2] = 38, i=2, j=1, k=3
       Step 4: 38 > 3, arr[3] = 3, i=2, j=2, k=4
       Copy remaining: left_arr[2] = 43, arr[4] = 43
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

def merge_sort(arr: list[int], l: int = -1, r: int = -1) -> None:
    n = len(arr)
    if l == -1:
        l = 0
    if r == -1:
        r = n - 1

    if l < r:
        m = l + (r - l) // 2

        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)

        merge(arr, l, m, r)

def merge(arr: list[int], l: int, m: int, r: int) -> None:
    """
    Merge Two Sorted Subarrays

    This helper function merges two sorted subarrays [arr[l..m] and arr[m+1..r]
    back into a single sorted subarray arr[l..r].

    Algorithm Steps:
        1. Calculate the size of both subarrays
        2. Create temporary arrays to hold the elements from each subarray
        3. Copy the elements from the original array into the temporary arrays
        4. Merge the two sorted temporary arrays back into the original array
        5. Handle any remaining elements from either subarray

    Input:
        arr: The array containing the sorted subarrays to merge
        l: The starting index of the first subarray
        m: The middle index (end of first subarray)
        r: The ending index of the second subarray

    Output:
        Modifies the original array in-place by merging the sorted subarrays

    Note:
        The function uses a stable merge algorithm, preserving the relative order
        of equal elements from both subarrays.

    Complexity Analysis:
        Time Complexity: O(n) where n = r - l + 1
        - Each element is compared and placed exactly once
        Space Complexity: O(n) for the temporary arrays
        - Total space used: O(n1 + n2) = O(n) where n is the size of the merged segment
    """

    n1 = m - l + 1
    n2 = r - m

    left_arr = [0] * n1
    right_arr = [0] * n2

    for i in range(n1):
        left_arr[i] = arr[l + i]

    for j in range(n2):
        right_arr[j] = arr[m + 1 + j]

    i, j, k = 0, 0, l

    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

    
