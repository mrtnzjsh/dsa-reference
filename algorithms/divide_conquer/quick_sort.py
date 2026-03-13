"""
Quick Sort Algorithm Implementation

This module implements the quick sort algorithm, which is a divide and conquer
sorting algorithm that selects a 'pivot' element from the array and partitions
the other elements into two subarrays according to whether they are less than
or greater than the pivot. The subarrays are then recursively sorted.

Algorithm Steps:
    1. Base Case: If the array has 0 or 1 elements, it is already sorted
    2. Initial Setup: Set low to 0 and high to n-1 if not provided
    3. Partitioning: Select a pivot element and partition the array
       a. Use the partition function to rearrange elements around the pivot
       b. Elements less than pivot go to the left, greater go to the right
       c. The partition function returns the final position of the pivot
    4. Recursive Sorting: Recursively sort the left and right subarrays
       a. Sort elements from low to pivot-1 (elements less than pivot)
       b. Sort elements from pivot+1 to high (elements greater than pivot)
    5. Completion: The array is sorted in-place when all recursive calls complete

Input:
    arr: The list of integers to be sorted (will be sorted in-place)
    low: The starting index of the segment to sort (default -1 means entire array)
    high: The ending index of the segment to sort (default -1 means entire array)

Output:
    The function sorts the array in-place and returns None

Example:
    >>> arr = [10, 7, 8, 9, 1, 5]
    >>> quick_sort(arr)
    >>> arr
    [1, 5, 7, 8, 9, 10]

    Step-by-step example for quick_sort([10, 7, 8, 9, 1, 5]):
    1. Initial: arr = [10, 7, 8, 9, 1, 5], low = 0, high = 5
       pivot = arr[5] = 5
       Partitioning:
       j = 0: arr[0] = 10 > 5, no swap, i stays -1
       j = 1: arr[1] = 7 > 5, no swap, i stays -1
       j = 2: arr[2] = 8 > 5, no swap, i stays -1
       j = 3: arr[3] = 9 > 5, no swap, i stays -1
       j = 4: arr[4] = 1 <= 5, swap arr[-1] and arr[4]
              arr = [1, 7, 8, 9, 10, 5], i = 0
       Final swap: arr[1], arr[5] = arr[5], arr[1]
       arr = [1, 5, 8, 9, 10, 7], pivot position = 1

    2. Left recursive call: quick_sort(arr, 0, 0)
       Base case: segment has 1 element, return

    3. Right recursive call: quick_sort(arr, 2, 5)
       pivot = arr[5] = 7
       Partitioning:
       j = 2: arr[2] = 8 > 7, no swap, i stays 1
       j = 3: arr[3] = 9 > 7, no swap, i stays 1
       j = 4: arr[4] = 10 > 7, no swap, i stays 1
       Final swap: arr[2], arr[5] = arr[5], arr[2]
       arr = [1, 5, 7, 9, 10, 8], pivot position = 2

    4. Left recursive call: quick_sort(arr, 2, 1)
       Base case: low > high, return

    5. Right recursive call: quick_sort(arr, 3, 5)
       pivot = arr[5] = 8
       Partitioning:
       j = 3: arr[3] = 9 > 8, no swap, i stays 2
       j = 4: arr[4] = 10 > 8, no swap, i stays 2
       Final swap: arr[3], arr[5] = arr[5], arr[3]
       arr = [1, 5, 7, 8, 10, 9], pivot position = 3

    6. Left recursive call: quick_sort(arr, 3, 2)
       Base case: low > high, return

    7. Right recursive call: quick_sort(arr, 4, 5)
       pivot = arr[5] = 9
       Partitioning:
       j = 4: arr[4] = 10 > 9, no swap, i stays 3
       Final swap: arr[4], arr[5] = arr[5], arr[4]
       arr = [1, 5, 7, 8, 9, 10], pivot position = 4

    8. Left recursive call: quick_sort(arr, 4, 3)
       Base case: low > high, return

    9. Right recursive call: quick_sort(arr, 5, 5)
       Base case: segment has 1 element, return

    Final result: [1, 5, 7, 8, 9, 10]

Complexity Analysis:
    Time Complexity: O(n log n) average, O(n²) worst case
    - Average case: The pivot selection divides the array roughly in half
      Each level of recursion processes n elements, and there are log(n) levels
    - Best case: Pivot always divides array into equal halves, same as average
    - Worst case: Pivot always divides into 0 and n-1 elements (already sorted)
      This creates a very unbalanced partition, leading to O(n²) complexity

    Space Complexity: O(log n) average, O(n) worst case
    - Recursion stack depth: O(log n) average, O(n) worst case
    - Each recursive call adds to the call stack
    - Best/Average case: Depth of recursion is log(n)
    - Worst case: Depth of recursion is n (for sorted array)

    Note: The worst case performance is avoided by:
    - Random pivot selection
    - Median-of-three pivot selection
    - Using other partitioning strategies (like introsort)
"""

def quick_sort(arr: list[int], low: int = -1, high: int = -1) -> None:
    n = len(arr)
    if n <= 1:
        return

    if low == -1:
        low = 0
    if high == -1:
        high = n - 1

    if low < high:
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def partition(arr: list[int], low: int, high: int) -> int:
    """
    Partition the Array Around a Pivot

    This helper function implements the Lomuto partition scheme to rearrange
    elements around a selected pivot. All elements less than or equal to the
    pivot are moved to the left side, and all elements greater than the pivot
    are moved to the right side. The pivot is placed in its correct final position.

    Algorithm Steps:
        1. Select the pivot element (arr[high] in this implementation)
        2. Initialize index i to track the position for elements <= pivot
        3. Iterate through the array from low to high-1:
           a. If current element <= pivot, increment i and swap it with arr[i]
              This moves smaller elements to the left side
        4. Finally, place the pivot in its correct position by swapping it with arr[i+1]
        5. Return the final position of the pivot

    Input:
        arr: The array to be partitioned
        low: The starting index of the segment to partition
        high: The ending index of the segment to partition (pivot position)

    Output:
    Returns the final index of the pivot element after partitioning

    Note:
        This is the Lomuto partition scheme which uses the last element as pivot.
        It is simpler to implement than the Hoare partition scheme but performs
        worse with duplicate elements. The array is modified in-place.

    Complexity Analysis:
        Time Complexity: O(n) where n = high - low + 1
        - Single pass through the array
        - Each element is compared exactly once
        - Space Complexity: O(1)
        - Only uses a constant number of extra variables (i, j)
        - No additional arrays are created
    """

    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1
