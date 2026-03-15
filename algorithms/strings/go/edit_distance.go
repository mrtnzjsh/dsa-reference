package main

import (
	"fmt"
)

type EditOps struct {
	Distance int
	Ops      []Operation
}

type Operation struct {
	Type  string
	Index int
	Char  string
}

func min(a, b, c int) int {
	if a < b {
		if a < c {
			return a
		}
		return c
	}
	if b < c {
		return b
	}
	return c
}

func edit_distance(s string, t string) int {
	m := len(s)
	n := len(t)

	dp := make([][]int, m+1)
	for i := range m {
		dp[i] = make([]int, n+1)
	}

	for i := 0; i <= m; i++ {
		dp[i][0] = i
	}
	for j := 0; j <= n; j++ {
		dp[0][j] = j
	}

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			substitution_cost := 0
			if s[i-1] == t[j-1] {
				substitution_cost = 0
			} else {
				substitution_cost = 1
			}

			dp[i][j] = min(
				dp[i-1][j]+1,
				dp[i][j-1]+1,
				dp[i-1][j-1]+substitution_cost,
			)
		}
	}

	return dp[m][n]
}

func edit_distance_optimized(s string, t string) int {
	if len(s) < len(t) {
		s, t = t, s
	}

	previous_row := make([]int, len(t)+1)
	for i := 0; i <= len(t); i++ {
		previous_row[i] = i
	}

	for i := 1; i <= len(s); i++ {
		current_row := []int{i}

		for j := 1; j <= len(t); j++ {
			substitution_cost := 0
			if s[i-1] == t[j-1] {
				substitution_cost = 0
			} else {
				substitution_cost = 1
			}

			current_row = append(
				current_row,
				min(previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]+substitution_cost),
			)
		}
		previous_row = current_row
	}
	return previous_row[len(t)]
}

func edit_distance_with_operations(s string, t string) EditOps {
	m := len(s)
	n := len(t)
	dp := make([][]int, m+1)
	for i := 0; i <= m; i++ {
		dp[i] = make([]int, n+1)
	}

	for i := 0; i <= m; i++ {
		dp[i][0] = i
	}
	for j := 0; j <= n; j++ {
		dp[0][j] = j
	}

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			substitution_cost := 0
			if s[i-1] == t[j-1] {
				substitution_cost = 0
			} else {
				substitution_cost = 1
			}

			dp[i][j] = min(
				dp[i-1][j]+1,
				dp[i][j-1]+1,
				dp[i-1][j-1]+substitution_cost,
			)
		}
	}
	distance := dp[m][n]

	operations := []Operation{}
	i := m
	j := n

	for i > 0 && j > 0 {
		if i > 0 && j > 0 && s[i-1] == t[j-1] {
			i--
			j--
		} else if j > 0 && dp[i][j] == dp[i][j-1]+1 {
			operations = append(operations, Operation{Type: "insert", Index: i, Char: string([]rune(t)[j-1])})
			j--
		} else if i > 0 && dp[i][j] == dp[i-1][j]+1 {
			operations = append(operations, Operation{Type: "delete", Index: i, Char: string([]rune(s)[i-1])})
			i--
		} else {
			operations = append(operations, Operation{Type: "substitute", Index: i, Char: string([]rune(t)[j-1])})
			i--
			j--
		}
	}

	for k := len(operations)/2 - 1; k >= 0; k-- {
		opp := operations[k]
		operations[k] = operations[len(operations)-1-k]
		operations[len(operations)-1-k] = opp
	}
	return EditOps{Distance: distance, Ops: operations}
}

func main() {
	fmt.Println("edit distance algorithm.")
}
