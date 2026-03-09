"""
Bitwise OR Operator Examples

The OR operator (|) compares two bits and returns 1 if at least one of the bits is 1,
otherwise returns 0. It's commonly used for:
- Setting specific bits to 1 (bit masking)
- Combining multiple sets/flags
- Binary addition
- Finding commonalities in binary representations

Example 1: Setting a Specific Bit Using Bitwise OR
----------------------------------------------------
This algorithm demonstrates how to force a specific bit to 1 using OR.
When you OR a bit position with 1, it always becomes 1 regardless of the original value.
"""
def set_bit_to_1(number, bit_position):
    """
    Set a specific bit to 1.
    
    Args:
        number: The integer to modify
        bit_position: The 0-indexed position of the bit to set
    
    Returns:
        Integer with the specified bit set to 1
    
    Algorithm:
        1. Create a mask by shifting 1 to the left by the bit_position
        2. Use OR to force the bit to 1
    """
    mask = 1 << bit_position
    return number | mask


"""
Example 2: Merging Two Sets Using Bitwise OR
--------------------------------------------
This algorithm demonstrates how to combine two sets or merge flags using OR.
When you OR two bit masks together, you get all bits that are set in either of them.
"""
def merge_sets(set1, set2):
    """
    Merge two sets represented as integers using bitwise OR.
    
    Args:
        set1: First integer representing a set
        set2: Second integer representing a set
    
    Returns:
        Integer representing the union of both sets
    
    Algorithm:
        1. OR the two integers together
        2. Each bit that is 1 in either set1 or set2 will be 1 in the result
    """
    return set1 | set2


"""
Example 3: Binary Addition Using Bitwise OR
-------------------------------------------
This algorithm demonstrates how to perform binary addition using only OR operations.
When you OR two numbers, you get bits where both numbers have 1 in the same position.
"""
def binary_addition_addend_only(number1, number2):
    """
    Add two binary numbers using OR operation.
    
    Args:
        number1: First number to add
        number2: Second number to add
    
    Returns:
        Integer representing the sum
    
    Algorithm:
        1. Use OR to get bits where both numbers have 1 in the same position
        2. The result represents the sum of two 1s at the same position (with carry ignored)
    """
    return number1 | number2


"""
Example 4: Finding Maximum Number from OR Values
-------------------------------------------------
This algorithm finds the maximum number that can be formed from OR operations of array elements.
When you OR numbers together, the bits that are set in any element will be set in the result.
"""
def find_max_or_value(numbers):
    """
    Find the maximum number that can be formed from OR operations of an array.
    
    Args:
        numbers: List of integers to process
    
    Returns:
        Maximum integer value that can be formed by ORing any subset of numbers
    
    Algorithm:
        1. Initialize result as 0
        2. OR each number with the result
        3. After processing all numbers, the result has all bits that appear in any element
    """
    max_value = 0
    for num in numbers:
        max_value = max_value | num
    return max_value


"""
Example 5: Checking Common Set Members Using Bitwise OR
-------------------------------------------------------
This algorithm demonstrates how to check if two sets have any common elements
by examining if the OR result has any bits set.
"""
def have_common_elements(set1, set2):
    """
    Check if two sets have at least one common element.
    
    Args:
        set1: First integer representing a set
        set2: Second integer representing a set
    
    Returns:
        Boolean indicating if there's at least one common element
    
    Algorithm:
        1. Compute OR of the two sets
        2. If the result is non-zero, there are common elements
        3. Each bit in the result represents an element that exists in at least one set
    """
    result = set1 | set2
    return result != 0
