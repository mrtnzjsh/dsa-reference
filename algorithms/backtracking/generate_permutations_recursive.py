def generate_permutations_recursively(arr, start_idx, result):
    if start_idx == len(arr):
        result.append([i for i in arr])
        return

    for idx in range(start_idx, len(arr)):
        arr[start_idx], arr[idx] = arr[idx], arr[start_idx]
        generate_permutations_recursively(arr, start_idx + 1, result)
        arr[start_idx], arr[idx] = arr[idx], arr[start_idx]


def generate_permutations(arr: list[str]) -> list[str]:
    result = []
    if not arr:
        return result

    arr_copy = list(arr)
    generate_permutations_recursively(arr_copy, 0, result)

    return result
