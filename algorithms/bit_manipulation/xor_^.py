"""
Bitwise XOR Operator Examples

The XOR operator (^) compares two bits and returns 1 if they are different,
0 if they are the same. It's commonly used for:
- Toggling bits (flipping 0 to 1 or 1 to 0)
- Finding differences between sets
- Binary addition with carry
- Swapping values without temporary variables
- Checking parity (even/odd)

Example 1: Toggling a Bit Using Bitwise XOR
--------------------------------------------
This algorithm demonstrates how to flip a specific bit using XOR with 1.
When you XOR a bit position with 1, it flips its value. When XORed with 0, it stays the same.
"""
def toggle_bit(number, bit_position):
    """
    Toggle a specific bit (flip 0 to 1 or 1 to 0).
    
    Args:
        number: The integer to modify
        bit_position: The 0-indexed position of the bit to toggle
    
    Returns:
        Integer with the specified bit toggled
    
    Algorithm:
        1. Create a mask by shifting 1 to the left by the bit_position
        2. Use XOR to flip the bit (1 XOR 1 = 0, 0 XOR 1 = 1)
    """
    mask = 1 << bit_position
    return number ^ mask


"""
Example 2: Flipping All Bits Using Bitwise XOR
-----------------------------------------------
This algorithm demonstrates how to flip all bits in a number using XOR with 1s.
This is equivalent to bitwise NOT, but works on fixed bit width.
"""
def invert_all_bits(number, bit_width=32):
    """
    Flip all bits in a number within a specified bit width.
    
    Args:
        number: The integer to invert
        bit_width: Number of bits to consider
    
    Returns:
        Integer with all bits flipped within the specified width
    
    Algorithm:
        1. Create a mask by filling all bits with 1 within the width
        2. Use XOR to flip all bits
    """
    mask = (1 << bit_width) - 1
    return number ^ mask


"""
Example 3: Finding Differences Between Two Sets
------------------------------------------------
This algorithm finds all bits that are set in one set but not the other.
When you XOR two sets, you get bits that are different between them.
"""
def find_differences(set1, set2):
    """
    Find bits that are different between two sets.
    
    Args:
        set1: First integer representing a set
        set2: Second integer representing a set
    
    Returns:
        Integer representing the XOR of both sets (only different bits)
    
    Algorithm:
        1. XOR the two integers together
        2. Bits set in result are those that differ between set1 and set2
    """
    return set1 ^ set2


"""
Example 4: Binary Addition with XOR and AND
--------------------------------------------
This algorithm performs binary addition using XOR for sum (without carry)
and AND for carry, then combines them. This is the standard full adder algorithm.
"""
def binary_addition(number1, number2):
    """
    Add two binary numbers using XOR and AND operations.
    
    Args:
        number1: First number to add
        number2: Second number to add
    
    Returns:
        Integer representing the sum
    
    Algorithm:
        1. Use XOR to get sum without carry: a XOR b
        2. Use AND and shift to get carry bits: (a AND b) << 1
        3. Repeat until no carry remains
    """
    while number2 != 0:
        carry = number1 & number2
        number1 = number1 ^ number2
        number2 = carry << 1
    return number1


"""
Example 5: Swapping Values Without Temporary Variable
------------------------------------------------------
This algorithm demonstrates the classic XOR swap trick.
XORing a variable with itself results in 0, and XORing with 0 returns the original.
"""
def swap_xor(a, b):
    """
    Swap two values without using a temporary variable.
    
    Args:
        a: First value
        b: Second value
    
    Returns:
        Tuple of swapped values
    
    Algorithm:
        1. XOR a with b and store in a (a now contains a XOR b)
        2. XOR a with original b (b XOR a XOR b = a)
        3. XOR a with original a (a XOR a XOR b = b)
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


"""
Example 6: Checking Parity (Even or Odd)
----------------------------------------
This algorithm checks if a number is even or odd using XOR with 1.
If the least significant bit is 0, the number is even; if 1, odd.
"""
def check_parity(number):
    """
    Check if a number is even or odd.
    
    Args:
        number: The integer to check
    
    Returns:
        String indicating even or odd
    
    Algorithm:
        1. XOR with 1 to flip the LSB
        2. If the result is 0, the number was even
        3. If the result is 1, the number was odd
    """
    return 'even' if (number ^ 1) == 0 else 'odd'
