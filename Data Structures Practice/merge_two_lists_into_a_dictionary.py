def merge_lists_to_dictionary(keys, values):
    # Your code goes here
    if len(keys) != len(values):
        return False
        
    result = {}
    
    # return dict(zip(keys, values))
    for i in range(len(keys)):
        # Add each key-value pair to the dictionary
        result[keys[i]] = values[i]

    return result

# Test cases
print(merge_lists_to_dictionary(['a', 'b', 'c'], [1, 2, 3]))
print(merge_lists_to_dictionary(['a', 'b', 'c'], [1, 2]))