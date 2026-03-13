"""
Binary Search Algorithm Implementation

This module implements the binary search algorithm, which efficiently finds a target element
in a sorted array by repeatedly dividing the search interval in half. The algorithm follows
the divide and conquer approach, providing optimal performance for sorted datasets.

Algorithm Steps:
    1. Initialize two pointers: low at the start (0) and high at the end (n-1) of the array
    2. While low <= high:
       a. Calculate the mid index as the average of low and high
       b. If the element at mid equals the target, return the mid index
       c. If the target is greater than the element at mid, adjust low to mid + 1
       d. If the target is smaller than the element at mid, adjust high to mid - 1
    3. If the target is not found after the loop completes, return -1

Input:
    arr: A sorted list of integers
    target: The integer value to search for in the array

Output:
    Returns the index of the target if found, otherwise returns -1

Example:
    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> binary_search(arr, 5)
    4
    >>> binary_search(arr, 1)
    0
    >>> binary_search(arr, 9)
    8
    >>> binary_search(arr, 10)
    -1

    Step-by-step example for binary_search(arr, 5):
    1. Initial: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], target = 5
       low = 0, high = 8, mid = (0 + 8) // 2 = 4
       arr[4] = 5 == target → return 4

    Step-by-step example for binary_search(arr, 3):
    1. Initial: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], target = 3
       low = 0, high = 8, mid = 4
       arr[4] = 5 > target → high = 3
    2. low = 0, high = 3, mid = 1
       arr[1] = 2 < target → low = 2
    3. low = 2, high = 3, mid = 2
       arr[2] = 3 == target → return 2

Complexity Analysis:
    Time Complexity: O(log n)
    - Each iteration reduces the search space by half
    - Initial search space: n elements
    - After k iterations: n / (2^k) elements
    - When n / (2^k) = 1, k = log(n) iterations
    - Space Complexity: O(1)
    - Only uses constant extra space for pointers and variables
    - No recursion or additional data structures
"""

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
    """
    Binary Search in a 2D Matrix

    This function implements a binary search algorithm for finding a target element
    in a 2D sorted matrix. The matrix is assumed to be sorted in non-decreasing order
    both row-wise and column-wise. The algorithm uses a divide and conquer approach
    by starting from the bottom-left corner and moving based on the comparison.

    Algorithm Steps:
        1. Initialize row pointer at the last row (m-1) and column pointer at the first column (0)
        2. While row >= 0 and column < number of columns:
           a. If the current element equals the target, return its coordinates
           b. If the current element is less than the target, move right (column + 1)
              because all elements in this row to the left are also smaller
           c. If the current element is greater than the target, move up (row - 1)
              because all elements in this column below are also larger
        3. If the target is not found, return (-1, -1)

    Input:
        matrix: A 2D list of integers sorted in non-decreasing order row-wise and column-wise
        target: The integer value to search for in the matrix

    Output:
        Returns a tuple (row_index, column_index) if target is found, otherwise (-1, -1)

    Example:
        >>> matrix = [
        ...     [1, 3, 5, 7],
        ...     [10, 11, 16, 20],
        ...     [23, 30, 34, 50]
        ... ]
        >>> binary_search_matrix(matrix, 3)
        (0, 1)
        >>> binary_search_matrix(matrix, 13)
        (-1, -1)

        Step-by-step example for binary_search_matrix(matrix, 16):
        1. Initial: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
           target = 16, row = 2, col = 0
           matrix[2][0] = 23 > 16 → move up (row = 1)
        2. row = 1, col = 0, matrix[1][0] = 10 < 16 → move right (col = 1)
        3. row = 1, col = 1, matrix[1][1] = 11 < 16 → move right (col = 2)
        4. row = 1, col = 2, matrix[1][2] = 16 == target → return (1, 2)

    Complexity Analysis:
        Time Complexity: O(m + n)
        - Worst case scenario: You traverse one row and one column
        - Each step moves either up (row -= 1) or right (col += 1)
        - Maximum number of steps is bounded by (m + n - 1) because you can't move outside the matrix
        - Space Complexity: O(1)
        - Only uses constant extra space for row and column pointers
        - No recursion or additional data structures

    Note:
        This algorithm is more efficient than binary search on each row separately
        which would have O(m * n * log n) time complexity.
    """

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


