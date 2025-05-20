def is_palindrome(s):
    """
    Function to check if the input string is a palindrome.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Your code here
    s = s.lower().replace(" ","")
    return s == s[::-1]

# Test cases
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("hello"))
print(is_palindrome("racecar"))