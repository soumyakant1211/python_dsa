def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    # Your code here
    if n == 0:
        return "0"

    is_negative = n < 0
    n = abs(n)
    binary_digits = []

    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n = n // 2

    # Reverse the collected digits to get the correct binary number
    binary_digits.reverse()
    binary_str = ''.join(binary_digits)

    return '-' + binary_str if is_negative else binary_str

# Test cases
print(int_to_binary(10))  # Output: '1010'
print(int_to_binary(-5))  # Output: '-101'