# Bitwise Shift Operators (<< and >>)

## Overview
Performs bit shifting operations. Left shift (<<) moves bits left, right shift (>>) moves bits right.
Left shift multiplies by 2^n, right shift divides by 2^n (for non-negative numbers).

## Use Cases

### 1. Left Shift for Multiplication
Multiply a number by 2^n using left shift operation.

```python
# Multiply by 4
value = 5
result = value << 2
# result = 20 (5 * 4)
```

### 2. Right Shift for Division
Divide a number by 2^n using right shift operation.

```python
# Divide by 2
num = 16
result = num >> 1
# result = 8 (16 / 2)
```

### 3. Creating Bit Masks
Generate a mask for a specific bit position.

```python
# Create mask for 3rd bit
position = 3
mask = 1 << position
# mask = 0b1000 = 8
```

### 4. Extracting Specific Bits
Retrieve the value of a specific bit position.

```python
# Extract 4th bit
value = 0b10111001
bit = (value >> 4) & 1
# bit = 1
```

### 5. Sign-Extension Right Shift
Preserve sign when shifting right (for two's complement).

```python
# Sign-extend negative number
num = -8
sign_bits = num >> 3
# sign_bits = -1 (sign bit extended)
```

### 6. Encoding Multiple Values
Combine multiple values into single integer using bit shifts.

```python
# Encode three values
val1 = 1
val2 = 2
val3 = 3
encoded = (val1 << 4) | (val2 << 2) | val3
# encoded = 0b110011
```

## Complexity Analysis

**Time Complexity:** O(1) - constant time regardless of input size

**Space Complexity:** O(1) - uses fixed number of bits

## Practical Notes
- Left shift multiplies by powers of two, right shift divides by powers of two
- Right shift on negative numbers preserves the sign bit
- Used for efficient multiplication/division, bit manipulation, and encoding
- Shifts by large amounts may have undefined behavior in some languages
