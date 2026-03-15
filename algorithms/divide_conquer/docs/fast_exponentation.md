"""Fast Exponentiation Algorithm Implementation

This module implements the fast exponentiation (also known as exponentiation by squaring)
algorithm, which efficiently computes large powers by exploiting the mathematical property:
a^n = a^(n/2) * a^(n/2) if n is even, and a^n = a * a^(n/2) * a^(n/2) if n is odd.

This algorithm dramatically reduces the time complexity from O(n) for the naive approach
to O(log n) for the fast exponentiation method.

Algorithm Steps:
    1. Base Case: If the power is 0, return 1 (any number to the power of 0 is 1)
    2. Recursive Step: Calculate half_power = a^(power/2) recursively
    3. Even Power: If power is even, return half_power * half_power
    4. Odd Power: If power is odd, return base * half_power * half_power
       This accounts for the extra base factor when the power is odd

Input:
    base: The base number to be exponentiated (integer)
    power: The exponent to which the base is raised (non-negative integer)

Output:
    Returns base^power as an integer

Example:
    >>> fast_exponentation(2, 10)
    1024
    >>> fast_exponentation(3, 5)
    243
    >>> fast_exponentation(5, 0)
    1
    >>> fast_exponentation(10, 3)
    1000

    Step-by-step example for fast_exponentation(2, 10):
    2^10 = 2^5 * 2^5
        2^5 = 2 * 2^2 * 2^2
            2^2 = 2^1 * 2^1
                2^1 = 2 * 2^0
                    2^0 = 1 (base case)
                2^1 = 2 * 1 = 2
            2^2 = 2 * 2 = 4
        2^5 = 2 * 4 * 4 = 32
    2^10 = 32 * 32 = 1024

Complexity Analysis:
    Time Complexity: O(log n)
    - Each recursive call divides the power by 2 (or halves it)
    - Number of recursive calls: log₂(n) (binary representation of n)
    - Each call does constant work (multiplications)
    - Total operations: proportional to the number of bits in n

    Space Complexity: O(log n) for the recursion stack
    - Each recursive call adds a frame to the call stack
    - Maximum stack depth is log₂(n) (depth of recursion tree)
    - No additional space for storing intermediate results
    - Can be optimized to O(1) space using iterative approach

    Comparison:
    - Naive approach: O(n) multiplications
    - Fast exponentiation: O(log n) multiplications
    - For n = 1,000,000, naive needs 1,000,000 operations vs fast exponentiation needs ~20 operations
"""
