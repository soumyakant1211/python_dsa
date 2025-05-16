def is_subset(lst1, lst2):
    # Your code goes here
    set1 = set(lst1)
    set2 = set(lst2)
    return set1.issubset(set2)

# Test cases
print(is_subset([1, 2, 3], [1, 2, 3, 4, 5]))
print(is_subset([1, 2, 3], [1, 2, 4, 5]))