# Quick Sort Algorithm Implementation

# This module implements the quick sort algorithm, which is a divide and conquer
# sorting algorithm that selects a 'pivot' element from the array and partitions
# the other elements into two subarrays according to whether they are less than
# or greater than the pivot. The subarrays are then recursively sorted

# Algorithm Steps:
#     1. Base Case: If the array has 0 or 1 elements, it is already sorted
#     2. Initial Setup: Set low to 0 and high to n-1 if not provided
#     3. Partitioning: Select a pivot element and partition the array
#        a. Use the partition function to rearrange elements around the pivot
#        b. Elements less than pivot go to the left, greater go to the right
#        c. The partition function returns the final position of the pivot
#     4. Recursive Sorting: Recursively sort the left and right subarrays
#        a. Sort elements from low to pivot-1 (elements less than pivot)
#        b. Sort elements from pivot+1 to high (elements greater than pivot)
#     5. Completion: The array is sorted in-place when all recursive calls complete

# Input:
#     arr: The list of integers to be sorted (will be sorted in-place)
#     low: The starting index of the segment to sort (default -1 means entire array)
#     high: The ending index of the segment to sort (default -1 means entire array)

# Output:
#     The function sorts the array in-place and returns None

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
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1
