# 0/1 Knapsack Algorithm

## Overview

The 0/1 Knapsack algorithm solves the classic optimization problem of selecting items to maximize total value without exceeding the knapsack's weight capacity. In this problem, each item can either be taken completely or left completely - partial usage is not allowed.

The algorithm uses dynamic programming to efficiently solve this NP-hard problem by breaking it down into smaller subproblems.

### Applications

- Resource allocation and portfolio optimization
- Budget allocation in project management
- Product selection for packaging and shipping
- Cryptography and code design
- Combinatorial optimization
- Network design and communication
- Machine learning and feature selection
- Operations research

### Problem Definition

**Given:**
- A set of n items, where each item has:
  - `weight[i]`: The weight of item i
  - `value[i]`: The value (profit) of item i
- A knapsack with a maximum weight capacity `W`

**Constraints:**
- Each item can be taken at most once (0 or 1)
- Total weight of selected items ≤ W

**Objective:**
- Maximize the total value of selected items

## Algorithm Steps

The algorithm uses a 2D DP table to store solutions to subproblems:

1. **Create DP table**: Create a 2D array `dp[n+1][W+1]` where:
   - `dp[i][w]` represents the maximum value achievable using the first i items with a knapsack capacity of w

2. **Initialize**: 
   - `dp[0][w] = 0` for all w (0 items → 0 value)
   - `dp[i][0] = 0` for all i (0 capacity → 0 value)

3. **Fill the DP table**:
   - For i from 1 to n:
   - For w from 1 to W:
     - If `weight[i-1] > w`: `dp[i][w] = dp[i-1][w]` (skip the item)
     - Else: `dp[i][w] = max(
         dp[i-1][w],                    // Don't take item i
         value[i-1] + dp[i-1][w - weight[i-1]]  // Take item i
       )`

4. **Result**: The answer is `dp[n][W]` - the maximum value achievable with all items

5. **Backtrack** to find which items were selected

## Input

- `weights`: A list of integers representing the weights of each item
- `values`: A list of integers representing the values of each item
- `W`: An integer representing the maximum weight capacity of the knapsack

## Output

Returns the maximum value achievable with the given capacity
Optionally returns the list of selected items (indices)

## Example

```python
>>> weights = [2, 3, 4, 5]
>>> values = [3, 4, 5, 6]
>>> W = 5
>>> knapsack_01(weights, values, W)
7

>>> weights = [1, 3, 4, 5]
>>> values = [1, 4, 5, 7]
>>> W = 7
>>> knapsack_01(weights, values, W)
9

>>> weights = [10, 20, 30]
>>> values = [60, 100, 120]
>>> W = 50
>>> knapsack_01(weights, values, W)
220
```

### Step-by-step Example

For `knapsack_01([2, 3, 4, 5], [3, 4, 5, 6], 5)`:

**Initial DP table**: Create dp[5][6] table where rows = items (0-4), cols = capacity (0-5)

**Initialize all cells: dp[0][w] = 0 for all w, dp[i][0] = 0 for all i

**Fill the table row by row**:

**Row 1 (Item 1: weight=2, value=3)**:
- w=1: weight(2) > 1 → dp[1][1] = dp[0][1] = 0
- w=2: weight(2) ≤ 2 → max(dp[0][2]=0, value(3)+dp[0][0]=3) = 3
- w=3: weight(2) ≤ 3 → max(dp[0][3]=0, value(3)+dp[0][1]=3) = 3
- w=4: weight(2) ≤ 4 → max(dp[0][4]=0, value(3)+dp[0][2]=3) = 3
- w=5: weight(2) ≤ 5 → max(dp[0][5]=0, value(3)+dp[0][3]=3) = 3

**Row 2 (Item 2: weight=3, value=4)**:
- w=1: weight(3) > 1 → dp[2][1] = dp[1][1] = 0
- w=2: weight(3) > 2 → dp[2][2] = dp[1][2] = 3
- w=3: weight(3) ≤ 3 → max(dp[1][3]=3, value(4)+dp[1][0]=4) = 4
- w=4: weight(3) ≤ 4 → max(dp[1][4]=3, value(4)+dp[1][1]=4) = 4
- w=5: weight(3) ≤ 5 → max(dp[1][5]=3, value(4)+dp[1][2]=7) = 7

**Row 3 (Item 3: weight=4, value=5)**:
- w=1: weight(4) > 1 → dp[3][1] = dp[2][1] = 0
- w=2: weight(4) > 2 → dp[3][2] = dp[2][2] = 3
- w=3: weight(4) > 3 → dp[3][3] = dp[2][3] = 4
- w=4: weight(4) ≤ 4 → max(dp[2][4]=4, value(5)+dp[2][0]=5) = 5
- w=5: weight(4) ≤ 5 → max(dp[2][5]=7, value(5)+dp[2][1]=5) = 7

**Row 4 (Item 4: weight=5, value=6)**:
- w=1: weight(5) > 1 → dp[4][1] = dp[3][1] = 0
- w=2: weight(5) > 2 → dp[4][2] = dp[3][2] = 3
- w=3: weight(5) > 3 → dp[4][3] = dp[3][3] = 4
- w=4: weight(5) > 4 → dp[4][4] = dp[3][4] = 5
- w=5: weight(5) ≤ 5 → max(dp[3][5]=7, value(6)+dp[3][0]=6) = 7

**Final result**: dp[4][5] = 7
The optimal solution is to select items 1 and 2:
- Item 1: weight=2, value=3
- Item 2: weight=3, value=4
- Total weight: 2 + 3 = 5, Total value: 3 + 4 = 7

## Complexity Analysis

### Time Complexity: O(n * W)
- n: Number of items
- W: Knapsack capacity
- We fill an (n+1) × (W+1) table, performing O(1) work per cell

### Space Complexity: O(n * W)
- The 2D DP table requires O(n * W) space
- Space can be optimized to O(W) using a 1D array (space optimization)

### Space Optimization
- We can optimize the space complexity from O(n * W) to O(W) by using a 1D DP array that we update iteratively
- The key insight is that dp[i][w] only depends on dp[i-1][w] and dp[i-1][w - weight[i-1]]
- By iterating w from W down to 0, we ensure we always use the previous iteration's value

## Notes

The 0/1 Knapsack problem is NP-hard, but the dynamic programming solution provides an efficient solution for cases where W is not too large. The space optimization technique can significantly reduce memory usage, especially when W is large but the solution is found early. The algorithm is essential for understanding dynamic programming, memoization, and the principle of optimal substructure. For very large capacities, consider using the branch and bound method or meet-in-the-middle algorithms. The 0/1 Knapsack problem also has applications in many real-world scenarios including resource allocation, budget management, and optimization problems in various industries.
