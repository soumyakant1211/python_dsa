def gcd(n, m):
    """
    Function to find the GCD of two integers without using built-in functions and recursion.
    
    Parameters:
    n (int): The first integer.
    m (int): The second integer.
    
    Returns:
    int: The GCD of n and m.
    """
    # Your code here
    while m != 0:
        remainder = n % m
        n = m
        m = remainder
    return n

# Test cases
print(gcd(48, 18))  # 6 
print(gcd(10, 15))  # 5