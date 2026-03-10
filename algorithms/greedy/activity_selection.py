"""
Activity Selection Algorithm

Step-by-step explanation:
1. Sort all activities by their finish times in ascending order
2. Initialize a result array of size n and select the first activity from the sorted list
3. Set two pointers: i for the last selected activity and j for the current activity
4. Iterate through the remaining activities starting from index 1
5. For each activity at index j, check if it starts after the last selected activity (at i) finishes
6. If the start time is greater than the finish time of activity i, select this activity
7. Move the i pointer to j to use this newly selected activity as the reference point
8. Move j pointer to the next activity and repeat step 5
9. Continue until all activities are processed
10. Return the array containing all selected activities

Time Complexity: O(n log n) for sorting activities, O(n) for selection loop
Space Complexity: O(n) for storing the result array
"""
from typing import Any

def activity_selection(arr: list[Any]) -> list[Any]:
    arr = sorted(arr)
    n = len(arr)

    result = [0] * n
    result[0] = arr[0]
    i, j = 0, 1

    while j < n:
        if arr[j] > arr[i]:
            result[j] = arr[j]
            k = j
        j += 1

    return result
