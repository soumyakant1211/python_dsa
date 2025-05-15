'''
Problem Description:
You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part 
(the widest row will have 2n - 1 stars), 
and the lower part is the mirrored version of the upper part. 
Each row should be centered with appropriate spaces.

Input:
A single integer n, where 1 <= n <= 100.

Output:
A list of strings where each string represents a row in the diamond pattern.

Example:
Input: 3
Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']

'''

def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    if n % 2 == 0:
        raise ValueError("n must be an odd number")

    diamond = []
    # Top half of the diamond
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        diamond.append(spaces + stars + spaces)

    # Bottom half of the diamond
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        diamond.append(spaces + stars + spaces)
    return diamond

# Example usage
print(generate_diamond(3))
print(generate_diamond(5))