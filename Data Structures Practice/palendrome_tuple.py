def is_palindromic_tuple(tup):
    # Your code goes here
    return tup == tup[::-1]

# Test cases
print(is_palindromic_tuple((1, 2, 3, 2, 1)))  # True
print(is_palindromic_tuple((1, 2, 3, 4, 5)))  # False