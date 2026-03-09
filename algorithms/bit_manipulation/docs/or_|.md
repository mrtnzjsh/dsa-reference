# Bitwise OR (|) Operator

## Overview
Performs a bitwise OR operation on two integers. Returns 1 where either bit is 1, 0 otherwise.

## Use Cases

### 1. Setting Bits - Force a Bit to 1
Force a specific bit to 1 regardless of its original value using OR with 1. Common for enabling flags or forcing certain states.

```python
# Force the 3rd bit to 1
value = 0b01001010
mask = 0b00000100
result = value | mask
# result = 0b01101010
```

### 2. Merging Sets - Combine Flags
Combine multiple sets or flags by OR-ing them together. Each bit that is set in any set will be set in the result.

```python
# Merge two sets
set_a = 0b101101
set_b = 0b01011010
merged = set_a | set_b
# merged = 0b11111110
```

### 3. Binary Addition Without Carry
Add two binary numbers using only OR operations. When two 1s appear in the same position, the result will have a 1 there (ignoring carry).

```python
# Add two numbers using OR
num1 = 0b00011010
num2 = 0b00100111
result = num1 | num2
# result = 0b00111111
```

### 4. Finding Maximum OR Value
Find the maximum possible value by OR-ing all elements in an array together. The result contains all bits that appear in any element.

```python
# Find maximum OR from array
values = [0b001010, 0b100110, 0b011001]
max_or = 0
for val in values:
    max_or = max_or | val
# max_or = 0b111111
```

### 5. Checking Common Elements
Check if two sets have any common elements by examining if the OR result is non-zero.

```python
# Check if sets have common elements
set_a = 0b101101
set_b = 0b01011010
common_exists = (set_a | set_b) != 0
# common_exists = True
```

## Complexity Analysis

**Time Complexity:** O(1) - constant time regardless of input size

**Space Complexity:** O(1) - uses fixed number of bits

## Practical Notes
- Operates on individual bits in parallel
- Fast for bit-level operations compared to arithmetic operations
- Used in bitmask operations, graphics, networking, and performance-critical code
- Particularly useful for combining configurations, toggling features on, and finding commonalities
