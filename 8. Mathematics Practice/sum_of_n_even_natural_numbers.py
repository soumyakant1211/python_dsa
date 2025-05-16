def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers.
    
    Parameters:
    n (int): The number of even numbers to sum.
    
    Returns:
    int: The sum of the first n even natural numbers.
    """
    # Your code here
    sum = 0
    current_number = 2
    for i in range(n):
        sum = sum + current_number
        current_number = current_number + 2
    return sum

# Test cases
print(sum_of_even_numbers(5))
print(sum_of_even_numbers(10))