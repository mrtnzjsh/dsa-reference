"""
Logic: Returns 1 only if both bits are 1.
Use Case: Checking if a specific bit is turned on (e.g., is the 'Error' bit set in this byte)
"""

def check_bit(n, bit_position):
    """
    Check if a specific bit is set in a number.
    Returns True if the bit is set, False otherwise.
    
    Example:
    >>> check_bit(13, 2)  # 13 = 1101 in binary, bit 2 is 1
    True
    >>> check_bit(13, 0)  # 13 = 1101 in binary, bit 0 is 1
    True
    >>> check_bit(13, 3)  # 13 = 1101 in binary, bit 3 is 1
    False
    """
    return (n & (1 << bit_position)) != 0


def clear_bit(n, bit_position):
    """
    Clear (set to 0) a specific bit in a number.
    Returns the new number with the specified bit cleared.
    
    Example:
    >>> clear_bit(13, 2)  # 13 = 1101, clearing bit 2
    9  # 9 = 1001 in binary
    >>> clear_bit(13, 0)  # 13 = 1101, clearing bit 0
    12 # 12 = 1100 in binary
    """
    return n & ~(1 << bit_position)


def set_bit(n, bit_position):
    """
    Set (turn on) a specific bit in a number.
    Returns the new number with the specified bit set to 1.
    
    Example:
    >>> set_bit(9, 2)  # 9 = 1001, setting bit 2
    13 # 13 = 1101 in binary
    >>> set_bit(12, 0)  # 12 = 1100, setting bit 0
    13 # 13 = 1101 in binary
    """
    return n | (1 << bit_position)


def toggle_bit(n, bit_position):
    """
    Toggle (flip) a specific bit in a number.
    If the bit is 0, it becomes 1; if it is 1, it becomes 0.
    Returns the new number with the specified bit toggled.
    
    Example:
    >>> toggle_bit(13, 2)  # 13 = 1101, toggling bit 2
    9  # 9 = 1001 in binary
    >>> toggle_bit(13, 0)  # 13 = 1101, toggling bit 0
    12 # 12 = 1100 in binary
    """
    return n ^ (1 << bit_position)


def count_set_bits(n):
    """
    Count the number of 1s (set bits) in the binary representation of a number.
    
    Example:
    >>> count_set_bits(13)  # 13 = 1101
    3
    >>> count_set_bits(7)   # 7 = 111
    3
    >>> count_set_bits(0)   # 0 = 0
    0
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def bits_equal(a, b):
    """
    Check if two numbers have the same set bits (are bitwise equal).
    Returns True if all bits are identical, False otherwise.
    
    Example:
    >>> bits_equal(5, 5)   # Both are 101 in binary
    True
    >>> bits_equal(5, 3)   # 101 vs 011
    False
    >>> bits_equal(0, 0)   # Both are 0 in binary
    True
    """
    return (a & b) == ((a ^ b) == 0)


def get_lowest_set_bit(n):
    """
    Get the position of the lowest set bit in a number.
    Returns the position (0-indexed) of the lowest 1-bit, or -1 if no bits are set.
    
    Example:
    >>> get_lowest_set_bit(12)  # 12 = 1100
    2
    >>> get_lowest_set_bit(24)  # 24 = 11000
    3
    >>> get_lowest_set_bit(0)   # 0 has no set bits
    -1
    """
    if n == 0:
        return -1
    return (n & -n).bit_length() - 1


def clear_all_bits_except_specific_bits(n, mask):
    """
    Clear all bits except those specified in the mask.
    Only bits in the mask remain set; all others become 0.
    
    Example:
    >>> clear_all_bits_except_specific_bits(13, 9)  # 13 = 1101, keep 1001
    9  # 9 = 1001 in binary
    >>> clear_all_bits_except_specific_bits(255, 255)  # Keep all bits
    255 # 255 = 11111111 in binary
    >>> clear_all_bits_except_specific_bits(255, 1)   # Only keep lowest bit
    1  # 1 = 1 in binary
    """
    return n & mask
