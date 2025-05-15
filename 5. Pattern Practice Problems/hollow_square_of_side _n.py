'''
Problem Description:
You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

Input Parameters:
n (int): The size of the square (number of rows and columns).

Output:
A list of strings where each string is a row of n characters, representing a hollow square.

Example:
Input: 3
Output: ['***', '* *', '***']
 
Input: 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']
'''

def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    # Initialize the result list
    result = []
    
    # Loop through the rows
    for i in range(n):
        # For the first and last row, fill it entirely with '*'
        if i == 0 or i == n - 1:
            result.append('*' * n)
        else:
            # For the middle rows, put '*' at the first and last position and space in between
            result.append('*' + ' ' * (n - 2) + '*')
    
    return result

# Example usage
print(generate_hollow_square(3))
print(generate_hollow_square(5))