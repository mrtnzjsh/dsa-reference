"""
Fast Exponentiation Algorithm Implementation

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

    Step-by-step execution for fast_exponentation(2, 10):
    1. fast_exponentation(2, 10):
       power = 10, not 0
       half_power = fast_exponentation(2, 5)
       10 is even → return half_power * half_power
    2. fast_exponentation(2, 5):
       power = 5, not 0
       half_power = fast_exponentation(2, 2)
       5 is odd → return 2 * half_power * half_power
    3. fast_exponentation(2, 2):
       power = 2, not 0
       half_power = fast_exponentation(2, 1)
       2 is even → return half_power * half_power
    4. fast_exponentation(2, 1):
       power = 1, not 0
       half_power = fast_exponentation(2, 0)
       1 is odd → return 2 * half_power * half_power
    5. fast_exponentation(2, 0):
       power = 0 (base case)
       return 1
    6. Back to step 4: fast_exponentation(2, 1)
       half_power = 1
       return 2 * 1 * 1 = 2
    7. Back to step 3: fast_exponentation(2, 2)
       half_power = 2
       return 2 * 2 = 4
    8. Back to step 2: fast_exponentation(2, 5)
       half_power = 4
       return 2 * 4 * 4 = 32
    9. Back to step 1: fast_exponentation(2, 10)
       half_power = 32
       return 32 * 32 = 1024

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
def fast_exponentation_recursive(base, power) -> int:
    """
    Fast Exponentiation - Recursive Implementation

    This function implements a recursive version of fast exponentiation (also known as
    exponentiation by squaring), which efficiently computes large powers by exploiting
    the mathematical property: a^n = a^(n/2) * a^(n/2) if n is even, and a^n = a * a^(n/2) * a^(n/2) if n is odd.

    The algorithm breaks the exponentiation problem into smaller subproblems, solving
    them recursively, and then combines the results.

    Algorithm Steps:
        1. Base Case: If power is 0, return 1 (any number to the power of 0 is 1)
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
        >>> fast_exponentation_recursive(2, 10)
        1024
        >>> fast_exponentation_recursive(3, 5)
        243
        >>> fast_exponentation_recursive(5, 0)
        1
        >>> fast_exponentation_recursive(10, 3)
        1000

        Step-by-step example for fast_exponentation_recursive(2, 10):
        2^10 = 2^5 * 2^5
            2^5 = 2 * 2^2 * 2^2
                2^2 = 2^1 * 2^1
                    2^1 = 2 * 2^0
                        2^0 = 1 (base case)
                    2^1 = 2 * 1 = 2
                2^2 = 2 * 2 = 4
            2^5 = 2 * 4 * 4 = 32
        2^10 = 32 * 32 = 1024

        Step-by-step execution for fast_exponentation_recursive(2, 10):
        1. fast_exponentation_recursive(2, 10):
           power = 10, not 0
           half_power = fast_exponentation_recursive(2, 5)
           10 is even → return half_power * half_power
        2. fast_exponentation_recursive(2, 5):
           power = 5, not 0
           half_power = fast_exponentation_recursive(2, 2)
           5 is odd → return 2 * half_power * half_power
        3. fast_exponentation_recursive(2, 2):
           power = 2, not 0
           half_power = fast_exponentation_recursive(2, 1)
           2 is even → return half_power * half_power
        4. fast_exponentation_recursive(2, 1):
           power = 1, not 0
           half_power = fast_exponentation_recursive(2, 0)
           1 is odd → return 2 * half_power * half_power
        5. fast_exponentation_recursive(2, 0):
           power = 0 (base case)
           return 1
        6. Back to step 4: fast_exponentation_recursive(2, 1)
           half_power = 1
           return 2 * 1 * 1 = 2
        7. Back to step 3: fast_exponentation_recursive(2, 2)
           half_power = 2
           return 2 * 2 = 4
        8. Back to step 2: fast_exponentation_recursive(2, 5)
           half_power = 4
           return 2 * 4 * 4 = 32
        9. Back to step 1: fast_exponentation_recursive(2, 10)
           half_power = 32
           return 32 * 32 = 1024

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

    Notes:
        This recursive implementation has the advantage of being more intuitive
        for understanding the mathematical properties of exponentiation. However,
        it uses more memory due to recursion stack overhead.
    """

    if power == 0:
        return 1

    half_power = fast_exponentation_recursive(base, power // 2)

    if power % 2 == 0:
        return half_power * half_power
    else:
        return base * half_power * half_power


def fast_exponentation_iterative(base, power) -> int:
    """
    Fast Exponentiation - Iterative Implementation

    This function implements an iterative version of fast exponentiation (also known as
    exponentiation by squaring), which efficiently computes large powers using the
    mathematical property: a^n = a^(n/2) * a^(n/2) if n is even, and a^n = a * a^(n/2) * a^(n/2) if n is odd.

    Unlike the recursive implementation, this version uses an iterative loop to avoid
    recursion stack overhead and achieve O(1) space complexity. The algorithm processes
    the exponent by examining its binary representation, building the result through
    multiplication and squaring operations.

    Algorithm Steps:
        1. Handle base case: If power is 0, return 1
        2. Initialize result = 1 and temp = base
        3. Loop while power > 0:
           a. If power is odd (power % 2 == 1):
              - Multiply result by temp
              result = result * temp
           b. Square the temp: temp = temp * temp
           c. Integer divide power by 2: power = power // 2
        4. Return the result

    Input:
        base: The base number to be exponentiated (integer)
        power: The exponent to which the base is raised (non-negative integer)

    Output:
    Returns base^power as an integer

    Example:
        >>> fast_exponentation_iterative(2, 10)
        1024
        >>> fast_exponentation_iterative(3, 5)
        243
        >>> fast_exponentation_iterative(5, 0)
        1
        >>> fast_exponentation_iterative(10, 3)
        1000

        Step-by-step example for fast_exponentation_iterative(2, 10):
        Binary representation of 10: 1010
        
        Iteration 1:
            power = 10 (1010), result = 1, temp = 2
            power % 2 == 0 → not odd
            temp = 2 * 2 = 4
            power = 10 // 2 = 5
        
        Iteration 2:
            power = 5 (101), result = 1, temp = 4
            power % 2 == 1 → odd
            result = 1 * 4 = 4
            temp = 4 * 4 = 16
            power = 5 // 2 = 2
        
        Iteration 3:
            power = 2 (10), result = 4, temp = 16
            power % 2 == 0 → not odd
            temp = 16 * 16 = 256
            power = 2 // 2 = 1
        
        Iteration 4:
            power = 1 (1), result = 4, temp = 256
            power % 2 == 1 → odd
            result = 4 * 256 = 1024
            temp = 256 * 256 = 65536
            power = 1 // 2 = 0
        
        Loop ends (power = 0)
        Return 1024

        Another example for fast_exponentation_iterative(3, 5):
        Binary representation of 5: 101
        
        Iteration 1:
            power = 5 (101), result = 1, temp = 3
            power % 2 == 1 → odd
            result = 1 * 3 = 3
            temp = 3 * 3 = 9
            power = 5 // 2 = 2
        
        Iteration 2:
            power = 2 (10), result = 3, temp = 9
            power % 2 == 0 → not odd
            temp = 9 * 9 = 81
            power = 2 // 2 = 1
        
        Iteration 3:
            power = 1 (1), result = 3, temp = 81
            power % 2 == 1 → odd
            result = 3 * 81 = 243
            temp = 81 * 81 = 6561
            power = 1 // 2 = 0
        
        Return 243

    Complexity Analysis:
        Time Complexity: O(log n)
        - Each iteration halves the power (integer division by 2)
        - Number of iterations: log₂(n) (binary representation of n)
        - Each iteration does constant work (multiplications and condition checks)
        - Total operations: proportional to the number of bits in n

        Space Complexity: O(1)
        - Only uses a constant number of variables (result, temp, power)
        - No recursion stack or additional data structures
        - No additional space that grows with input size

        Comparison:
        - Naive approach: O(n) multiplications, O(1) space
        - Recursive fast exponentiation: O(log n) multiplications, O(log n) space
        - Iterative fast exponentiation: O(log n) multiplications, O(1) space

        Advantages:
        - No recursion stack overhead
        - More memory efficient than recursive version
        - Typically faster in practice due to reduced overhead
        - Avoids potential recursion depth limits

        Disadvantages:
        - Slightly more complex to understand than recursive version
        - Requires manual loop management

    Notes:
        This iterative approach builds the result by examining the binary representation
        of the exponent. When a bit is set (1), it means we need to multiply the current
        result by the current base value. We then square the base (because we move to
        the next bit position) and halve the exponent. This mirrors the mathematical
        property of exponents and avoids redundant calculations.
    """

    if power == 0:
        return 1

    result = 1
    temp = base

    while power > 0:
        if power % 2 == 1:
            result = result * temp
        temp = temp * temp
        power = power // 2

    return result
