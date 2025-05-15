'''
Problem Description:
You are given an integer n. Your task is to return a right-angled triangle pattern of '*', 
where each row contains stars aligned to the right. The first row has one star, 
the second row has two stars, and so on, until the nth row has n stars.

Input:
A single integer n, where 1 <= n <= 100.

Output:
A list of strings where each string represents a row in the right-angled triangle, right-aligned.

Example:
Input: 4
Output: ['   *', '  **', ' ***', '****']
 
Input: 3
Output: ['  *', ' **', '***']

'''

def generate_right_angled_triangle(n):
    return [' ' * (n - i) + '*' * i for i in range(1, n + 1)]

# Example usage
print(generate_right_angled_triangle(4))
print(generate_right_angled_triangle(3))