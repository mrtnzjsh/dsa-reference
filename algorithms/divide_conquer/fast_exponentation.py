# Fast Exponentiation Algorithm Implementation

# This module implements the fast exponentiation (also known as exponentiation by squaring)
# algorithm, which efficiently computes large powers by exploiting the mathematical property:
# a^n = a^(n/2) * a^(n/2) if n is even, and a^n = a * a^(n/2) * a^(n/2) if n is odd

# This algorithm dramatically reduces the time complexity from O(n) for the naive approach
# to O(log n) for the fast exponentiation method

# Algorithm Steps:
#     1. Base Case: If the power is 0, return 1 (any number to the power of 0 is 1)
#     2. Recursive Step: Calculate half_power = a^(power/2) recursively
#     3. Even Power: If power is even, return half_power * half_power
#     4. Odd Power: If power is odd, return base * half_power * half_power
#        This accounts for the extra base factor when the power is odd

def fast_exponentation_recursive(base, power) -> int:
    if power == 0:
        return 1

    half_power = fast_exponentation_recursive(base, power // 2)

    if power % 2 == 0:
        return half_power * half_power
    else:
        return base * half_power * half_power

def fast_exponentation_iterative(base, power) -> int:
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
