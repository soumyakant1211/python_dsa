def merge_two_sorted_lists(list1, list2):
    # Your code goes here
    list1.extend(list2)
    list1.sort()
    return list1

# Test cases
print(merge_two_sorted_lists([1, 3, 5], [2, 4, 6]))
print(merge_two_sorted_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))