package main

import "sort"

func activity_selection(arr []int) []int {
	sort.Ints(arr)
	n := len(arr)

	result := make([]int, n)
	result[0] = arr[0]
	i := 0
	j := 1

	for j < n {
		if arr[j] > arr[i] {
			result[j] = arr[j]
			i = j
		}
		j += 1
	}

	return result
}

func main() {
	arr := []int{1, 6, 0, 7, 8}
	activity_selection(arr)
}
