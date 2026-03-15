# GCD Algorithm

## Overview

This module implements the Greatest Common Divisor (GCD) using the Euclidean algorithm and its extended form. The Euclidean algorithm is one of the oldest and most widely used algorithms for computing the GCD of two integers, making it fundamental in number theory, cryptography, and various computational applications.

## Algorithm Steps

### GCD Function (Recursive)

1. Take two integers a and b
2. Convert both to absolute values
3. If b == 0, return a (base case)
4. Otherwise, recursively compute gcd(b, a % b)

### GCD Function (Iterative)

1. Take two integers a and b
2. Convert both to absolute values
3. While b != 0, set a, b = b, a % b
4. Return a when loop terminates

## Input

- `a`: First integer value
- `b`: Second integer value

## Output

- Returns the greatest common divisor of a and b

## Example

```python
>>> gcd(48, 18)
6
>>> gcd_iterative(48, 18)
6
>>> extended_gcd(48, 18)
(6, -1, 3)
```

### Step-by-step example for gcd(48, 18):

1. a = 48, b = 18
2. b != 0, so compute gcd(18, 48 % 18)
3. a = 18, b = 48
4. b != 0, so compute gcd(12, 18 % 12)
5. a = 12, b = 6
6. b != 0, so compute gcd(6, 12 % 6)
7. a = 6, b = 0
8. b == 0, return a = 6

### Step-by-step example for extended_gcd(48, 18):

1. a = 48, b = 18
2. b != 0, so compute extended_gcd(18, 48 % 18)
3. a = 18, b = 12
4. b != 0, so compute extended_gcd(12, 18 % 12)
5. a = 12, b = 6
6. b != 0, so compute extended_gcd(6, 12 % 6)
7. a = 6, b = 0
8. b == 0, return (6, 1, 0)
9. At each recursive level, compute:
   - gcd = 6, x1 = 0, y1 = 1
   - x = y1 = 1
   - y = x1 - (a // b) * y1 = 0 - (6 // 6) * 1 = -1
   - Return (6, 1, -1)
10. Final return (6, -1, 3) which satisfies 48*(-1) + 18*3 = -48 + 54 = 6

## Complexity Analysis

### Time Complexity: O(log(min(a, b)))

- The Euclidean algorithm reduces the problem size exponentially
- Each recursive step reduces the larger number by the remainder operation
- Average and worst-case complexity is logarithmic in the minimum of the two numbers
- Iterative version has the same time complexity but uses constant space

### Space Complexity: O(log n)

- Recursive version uses O(log n) stack space due to recursion depth
- Iterative version uses O(1) space
- Extended GCD function uses O(log n) space for recursion

## Notes

The extended Euclidean algorithm computes not only the GCD but also the coefficients x and y such that a*x + b*y = gcd(a, b). This is particularly useful in modular arithmetic, solving Diophantine equations, and finding modular inverses in cryptography applications. The algorithm also handles negative numbers by converting them to absolute values before computation.
