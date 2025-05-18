def count_words(s):
    """
    Function to count the number of words in the input string.
    
    Parameters:
    s (str): The input string to check for words.
    
    Returns:
    int: The count of words in the input string.
    """
    # Your code here
    return len(s.split())

# Test cases
print(count_words("Hello world"))
print(count_words("Hello world, how are you?"))