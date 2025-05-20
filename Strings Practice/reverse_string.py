def reverse_string(s):
    """
    Function to return the reversed version of the input string.
    
    Parameters:
    s (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    # Your code here
    return s[::-1]

# Example usage
if __name__ == "__main__":
    input_string = "Hello, World!"
    reversed_string = reverse_string(input_string)
    print(f"Original string: {input_string}")
    print(f"Reversed string: {reversed_string}")