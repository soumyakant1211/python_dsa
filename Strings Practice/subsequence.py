def is_subsequence(s, t):
    """
    Function to check if t is a subsequence of s.
    
    Parameters:
    s (str): The original string.
    t (str): The target subsequence string.
    
    Returns:
    bool: True if t is a subsequence of s, False otherwise.
    """
    # Your code here
    i = 0  # Pointer for t

    for char in s:
        if i < len(t) and char == t[i]:
            i += 1

    return i == len(t)

# Test cases
print(is_subsequence("abcde", "ace"))  # True
print(is_subsequence("abcde", "axcye"))  # False