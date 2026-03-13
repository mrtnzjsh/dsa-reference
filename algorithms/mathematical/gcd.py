"""
GCD / Euclidean Algorithm Implementation

This module implements the Greatest Common Divisor (GCD) algorithm using the Euclidean
algorithm, one of the oldest and most fundamental algorithms in mathematics. The Euclidean
algorithm finds the largest positive integer that divides two numbers without leaving a
remainder. It's widely used in number theory, cryptography, and various computer science
applications.

GCD Algorithm Overview:
    The Euclidean algorithm is a fundamental algorithm with numerous applications:
    - Cryptography (RSA encryption, Diffie-Hellman key exchange)
    - Number theory (solving Diophantine equations, finding modular inverses)
    - Computer graphics (image compression, pixel manipulation)
    - Data compression (lossless compression algorithms)
    - Music theory (rhythm and tempo calculations)
    - Financial mathematics (loan calculations, interest rates)
    - Cryptocurrency (blockchain algorithms, mining)
    - Network theory (graph theory, path finding)

Algorithm Description:
    The Euclidean algorithm is based on the principle that the GCD of two numbers also
    divides their difference. The algorithm repeatedly replaces the larger number by its
    remainder when divided by the smaller number, until one of the numbers becomes zero.
    The non-zero number at this point is the GCD.

Mathematical Foundation:
    Let a and b be two positive integers. The Euclidean algorithm computes:
    - gcd(a, b) = gcd(b, a mod b)
    - When b = 0, then gcd(a, b) = a

Algorithm Steps:
    1. Start with two numbers, a and b
    2. While b ≠ 0:
       a. Calculate the remainder r = a % b
       b. Replace a with b
       c. Replace b with r
    3. When b = 0, return a as the GCD

Input:
    a: An integer representing the first number
    b: An integer representing the second number

Output:
    Returns the greatest common divisor of a and b

Example:
    >>> gcd(48, 18)
    6

    >>> gcd(56, 32)
    8

    >>> gcd(17, 23)
    1

    >>> gcd(0, 10)
    10

    >>> gcd(0, 0)
    0

    Step-by-step example for gcd(48, 18):
    1. Initialize a = 48, b = 18
    2. b ≠ 0 → continue
    3. First iteration:
       - r = 48 % 18 = 12
       - a = 18, b = 12
    4. Second iteration:
       - r = 18 % 12 = 6
       - a = 12, b = 6
    5. Third iteration:
       - r = 12 % 6 = 0
       - a = 6, b = 0
    6. b = 0 → return a = 6
    The GCD of 48 and 18 is 6.

Complexity Analysis:
    Time Complexity: O(log(min(a, b)))
    - The algorithm reduces the problem size exponentially
    - Each iteration reduces the size of the numbers by a factor of at least 2
    - Space Complexity: O(1)
    - Only uses a constant amount of additional space
    - For the recursive version: O(log(min(a, b))) for the call stack

    Space Complexity:
    - Iterative version: O(1)
    - Recursive version: O(log(min(a, b))) for the recursion stack
    - Total space complexity is O(1) for the iterative version

    Note:
    The Euclidean algorithm is one of the oldest algorithms in mathematics, dating back
    to ancient Greece (approximately 300 BC). It's extremely efficient and has a running
    time that grows logarithmically with the input size, making it suitable for very
    large numbers. The algorithm can be extended to find the Extended Euclidean Algorithm,
    which not only finds the GCD but also computes integers x and y such that:
    - ax + by = gcd(a, b)
    This is useful for finding modular inverses, which are essential in cryptography.
    The Euclidean algorithm also has a connection to the Fibonacci numbers - the worst-
    case scenario occurs when a and b are consecutive Fibonacci numbers. The algorithm
    is used in many real-world applications including RSA encryption, where it's used
    to find the totient function and generate encryption keys.
"""

def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two numbers using the Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Greatest common divisor of a and b
    """
    # Handle negative numbers
    a = abs(a)
    b = abs(b)

    # Base case: if b is 0, a is the GCD
    if b == 0:
        return a

    # Recursive case: compute gcd(b, a % b)
    return gcd(b, a % b)


def gcd_iterative(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two numbers using the iterative Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Greatest common divisor of a and b
    """
    # Handle negative numbers
    a = abs(a)
    b = abs(b)

    # Iterate until b becomes 0
    while b != 0:
        a, b = b, a % b

    return a


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Calculate the greatest common divisor and extended coefficients using the extended Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        A tuple of (gcd, x, y) where a*x + b*y = gcd(a, b)
    """
    # Handle negative numbers
    a = abs(a)
    b = abs(b)

    # Base case
    if b == 0:
        return (a, 1, 0)

    # Recursive case
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return (gcd, x, y)
