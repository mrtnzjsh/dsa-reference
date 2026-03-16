# Memoization & Bottom-Up Dynamic Programming Algorithm

## Overview

This module implements memoization (top-down dynamic programming) and bottom-up dynamic programming approaches for solving optimization problems. Memoization is a technique where we store the results of expensive function calls and return the cached result when the same inputs occur again. Bottom-up dynamic programming involves solving all subproblems starting from the smallest to the largest, filling a table progressively.

Both Approaches:
- Avoid redundant calculations
- Build solutions incrementally
- Break problems into smaller subproblems
- Exhibit optimal substructure
- Time Complexity: O(n) or O(n^2) or O(n^3) depending on the problem
- Space Complexity: O(n) or O(n^2) or O(n^3) for the cache/table

## Algorithm Steps

### Memoization (Top-Down) Implementation Steps:

1. Define a recursive function that solves the problem
2. Create a cache (dictionary or array) to store computed results
3. In the recursive function, first check if the result is in cache
4. If in cache, return the cached value
5. If not in cache, compute the result recursively and store it in cache
6. Return the computed result

### Bottom-Up (Iterative) Implementation Steps:

1. Create a table (array or 2D array) for storing intermediate results
2. Initialize the base cases (usually when input is 0 or 1)
3. Fill the table for increasing input sizes (iterative approach)
4. The solution is in the table at the target index
5. Backtrack if needed to reconstruct the actual solution

## Input

- `n`: Integer specifying the Fibonacci number to calculate
- `weights`: List of item weights
- `values`: List of item values
- `W`: Maximum knapsack capacity
- `coins`: List of available coin denominations
- `amount`: Target amount to make change for

## Output

Returns the solution using the specified approach (memoization or bottom-up):
- Fibonacci number: The nth Fibonacci number
- Knapsack: Maximum value achievable with the given capacity
- Coin Change: Minimum number of coins needed to make the exact amount

## Example

```python
>>> memoization_fibonacci(10)
55

>>> bottom_up_fibonacci(10)
55

>>> memoization_knapsack([2, 3, 4], [3, 4, 5], 5)
7

>>> bottom_up_knapsack([2, 3, 4], [3, 4, 5], 5)
7

>>> memoization_coin_change([1, 2, 5], 11)
3

>>> bottom_up_coin_change([1, 2, 5], 11)
3
```

### Step-by-step example for memoization_fibonacci(10):

1. Call memoization_fibonacci(10)
2. Check cache[10] → not in cache
3. Compute: memoization_fibonacci(10) = memoization_fibonacci(9) + memoization_fibonacci(8)
4. Check cache[9] → not in cache
5. Compute: memoization_fibonacci(9) = memoization_fibonacci(8) + memoization_fibonacci(7)
6. Check cache[8] → not in cache
7. Compute: memoization_fibonacci(8) = memoization_fibonacci(7) + memoization_fibonacci(6)
8. Continue recursively...
9. Eventually reach base cases: memoization_fibonacci(0) = 0, memoization_fibonacci(1) = 1
10. Cache now contains: {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}
11. Return 55

### Step-by-step example for bottom_up_fibonacci(10):

1. Create array dp of size 11
2. Initialize base cases: dp\[0\] = 0, dp\[1\] = 1
3. Fill the array iteratively:
   - dp\[2\] = dp\[1\] + dp\[0\] = 1 + 0 = 1
   - dp\[3\] = dp\[2\] + dp\[1\] = 1 + 1 = 2
   - dp\[4\] = dp\[3\] + dp\[2\] = 2 + 1 = 3
   - dp\[5\] = dp\[4\] + dp\[3\] = 3 + 2 = 5
   - dp\[6\] = dp\[5\] + dp\[4\] = 5 + 3 = 8
   - dp\[7\] = dp\[6\] + dp\[5\] = 8 + 5 = 13
   - dp\[8\] = dp\[7\] + dp\[6\] = 13 + 8 = 21
   - dp\[9\] = dp\[8\] + dp\[7\] = 21 + 13 = 34
   - dp\[10\] = dp\[9\] + dp\[8\] = 34 + 21 = 55
4. Return dp\[10\] = 55

### Step-by-step example for bottom_up_knapsack_01([2, 3, 4], [3, 4, 5], 5):

1. Create DP table of size (n+1) × (W+1) = 4 × 6
2. Initialize all values to 0
3. Fill the DP table row by row:
   - Row 1 (i=1, weight 2, value 3):
     - w=1: weight(2) > 1 → dp\[1\][1] = dp\[0\][1] = 0
     - w=2: weight(2) ≤ 2 → dp\[1\][2] = max(dp\[0\][2], 3 + dp\[0\][0]) = max(0, 3) = 3
     - w=3: weight(2) ≤ 3 → dp\[1\][3] = max(dp\[0\][3], 3 + dp\[0\][1]) = max(0, 3) = 3
     - w=4: weight(2) ≤ 4 → dp\[1\][4] = max(dp\[0\][4], 3 + dp\[0\][2]) = max(0, 3) = 3
     - w=5: weight(2) ≤ 5 → dp\[1\][5] = max(dp\[0\][5], 3 + dp\[0\][3]) = max(0, 3) = 3
   - Row 2 (i=2, weight 3, value 4):
     - w=1: weight(3) > 1 → dp\[2\][1] = dp\[1\][1] = 0
     - w=2: weight(3) > 2 → dp\[2\][2] = dp\[1\][2] = 3
     - w=3: weight(3) ≤ 3 → dp\[2\][3] = max(dp\[1\][3], 4 + dp\[1\][0]) = max(3, 4) = 4
     - w=4: weight(3) ≤ 4 → dp\[2\][4] = max(dp\[1\][4], 4 + dp\[1\][1]) = max(3, 4) = 4
     - w=5: weight(3) ≤ 5 → dp\[2\][5] = max(dp\[1\][5], 4 + dp\[1\][2]) = max(3, 7) = 7
   - Row 3 (i=3, weight 4, value 5):
     - w=1: weight(4) > 1 → dp\[3\][1] = dp\[2\][1] = 0
     - w=2: weight(4) > 2 → dp\[3\][2] = dp\[2\][2] = 3
     - w=3: weight(4) > 3 → dp\[3\][3] = dp\[2\][3] = 4
     - w=4: weight(4) ≤ 4 → dp\[3\][4] = max(dp\[2\][4], 5 + dp\[2\][0]) = max(4, 5) = 5
     - w=5: weight(4) ≤ 5 → dp\[3\][5] = max(dp\[2\][5], 5 + dp\[2\][1]) = max(7, 5) = 7
4. Return dp\[3\][5] = 7

### Step-by-step example for bottom_up_coin_change([1, 2, 5], 11):

1. Create array dp of size 12 (amount + 1)
2. Initialize all values to amount + 1 = 12: [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
3. Set dp\[0\] = 0: [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
4. Fill the array iteratively:
   - i=1: coin=1 → dp\[1\] = min(12, dp\[0\] + 1) = 1; coin=2 → dp\[1\] = min(1, 12+1) = 1; coin=5 → dp\[1\] = min(1, 12+1) = 1
   - i=2: coin=1 → dp\[2\] = min(12, dp\[1\] + 1) = 2; coin=2 → dp\[2\] = min(2, dp\[0\] + 1) = 1; coin=5 → dp\[2\] = min(1, 12+1) = 1
   - i=3: coin=1 → dp\[3\] = min(12, dp\[2\] + 1) = 2; coin=2 → dp\[3\] = min(2, dp\[1\] + 1) = 2; coin=5 → dp\[3\] = min(2, 12+1) = 2
   - i=4: coin=1 → dp\[4\] = min(12, dp\[3\] + 1) = 3; coin=2 → dp\[4\] = min(3, dp\[2\] + 1) = 2; coin=5 → dp\[4\] = min(2, 12+1) = 2
   - i=5: coin=1 → dp\[5\] = min(12, dp\[4\] + 1) = 3; coin=2 → dp\[5\] = min(3, dp\[3\] + 1) = 3; coin=5 → dp\[5\] = min(3, dp\[0\] + 1) = 1
   - i=6: coin=1 → dp\[6\] = min(12, dp\[5\] + 1) = 2; coin=2 → dp\[6\] = min(2, dp\[4\] + 1) = 3; coin=5 → dp\[6\] = min(2, dp\[1\] + 1) = 2
   - i=7: coin=1 → dp\[7\] = min(12, dp\[6\] + 1) = 3; coin=2 → dp\[7\] = min(3, dp\[5\] + 1) = 3; coin=5 → dp\[7\] = min(3, dp\[2\] + 1) = 2
   - i=8: coin=1 → dp\[8\] = min(12, dp\[7\] + 1) = 3; coin=2 → dp\[8\] = min(3, dp\[6\] + 1) = 3; coin=5 → dp\[8\] = min(3, dp\[3\] + 1) = 3
   - i=9: coin=1 → dp\[9\] = min(12, dp\[8\] + 1) = 4; coin=2 → dp\[9\] = min(4, dp\[7\] + 1) = 4; coin=5 → dp\[9\] = min(4, dp\[4\] + 1) = 3
   - i=10: coin=1 → dp\[10\] = min(12, dp\[9\] + 1) = 4; coin=2 → dp\[10\] = min(4, dp\[8\] + 1) = 4; coin=5 → dp\[10\] = min(4, dp\[5\] + 1) = 3
   - i=11: coin=1 → dp\[11\] = min(12, dp\[10\] + 1) = 5; coin=2 → dp\[11\] = min(5, dp\[9\] + 1) = 4; coin=5 → dp\[11\] = min(4, dp\[6\] + 1) = 3
5. Return dp\[11\] = 3

## Complexity Analysis

### Time Complexity: O(n) or O(n^2) or O(n^3) depending on the problem

- **Fibonacci**: O(n) for both approaches
- **Knapsack 0/1**: O(n × W) where n is the number of items and W is the capacity
- **Coin Change**: O(amount × num_coins) where amount is the target amount
- Both memoization and bottom-up achieve optimal time complexity by avoiding redundant calculations

### Space Complexity: O(n) or O(n × W)

- **Fibonacci**:
  - Memoization: O(n) for the recursion stack + O(n) for the cache = O(n)
  - Bottom-Up: O(n) for the DP array

- **Knapsack 0/1**:
  - Memoization: O(n × W) for the recursion stack + O(n × W) for the cache = O(n × W)
  - Bottom-Up: O(n × W) for the DP table

- **Coin Change**:
  - Memoization: O(amount × num_coins) for the recursion stack + O(amount × num_coins) for the cache = O(amount × num_coins)
  - Bottom-Up: O(amount) for the DP array

## Notes

Both memoization and bottom-up dynamic programming are powerful techniques for solving optimization problems. Memoization is often more intuitive for recursive solutions and is closer to the mathematical definition of dynamic programming. However, it uses implicit recursion and may cause stack overflow for very large inputs. Bottom-up is more efficient in terms of space (no recursion stack) and is generally preferred for problems with large inputs. The choice between the two approaches depends on the specific problem, input size, and implementation preferences. Both techniques avoid the exponential time complexity of the naive recursive approach, reducing it to polynomial time by exploiting the overlapping subproblems property of the problem.
