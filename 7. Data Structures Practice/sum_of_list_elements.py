'''
Problem Description: Sum of List Elements
Write a Python function that calculates the sum of all elements in a given list of integers.

Parameters: numbers (List of integers): The input list containing integers.

Returns: An integer representing the sum of all elements in the input list.

Example:
Input: numbers = [1, 2, 3, 4, 5]
Output: 15

Input: numbers = [10, -5, 7, 8, -2]
Output: 18
'''

def sum_list(numbers):
    # Your code goes here
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum

# Example usage
print(sum_list([1, 2, 3, 4, 5]))
print(sum_list([10, -5, 7, 8, -2]))