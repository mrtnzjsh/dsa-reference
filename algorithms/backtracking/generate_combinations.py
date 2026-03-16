"""Generate all possible combinations of elements from an array.

Args:
    arr: A list of integers representing the source elements
    size: The desired size (length) of each combination

Returns:
    A list of all possible combinations, where each combination is represented as a list of integers
"""


def generate_combinations(arr: list[str], size: int) -> list[list[str]]:
    results: list[list[str]] = []
    curr_combo: list[str] = []

    generate_combinations_recursive(arr, size, 0, curr_combo, results)

    return results


def generate_combinations_recursive(
    arr: list[str],
    size: int,
    start_index: int,
    curr: list[str],
    results: list[list[str]],
) -> None:
    if size == 0:
        results.append([i for i in curr])
        return

    for i in range(start_index, len(arr)):
        curr.append(arr[i])
        generate_combinations_recursive(arr, size - 1, i + 1, curr, results)
        _ = curr.pop()
