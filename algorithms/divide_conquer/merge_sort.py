# Merge Sort Algorithm Implementation

# This module implements the merge sort algorithm, which is a divide and conquer sorting
# algorithm that recursively divides the input array into halves, sorts them, and then
# merges the sorted halves back together

# Algorithm Steps:
#     1. Divide Phase:
#        a. Calculate the middle index of the array segment
#        b. Recursively call merge_sort on the left half (from l to m)
#        c. Recursively call merge_sort on the right half (from m+1 to r)
#     2. Conquer Phase:
#        a. Each recursive call reaches the base case where the segment has 1 element
#        b. The function returns as the array is considered sorted
#     3. Merge Phase:
#        a. Create temporary arrays to hold left and right sorted halves
#        b. Compare elements from both halves and merge them back into the original array
#        c. Fill in the remaining elements from either half
#        d. The merge operation uses the stable property (<= comparison)

# Input:
#     arr: The list of integers to be sorted (will be sorted in-place)
#     l: The starting index of the segment to sort (default -1 means entire array)
#     r: The ending index of the segment to sort (default -1 means entire array)

# Output:
#     The function sorts the array in-place and returns None

# Example:
#     >>> arr = [38, 27, 43, 3, 9, 82, 10]
#     >>> merge_sort(arr)
#     >>> arr
#     [3, 9, 10, 27, 38, 43, 82]

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
