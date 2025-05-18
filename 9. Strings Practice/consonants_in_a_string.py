def count_consonants(s):
    """
    Function to count the number of consonants in the input string.
    
    Parameters:
    s (str): The input string to check for consonants.
    
    Returns:
    int: The count of consonants in the input string.
    """
    # Your code here
    count = 0
    vowels = 'aeiouAEIOU'
    for char in s:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            if char not in vowels:
                count += 1
    
    return count

# Test cases
print(count_consonants("Hello world"))  # Output: 7
print(count_consonants("Hello world, how are you?"))  # Output: 13