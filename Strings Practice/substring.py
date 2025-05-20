def is_substring(s, t):
    """
    Function to check if string t is a substring of string s without using built-in functions and recursion.
    
    Parameters:
    s (str): The main string.
    t (str): The string to check as a substring.
    
    Returns:
    bool: True if t is a substring of s, False otherwise.
    """
    # Your code here
    # Get lengths of both strings
    len_s = len(s)
    len_t = len(t)

    # If t is longer than s, it can't be a substring
    if len_t > len_s:
        return False

    # Loop through each position in s where t could start
    for i in range(len_s - len_t + 1):
        match = True  # Assume a match
        for j in range(len_t):
            if s[i + j] != t[j]:  # Compare each character
                match = False
                break
        if match:
            return True  # Found a match

    return False  # No match found

# Test cases
print(is_substring("Hello world", "world"))  # Output: True
print(is_substring("Hello world", "hello"))  # Output: False