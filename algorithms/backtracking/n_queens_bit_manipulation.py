"""
N-Queens problem solved using bitwise backtracking.

Algorithm Overview:
- Uses 4 integer variables to represent:
  * row: current row being processed (0 to n-1)
  * cols: column positions already occupied (bit i set means column i has a queen)
  * ld: left diagonals already attacked (bits set for all diagonals going left-down)
  * rd: right diagonals already attacked (bits set for all diagonals going right-down)

Bit Manipulation Explanation:
- available_positions: shows all safe squares for current row
  * (~(cols | ld | rd)): clear columns, left-diagonals, and right-diagonals bits
  * & ((1 << n) - 1): mask to keep only first n bits
- bit: extracts lowest set bit using two's complement
  * available_positions & -available_positions isolates the rightmost 1 bit
- available_positions -= bit: removes that bit from available positions

Backtracking Process:
1. For each row from 0 to n-1:
   - Calculate available_positions (squares not under attack)
   - While squares are available:
     * Choose a square by extracting its bit
     * Place queen (update cols, ld, rd with this position)
     * Recurse to next row
     * Remove queen (backtrack by undoing placements)
   - If no square available, trigger backtracking

Diagonal Tracking:
- ld (left diagonals) left-shifted after each row
- rd (right diagonals) right-shifted after each row
- | bit combines new position with existing diagonals
- Shifts simulate moving diagonally to next row

Time Complexity: O(n!)
- N-Queens explores all possible queen placements
- First row: n choices
- Second row: at most n-1 valid positions
- Third row: at most n-2 valid positions
- Continue until last row: at most 1 position
- Multiply all possibilities: n × (n-1) × (n-2) × ... × 1 = n!
- Backtracking prunes invalid paths, but worst case still explores factorial number of arrangements

Space Complexity: O(n) for recursion stack
"""

def n_queens(n: int) -> list[list[str]]:
    def backtrack(row, cols, ld, rd):
        if row == n:
            return True

        available_positions = (~(cols | ld | rd)) & ((1 << n) - 1)

        while available_positions:
            bit = available_positions & -available_positions

            backtrack(row + 1, cols | bit, (ld | bit) << 1, (rd | bit) >> 1)

            available_positions -= bit

    backtrack(0, 0, 0, 0)
    return []
