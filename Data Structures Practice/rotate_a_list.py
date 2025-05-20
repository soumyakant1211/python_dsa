def rotate_list(lst, k):
    # Your code goes here
    if not lst:
        return []
        
    k = k % len(lst)

    for _ in range(k):
        lastElement = lst.pop()
        lst.insert(0, lastElement)
        
    return lst
    
# Test cases
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3], 3))