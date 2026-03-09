"""
Bitwise NOT Operator Examples

The NOT operator (~) inverts all bits of an integer. It's commonly used for:
- Computing two's complement (negation)
- Bitwise complement operations
- Converting between different representations
- Checking for zero or non-zero values
- Complementing sets

Example 1: Basic Bitwise NOT Operation
---------------------------------------
This algorithm demonstrates the fundamental bitwise NOT operation.
The NOT operator flips every bit: 0 becomes 1, and 1 becomes 0.
"""
def basic_not_operator(number):
    """
    Perform basic bitwise NOT on a number.
    
    Args:
        number: The integer to invert
    
    Returns:
        Integer with all bits flipped
    
    Algorithm:
        1. Apply bitwise NOT operator to the number
        2. Each bit is inverted: 0 becomes 1, 1 becomes 0
    """
    return ~number


"""
Example 2: Computing Two's Complement (Negative Number)
-------------------------------------------------------
This algorithm demonstrates how to compute the two's complement of a number,
which is used to represent negative numbers in binary.
Two's complement is: NOT of number + 1
"""
def two_complement(number):
    """
    Compute the two's complement of a number.
    
    Args:
        number: The integer to negate
    
    Returns:
        Integer representing the negative of the input
    
    Algorithm:
        1. Invert all bits using NOT operator
        2. Add 1 to get the two's complement
    """
    return ~number + 1


"""
Example 3: Finding One's Complement
-----------------------------------
This algorithm demonstrates the one's complement operation,
which simply inverts bits without adding 1. This is useful in
digital logic and hardware design.
"""
def one_complement(number):
    """
    Compute the one's complement of a number.
    
    Args:
        number: The integer to complement
    
    Returns:
        Integer with all bits flipped
    
    Algorithm:
        1. Apply bitwise NOT operator
        2. No addition is performed (unlike two's complement)
    """
    return ~number


"""
Example 4: Checking for Zero Value
-----------------------------------
This algorithm demonstrates how to use bitwise NOT to check if a number is zero.
When you NOT a number, the result will be -1 if the original was 0.
"""
def is_zero_with_not(number):
    """
    Check if a number is zero using bitwise NOT.
    
    Args:
        number: The integer to check
    
    Returns:
        Boolean indicating if the number is zero
    
    Algorithm:
        1. Apply NOT operator to the number
        2. If the result is -1, the original was 0
        3. If the result is not -1, the original was non-zero
    """
    return ~number == -1


"""
Example 5: Inverting Specific Bit Range
---------------------------------------
This algorithm demonstrates how to invert only a specific range of bits
using bitwise NOT with masking.
"""
def invert_bit_range(number, bit_range_start, bit_range_end):
    """
    Invert only a specific range of bits.
    
    Args:
        number: The integer to modify
        bit_range_start: Starting position of the range (0-indexed)
        bit_range_end: Ending position of the range (exclusive)
    
    Returns:
        Integer with the specified bit range inverted
    
    Algorithm:
        1. Create a mask with 1s in the specified range
        2. Invert only the masked portion using NOT
    """
    range_size = bit_range_end - bit_range_start
    mask = ((1 << range_size) - 1) << bit_range_start
    inverted_mask = ~mask
    return number & inverted_mask


"""
Example 6: Converting Between Sign and Magnitude
------------------------------------------------
This algorithm demonstrates how to use bitwise NOT to flip the sign bit
in fixed-width numbers, useful for debugging and understanding binary representation.
"""
def flip_sign_bit(number, bit_width=32):
    """
    Flip the sign bit of a fixed-width number.
    
    Args:
        number: The integer to modify
        bit_width: Number of bits to consider
    
    Returns:
        Integer with sign bit flipped
    
    Algorithm:
        1. Create a mask with the sign bit set
        2. Flip only the sign bit using bitwise NOT
    """
    sign_mask = 1 << (bit_width - 1)
    flipped_sign = ~sign_mask
    return number & flipped_sign
