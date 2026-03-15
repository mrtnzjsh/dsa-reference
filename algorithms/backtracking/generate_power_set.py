def generate_power_set(arr: list[int]) -> list[int]:
    results = []
    curr_subset = []

    generate_power_set_recursive(arr, 0, curr_subset, results)

    return results


def generate_power_set_recursive(arr: list[int], start_idx: int, curr_subset: list[int], results: list[list[int]]) -> None:
    """
    Recursive helper function to generate power set using backtracking.

    Args:
        arr: The input array
        start_idx: The current starting index for exploration
        curr_subset: The current subset being built
        results: The list to store all subsets
    """
    # Add a copy of the current subset (this includes the empty set case)
    results.append(curr_subset.copy())

    # Base case: no more elements to explore
    if start_idx == len(arr):
        return

    # Explore all subsets that include arr[start_idx]
    for i in range(start_idx, len(arr)):
        curr_subset.append(arr[i])
        generate_power_set_recursive(arr, i + 1, curr_subset, results)
        curr_subset.pop()
