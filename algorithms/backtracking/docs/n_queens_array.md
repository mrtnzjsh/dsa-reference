"""N-Queens problem solved using array/backtracking approach.

Algorithm Overview:
- Uses a 2D board represented as list of strings
- Maintains three sets to track attacked positions:
  * cols: occupied column positions
  * diag1: diagonal attacks (row - col)
  * diag2: anti-diagonal attacks (row + col)
- Backtracking explores all valid queen placements row by row

Board Representation:
- '.' represents empty square
- 'Q' represents queen position
- Final results: list of board configurations with all solutions

Backtracking Process:
1. Start at first row (row 0)
2. For each row from 0 to n-1:
   - Try placing queen in each column (0 to n-1)
   - Check if column or diagonals are already attacked
   - If valid placement:
     * Mark position with 'Q'
     * Add column and diagonals to attack sets
     * Recurse to next row
     * Backtrack: remove queen and clear attack sets
   - If all columns tried and no solution, trigger backtracking

Attack Tracking:
- d1 = row - col: identifies diagonal direction (negative value)
- d2 = row + col: identifies anti-diagonal direction (positive value)
- Sets track unique diagonal values across entire board
- Each queen adds one unique value to each set (up to n values per set)

Time Complexity: O(n!)
- First row: n choices (all columns)
- Second row: at most n-1 valid positions (must avoid first queen)
- Third row: at most n-2 valid positions
- Continue until last row: at most 1 valid position
- Multiply: n × (n-1) × (n-2) × ... × 1 = n! combinations
- Each recursive call explores potential placements and builds solutions

Space Complexity: O(n²)
- Board storage: n × n characters
- Attack sets: O(n) each (each stores up to n unique diagonal values)
- Recursion stack: O(n) depth
- Results: O(n! × n²) for all solutions (not counted in space complexity)

Alternative Notes:
- More readable than bitwise approach
- Uses sets for clearer diagonal tracking
- Memory efficient for small n (n < 12)
- Trade-off: slightly slower due to set operations vs bitwise
"""
