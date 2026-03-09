"""
Bitwise Shift Operator Examples

The shift operators (<< and >>) move bits to the left or right. The left shift
operator (<<) is commonly used for:
- Multiplication by powers of two
- Setting specific bits to 1
- Creating bit masks
- Shifting data to encode/decode values

The right shift operator (>>) is commonly used for:
- Division by powers of two
- Extracting specific bits
- Sign extension
- Bitwise operations for compression

Example 1: Left Shift for Multiplication
----------------------------------------
This algorithm demonstrates using left shift as a fast way to multiply by 2.
Shifting left by n positions multiplies by 2^n.
"""
def left_shift_multiply(number, shift_amount):
    """
    Multiply a number by 2^n using left shift.
    
    Args:
        number: The integer to multiply
        shift_amount: Number of positions to shift
    
    Returns:
        Integer representing number * 2^shift_amount
    
    Algorithm:
        1. Shift the number left by shift_amount positions
        2. Each shift left multiplies by 2
        3. Equivalent to number * 2^shift_amount
    """
    return number << shift_amount


"""
Example 2: Right Shift for Division
-----------------------------------
This algorithm demonstrates using right shift as a fast way to divide by 2.
Shifting right by n positions divides by 2^n (for non-negative numbers).
"""
def right_shift_divide(number, shift_amount):
    """
    Divide a number by 2^n using right shift.
    
    Args:
        number: The integer to divide
        shift_amount: Number of positions to shift
    
    Returns:
        Integer representing number / 2^shift_amount
    
    Algorithm:
        1. Shift the number right by shift_amount positions
        2. Each shift right divides by 2
        3. Equivalent to number // 2^shift_amount (for non-negative)
    """
    return number >> shift_amount


"""
Example 3: Setting a Bit Using Left Shift
-----------------------------------------
This algorithm creates a mask by left shifting 1 to a specific position.
This is similar to the OR example but emphasizes the shift operation.
"""
def create_bit_mask(bit_position):
    """
    Create a bit mask for a specific position.
    
    Args:
        bit_position: The 0-indexed position of the bit
    
    Returns:
        Integer with only the specified bit set to 1
    
    Algorithm:
        1. Left shift 1 by the bit_position
        2. Create a mask with only that bit set
    """
    return 1 << bit_position


"""
Example 4: Extracting Specific Bits Using Right Shift
-----------------------------------------------------
This algorithm extracts a specific bit value by right shifting to position
and optionally masking with 1.
"""
def extract_bit(number, bit_position):
    """
    Extract the value of a specific bit.
    
    Args:
        number: The integer to extract from
        bit_position: The 0-indexed position of the bit
    
    Returns:
        The value of the specified bit (0 or 1)
    
    Algorithm:
        1. Right shift the number to move the bit to LSB position
        2. Mask with 1 to get only the bit value
    """
    return (number >> bit_position) & 1


"""
Example 5: Sign-Extension Right Shift
-------------------------------------
This algorithm demonstrates how right shift maintains the sign bit,
which is important for preserving negative numbers in two's complement.
"""
def sign_extension_right_shift(number, total_bits):
    """
    Sign-extend a number to a larger bit width.
    
    Args:
        number: The integer to sign-extend
        total_bits: Total number of bits for the result
    
    Returns:
        Integer sign-extended to the total bit width
    
    Algorithm:
        1. Right shift until all bits match the sign bit
        2. Extend the sign to fill all positions
    """
    sign_mask = 1 << (total_bits - 1)
    if number & sign_mask:
        return number | ~((1 << total_bits) - 1)
    return number & (sign_mask - 1)


"""
Example 6: Encoding Multiple Values with Bit Shifts
---------------------------------------------------
This algorithm demonstrates how to combine multiple values using bit shifts
to create a single encoded integer, commonly used in data structures.
"""
def encode_values(value1, value2, value3, bits_per_value):
    """
    Encode three values into a single integer using bit shifts.
    
    Args:
        value1: First value to encode
        value2: Second value to encode
        value3: Third value to encode
        bits_per_value: Number of bits each value occupies
    
    Returns:
        Single integer containing all values
    
    Algorithm:
        1. Shift value1 to correct position
        2. Shift value2 to correct position
        3. Shift value3 to correct position
        4. Combine all values into one integer
    """
    encoded = 0
    encoded |= value1 << (bits_per_value * 2)
    encoded |= value2 << bits_per_value
    encoded |= value3
    return encoded
