def count_vowels(s):
    """
    Function to count the number of vowels in the input string.
    
    Parameters:
    s (str): The input string to check for vowels.
    
    Returns:
    int: The count of vowels in the input string.
    """
    # Your code here
    count = 0
    vowels = 'aeiouAEIOU'
    for char in s:
        if char in vowels:
            count += 1
            
    return count

# Example usage
if __name__ == "__main__":
    s = "Hello, World!"
    print(count_vowels(s))