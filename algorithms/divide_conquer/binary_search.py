# Binary Search Algorithm Implementation

# This module implements the binary search algorithm, which efficiently finds a target element
# in a sorted array by repeatedly dividing the search interval in half

# Algorithm Steps:
#     1. Initialize two pointers: low at the start (0) and high at the end (n-1) of the array
#     2. While low <= high:
#        a. Calculate the mid index as the average of low and high
#        b. If the element at mid equals the target, return the mid index
#        c. If the target is greater than the element at mid, adjust low to mid + 1
#        d. If the target is smaller than the element at mid, adjust high to mid - 1
#     3. If the target is not found after the loop completes, return -1

# Input:
#     arr: A sorted list of integers
#     target: The integer value to search for in the array

# Output:
#     Returns the index of the target if found, otherwise returns -1

# Example:
#     >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     >>> binary_search(arr, 5)
#     4
#     >>> binary_search(arr, 1)
#     0
#     >>> binary_search(arr, 9)
#     8
#     >>> binary_search(arr, 10)
#     -1

#     Step-by-step example for binary_search(arr, 5):
#     1. Initial: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], target = 5
#        low = 0, high = 8, mid = (0 + 8) // 2 = 4
#        arr[4] = 5 == target → return 4

#     Step-by-step example for binary_search(arr, 3):
#     1. Initial: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], target = 3
#        low = 0, high = 8, mid = 4
#        arr[4] = 5 > target → high = 3
#     2. low = 0, high = 3, mid = 1
#        arr[1] = 2 < target → low = 2
#     3. low = 2, high = 3, mid = 2
#        arr[2] = 3 == target → return 2

# Complexity Analysis:
#     Time Complexity: O(log n)
#     - Each iteration reduces the search space by half
#     - Initial search space: n elements
#     - After k iterations: n / (2^k) elements
#     - When n / (2^k) = 1, k = log(n) iterations
#     - Space Complexity: O(1)
#     - Only uses constant extra space for pointers and variables
#     - No recursion or additional data structures

def binary_search(arr: list[int], target: int) -> int:
    n = len(arr)
    l, r = 0, n - 1

    while l <= r:
        mid = (r - l) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1

def binary_search_matrix(matrix: list[list[int]], target: int) -> tuple[int, int]:
    m = len(matrix)
    n = len(matrix[0])

    r = m - 1
    c = 0

    while r >= 0 and c < n:
        if matrix[r][c] == target:
            return (r, c)
        if matrix[r][c] < target:
            c += 1
        else:
            r -= 1

    return (-1, -1)
