def is_even(n):
    """
    Function to check if a number is even.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is even, False otherwise.
    """
    # Your code here
    if n % 2 == 0:
        return True
    else:
        return False

# Test cases
print(is_even(4))  # True
print(is_even(5))  # False