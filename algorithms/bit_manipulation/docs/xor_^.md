# Bitwise XOR (^) Operator

## Overview
Performs a bitwise XOR operation on two integers. Returns 1 where bits are different, 0 where they are the same.

## Use Cases

### 1. Toggling Bits
Flip a specific bit between 0 and 1 using XOR with 1. Each XOR with 1 toggles the bit.

```python
# Toggle 3rd bit
value = 0b01001010
mask = 0b00000100
result = value ^ mask
# result = 0b01101010
```

### 2. Inverting All Bits
Flip all bits in a number within a specified width using XOR with 1s.

```python
# Invert all 32 bits
value = 0b10101010
mask = 0xFFFFFFFF
result = value ^ mask
# result = 0b01010101
```

### 3. Finding Differences Between Sets
Find bits that are set in one set but not the other using XOR.

```python
# Find differences between sets
set_a = 0b101101
set_b = 0b01011010
differences = set_a ^ set_b
# differences = 0b11101110
```

### 4. Binary Addition with Carry
Add two binary numbers using XOR for sum and AND for carry propagation.

```python
# Add two numbers using XOR
num1 = 0b00011010
num2 = 0b00100111
result = num1 ^ num2
# result = 0b00111111 (sum without carry)
```

### 5. Swapping Values
Swap two values without using a temporary variable using XOR.

```python
# Swap values
a = 5
b = 10
a = a ^ b
b = a ^ b
a = a ^ b
# a = 10, b = 5
```

### 6. Checking Parity
Check if a number is even or odd by examining the least significant bit.

```python
# Check parity
num = 42
if (num ^ 1) == 0:
    print('Even')
# Output: Even
```

## Complexity Analysis

**Time Complexity:** O(1) - constant time regardless of input size

**Space Complexity:** O(1) - uses fixed number of bits

## Practical Notes
- Operates on individual bits in parallel
- Fast for bit-level operations compared to arithmetic operations
- Particularly useful for toggling states, finding differences, and swapping
- XOR with a number returns the original number if XORed with itself (a ^ a = 0)
- XOR with 0 returns the original number (a ^ 0 = a)
