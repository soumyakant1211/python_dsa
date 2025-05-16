def is_perfect_square(n):
    """
    Function to check if a number is a perfect square.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
    # Your code here
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

# Test cases
print(is_perfect_square(4))  # True
print(is_perfect_square(9))  # True
print(is_perfect_square(5))  # False