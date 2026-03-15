# Coin Change Algorithm

## Overview

The Coin Change algorithm is a fundamental optimization problem that uses dynamic programming to solve the classic problem of making change for a given amount of money using the minimum number of coins. Unlike the 0/1 Knapsack problem, this problem aims to minimize the number of coins rather than maximize value, but it employs a similar DP approach.

## Problem Definition

Given:
- An array coins[] representing the denominations of available coins
- An integer amount representing the target amount to make change for

Constraints:
- You can use unlimited coins of each denomination
- You must make change for exactly the given amount (cannot use less)

Objective:
- Find the minimum number of coins needed to make the exact amount
- If it's not possible to make the exact amount, return -1

## Algorithm Steps

The algorithm uses a 1D DP array to store the minimum number of coins needed for each possible amount from 0 to the target amount:

1. Create a 1D array dp of size (amount + 1) where:
   - dp[i] represents the minimum number of coins needed to make amount i

2. Initialize dp[0] = 0 (0 coins needed to make amount 0)

3. Initialize all other dp[i] = amount + 1 (or infinity) for i > 0

4. Fill the DP array:
   For i from 1 to amount:
     For each coin in coins:
       If coin ≤ i:
         - dp[i] = min(dp[i], 1 + dp[i - coin])

5. The answer is dp[amount] - the minimum number of coins needed

6. If dp[amount] > amount, it's impossible to make change, return -1

## Input

- coins: A list of integers representing the available coin denominations
- amount: An integer representing the target amount to make change for

## Output

Returns the minimum number of coins needed to make the exact amount
If it's not possible, returns -1

## Example

```python
>>> coins = [1, 2, 5]
>>> coin_change(coins, 11)
3

>>> coins = [1, 3, 4]
>>> coin_change(coins, 6)
2

>>> coins = [2]
>>> coin_change(coins, 3)
-1

>>> coins = [1, 2, 5]
>>> coin_change(coins, 0)
0
```

## Step-by-Step Breakdown

Step-by-step example for coin_change([1, 2, 5], 11):
Create dp array of size 12 (indices 0-11)

Initialize: dp = [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
(amount + 1 = 12 represents "infinity")

Fill the DP array:

i=1:
- coin 1: 1 ≤ 1 → dp[1] = min(12, 1 + dp[0]) = min(12, 1) = 1
- coin 2: 2 > 1 → skip
- coin 5: 5 > 1 → skip
- dp[1] = 1

i=2:
- coin 1: 1 ≤ 2 → dp[2] = min(12, 1 + dp[1]) = min(12, 2) = 2
- coin 2: 2 ≤ 2 → dp[2] = min(2, 1 + dp[0]) = min(2, 1) = 1
- coin 5: 5 > 2 → skip
- dp[2] = 1

i=3:
- coin 1: 1 ≤ 3 → dp[3] = min(12, 1 + dp[2]) = min(12, 2) = 2
- coin 2: 2 ≤ 3 → dp[3] = min(2, 1 + dp[1]) = min(2, 2) = 2
- coin 5: 5 > 3 → skip
- dp[3] = 2

i=4:
- coin 1: 1 ≤ 4 → dp[4] = min(12, 1 + dp[3]) = min(12, 3) = 3
- coin 2: 2 ≤ 4 → dp[4] = min(3, 1 + dp[2]) = min(3, 2) = 2
- coin 5: 5 > 4 → skip
- dp[4] = 2

i=5:
- coin 1: 1 ≤ 5 → dp[5] = min(12, 1 + dp[4]) = min(12, 3) = 3
- coin 2: 2 ≤ 5 → dp[5] = min(3, 1 + dp[3]) = min(3, 3) = 3
- coin 5: 5 ≤ 5 → dp[5] = min(3, 1 + dp[0]) = min(3, 1) = 1
- dp[5] = 1

i=6:
- coin 1: 1 ≤ 6 → dp[6] = min(12, 1 + dp[5]) = min(12, 2) = 2
- coin 2: 2 ≤ 6 → dp[6] = min(2, 1 + dp[4]) = min(2, 3) = 2
- coin 5: 5 ≤ 6 → dp[6] = min(2, 1 + dp[1]) = min(2, 2) = 2
- dp[6] = 2

i=7:
- coin 1: 1 ≤ 7 → dp[7] = min(12, 1 + dp[6]) = min(12, 3) = 3
- coin 2: 2 ≤ 7 → dp[7] = min(3, 1 + dp[5]) = min(3, 2) = 2
- coin 5: 5 ≤ 7 → dp[7] = min(2, 1 + dp[2]) = min(2, 2) = 2
- dp[7] = 2

i=8:
- coin 1: 1 ≤ 8 → dp[8] = min(12, 1 + dp[7]) = min(12, 3) = 3
- coin 2: 2 ≤ 8 → dp[8] = min(3, 1 + dp[6]) = min(3, 3) = 3
- coin 5: 5 ≤ 8 → dp[8] = min(3, 1 + dp[3]) = min(3, 3) = 3
- dp[8] = 3

i=9:
- coin 1: 1 ≤ 9 → dp[9] = min(12, 1 + dp[8]) = min(12, 4) = 4
- coin 2: 2 ≤ 9 → dp[9] = min(4, 1 + dp[7]) = min(4, 3) = 3
- coin 5: 5 ≤ 9 → dp[9] = min(3, 1 + dp[4]) = min(3, 3) = 3
- dp[9] = 3

i=10:
- coin 1: 1 ≤ 10 → dp[10] = min(12, 1 + dp[9]) = min(12, 4) = 4
- coin 2: 2 ≤ 10 → dp[10] = min(4, 1 + dp[8]) = min(4, 4) = 4
- coin 5: 5 ≤ 10 → dp[10] = min(4, 1 + dp[5]) = min(4, 2) = 2
- dp[10] = 2

i=11:
- coin 1: 1 ≤ 11 → dp[11] = min(12, 1 + dp[10]) = min(12, 3) = 3
- coin 2: 2 ≤ 11 → dp[11] = min(3, 1 + dp[9]) = min(3, 4) = 3
- coin 5: 5 ≤ 11 → dp[11] = min(3, 1 + dp[6]) = min(3, 3) = 3
- dp[11] = 3

Final result: dp[11] = 3
The optimal solution is to use 2 coins of denomination 5 and 1 coin of denomination 1:
5 + 5 + 1 = 11, total coins = 3

## Complexity Analysis

### Time Complexity: O(amount × number_of_coins)
- amount: Target amount
- number_of_coins: Count of available coin denominations
- We iterate through all coins for each amount from 1 to amount

### Space Complexity: O(amount)
- The 1D DP array requires O(amount) space
- Can be further optimized to O(1) if we only need the minimum number of coins
- Total space complexity is O(amount)

## Notes

The Coin Change problem is a classic dynamic programming problem that demonstrates the principle of optimal substructure. The key insight is that the optimal solution for amount i can be built from the optimal solutions for smaller amounts (i - coin).

The algorithm is efficient for making change with a limited number of coin denominations, but the time complexity grows linearly with the target amount. For very large amounts, consider using the meet-in-the-middle algorithms or generating functions.

The Coin Change problem has numerous real-world applications including currency exchange, payment processing, and optimization problems in various industries. It's also related to the unbounded knapsack problem, which is a generalization of this problem.

## Additional Function

### coin_change_with_coins

Returns both the minimum number of coins and the specific coins used:

```python
>>> coin_change_with_coins([1, 2, 5], 11)
(3, [5, 5, 1])
```

This function uses a separate DP array to track which coin was used at each amount, allowing backtracking to find the exact combination of coins that yields the minimum count.