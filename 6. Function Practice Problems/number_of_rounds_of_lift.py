'''
Problem Description:
You are given n, the total number of people, and capacity, the maximum number of people the lift can carry at a time. 
All people want to go from the ground floor to the top floor. 
Your task is to calculate the number of rounds the lift has to make to transport all the people to the top floor.

Input:
Two integers, n and capacity, where n is the total number of people, 
and capacity is the maximum number of people the lift can carry in one round.

Output:
An integer representing the number of rounds the lift needs to cover to transport all people to the top floor.

Example:
Input: n = 10, capacity = 3
Output: 4
 
Input: n = 7, capacity = 4
Output: 2
'''

def number_of_rounds_of_lift(n, capacity):
    """
    Function to calculate the number of rounds a lift needs to make to transport all people to the top floor.
    
    Parameters:
    n (int): The total number of people.
    capacity (int): The maximum number of people the lift can carry at a time.
    
    Returns:
    int: The number of rounds the lift needs to make.
    """
    # Your code here
    return (n + capacity - 1) // capacity

# Example usage
print(number_of_rounds_of_lift(10, 3))
print(number_of_rounds_of_lift(7, 4))