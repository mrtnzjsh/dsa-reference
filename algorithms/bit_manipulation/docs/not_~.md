# Bitwise NOT (~) Operator

## Overview
Performs a bitwise NOT operation on an integer. Inverts all bits: 0 becomes 1, and 1 becomes 0.

## Use Cases

### 1. Basic Bitwise NOT
Flip all bits of a number to get its complement.

```python
# Invert all bits
value = 0b10101010
result = ~value
# result = 0b01010101
```

### 2. Two's Complement (Negative Numbers)
Compute the negative of a number by inverting bits and adding 1.

```python
# Get negative value
num = 5
negated = ~num
# negated = -6 (two's complement)
```

### 3. One's Complement
Simply invert all bits without adding 1, used in digital logic and hardware.

```python
# Get one's complement
value = 0b10101010
complement = ~value
# complement = 0b01010101
```

### 4. Zero Check
Check if a number is zero by examining if its NOT equals -1.

```python
# Check for zero
num = 0
if ~num == -1:
    print('Zero')
# Output: Zero
```

### 5. Invert Bit Range
Flip only a specific range of bits using NOT with masking.

```python
# Invert 4th to 6th bits
value = 0b00111111
mask = 0b00000111
result = ~mask
# result = 0b11111000 (inverts only the specified range)
```

### 6. Flip Sign Bit
Change the sign of a fixed-width number by flipping its sign bit.

```python
# Flip sign bit
num = 42
sign_mask = 0x80000000
flipped = ~sign_mask
# flipped = 0x7FFFFFFF
```

## Complexity Analysis

**Time Complexity:** O(1) - constant time regardless of input size

**Space Complexity:** O(1) - uses fixed number of bits

## Practical Notes
- Operates on individual bits in parallel
- NOT of zero is always -1 (all bits set to 1)
- NOT of -1 is always 0 (all bits cleared)
- Used for negation, bitwise complement operations, and digital logic
- Remember Python uses infinite precision, so NOT behavior extends to sign bit
