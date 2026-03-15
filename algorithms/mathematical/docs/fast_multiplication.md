The Fast Multiplication Algorithms module implements fast multiplication algorithms for computing the product of large integers more efficiently than the traditional O(n²) multiplication algorithm.

## Overview
### Karatsuba Algorithm
- **Complexity:** O(n^log₂(3)) ≈ O(n^1.585)
- **Method:** Divide-and-conquer multiplication
- **Reduces multiplications:** From 4 to 3 using identity transformation
- **Formula:** a*b = ((a₁-a₀)(b₁-b₀)) + a₀*b₁*10^k + a₁*b₀*10^k

### Toom-Cook Algorithm
- **Complexity:** O(n^log₃(5)) ≈ O(n^1.465)
- **Method:** Generalization of Karatsuba
- **Features:** Uses polynomial interpolation, more efficient for very large numbers

### Schönhage-Strassen Algorithm
- **Complexity:** O(n log n log log n)
- **Method:** Number theoretic transform (NTT)
- **Use case:** For large numbers
- **Application:** Practical use for multiplication of very large integers


## Complexity Analysis

**Time Complexity:**
- Karatsuba: O(n^log₂(3)) ≈ O(n^1.585)
- Toom-Cook: O(n^log₃(5)) ≈ O(n^1.465)
- Schönhage-Strassen: O(n log n log log n)

**Space Complexity:**
- O(n)
  - For recursive implementations: O(log n) for the call stack
  - For Toom-Cook and Schönhage-Strassen: O(n) for temporary storage

## Example

**Example 1: Karatsuba Multiplication**
```python
>>> karatsuba(123, 456)
56088
```

**Step-by-Step:**
1. Split 123 and 456 by m = 2 digits
   - high1 = 1, low1 = 23
   - high2 = 4, low2 = 56
2. Calculate sub-products:
   - z0 = karatsuba(23, 56) = 1288
   - z1 = karatsuba((23+1), (56+4)) = karatsuba(24, 60) = 1440
   - z2 = karatsuba(1, 4) = 4
3. Combine: (4 * 100⁴) + ((1440 - 4 - 1288) * 10²) + 1288
   = 40000 + (148 * 100) + 1288
   = 40000 + 14800 + 1288
   = 56088

**Example 2: Toom-Cook Multiplication**
```python
>>> toom_cook(1234, 5678)
7006652
```

**Example 3: Schönhage-Strassen Multiplication**
```python
>>> schoenhage_strassen(1234, 5678)
7006652
```

**Example 4: Large Numbers**
```python
>>> karatsuba(123456789, 987654321)
121932631112635269
```


## Notes

The Karatsuba algorithm was discovered by Anatolii Karatsuba in 1960 and revolutionized the field of fast multiplication algorithms. It was the first algorithm to beat the naive O(n²) multiplication, achieving O(n^1.585) time complexity. The Toom-Cook algorithm generalizes Karatsuba and achieves O(n^1.465) by splitting numbers into more parts. The Schönhage-Strassen algorithm, developed in 1971, is the most efficient known algorithm for multiplication of very large integers and is used in practice for multiplication of integers with hundreds of thousands of digits.

These algorithms are essential in cryptography, where RSA encryption requires multiplication of extremely large numbers. The choice of algorithm depends on the size of the numbers and the specific application requirements.
