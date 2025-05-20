'''
Problem Description:

You are given an integer n. Your task is to return a pyramid pattern of numbers, 
where each row contains increasing numbers starting from 1 up to the row number, 
and the pyramid is centered with leading spaces.

Input: A single integer n, where 1 <= n <= 100.

Output: A list of strings where each string represents a row in the pyramid pattern.

Example:
Input: 4
Output: ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']
 
Input: 3
Output: ['  1  ', ' 1 2 ', '1 2 3']
'''

def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    pyramidPattern = []
    for x in range(1, n + 1):
        spaces = ' ' * (n - x)
        pyramidPattern.append(spaces + ' '.join(map(str, range(1, x + 1))) + spaces)
    return pyramidPattern

# Example usage
print(generate_number_pyramid(4))
print(generate_number_pyramid(3))