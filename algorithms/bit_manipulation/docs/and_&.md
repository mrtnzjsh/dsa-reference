# Bitwise AND (&) Operator

## Overview
Performs a bitwise AND operation on two integers. Returns 1 where both bits are 1, 0 otherwise.

## Use Cases

### 1. Masking - Extract Specific Bits
Extract individual bits by AND-ing with a mask. Common for reading flags or state information.

```python
# Extract 4th bit from value
value = 0b10111001
mask = 0b00001000
result = value & mask
# result = 0b00001000 = 8
```

### 2. Checking Even Numbers
Check if a number is even using bit masking on the least significant bit.

```python
# Check if number is even
num = 42
if num & 1 == 0:
    print('Even')
```

### 3. Computing AND of Sets
Find common elements between two sets represented as bitmasks.

```python
# Find common bits between two integers
set_a = 0b101101
set_b = 0b01011010
common = set_a & set_b
# common = 0b10010000
```

## Complexity Analysis

**Time Complexity:** O(1) - constant time regardless of input size

**Space Complexity:** O(1) - uses fixed number of bits

## Practical Notes
- Operates on individual bits in parallel
- Fast for bit-level operations compared to arithmetic operations
- Used in low-level systems, graphics, networking, and performance-critical code
