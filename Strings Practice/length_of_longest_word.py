def longest_word_length(s):
    """
    Function to find the length of the longest word in a string without using built-in functions.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The length of the longest word.
    """
    # Your code here
    longestWord = 0
    words = s.split()
    for word in words:
        longestWordLength = len(word)
        if longestWordLength > longestWord:
            longestWord = longestWordLength
    return longestWord

# Test cases
print(longest_word_length("Hello world"))  # Output: 5
print(longest_word_length("Hello world, how are you?"))  # Output: 6