'''
Problem Description:
You are given an integer n. Your task is to return a hollow inverted right-angled triangle pattern of '*', 
where the first row contains n stars, while the inner rows contain a star at the beginning and end, 
with spaces in between. The triangle should be left-aligned.

Input: A single integer n, where 1 <= n <= 100.

Output: A list of strings where each string represents a row in the hollow inverted right-angled triangle.

Example:
Input: 4
Output: ['****', '* *', '**', '*']
 
Input: 5
Output: ['*****', '*  *', '* *', '**', '*']
'''

def generate_hollow_inverted_triangle(n):
    """
    Function to return a hollow inverted right-angled triangle pattern of '*', 
    where the first row contains n stars, while the inner rows contain a star at the beginning and end, 
    with spaces in between. The triangle should be left-aligned.

    Parameters:
    n (int): The number of rows in the triangle.

    Returns:
    list: A list of strings where each string represents a row in the hollow inverted right-angled triangle.
    """
    triangle = []
    for i in range(n, 0, -1):
        if i == 1 or i == n:
            triangle.append('*' * i)
        else:
            triangle.append('*' + ' ' * (i - 2) + '*')
    return triangle

# Example usage
print(generate_hollow_inverted_triangle(4))
print(generate_hollow_inverted_triangle(5))