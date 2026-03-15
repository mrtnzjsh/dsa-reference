

def exponential_search(arr: list[int], target: int) -> int:
    # Get the length of the array
    n = len(arr)

    # Check if target is at the first position
    if arr[0] == target:
        return 0

    # Exponentially increase the index until we find the range
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # Set the lower bound to half of the last successful index
    low = i // 2
    # Set the upper bound to the last valid index
    high = min(i, n - 1)

    # Perform binary search within the found range
    return binary_search(arr, target, low, high)
