def gcd(a: int, b: int) -> int:
    """Calculate GCD using recursive Euclidean algorithm."""
    # Handle negative numbers
    a = abs(a)
    b = abs(b)
    
    # Base case: if b is 0, a is the GCD
    if b == 0:
        return a
    
    # Recursive case
    return gcd(b, a % b)


def gcd_iterative(a: int, b: int) -> int:
    """Calculate GCD using iterative Euclidean algorithm."""
    # Handle negative numbers
    a = abs(a)
    b = abs(b)
    
    # Iterate until b becomes 0
    while b != 0:
        a, b = b, a % b
    
    return a


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Calculate GCD and extended coefficients using extended Euclidean algorithm.

    Returns:
        Tuple of (gcd, x, y) where a*x + b*y = gcd(a, b)
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
