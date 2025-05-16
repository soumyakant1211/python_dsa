def merge_dicts_with_overlapping_keys(dicts):
    # Your code goes here
    result = {}
    for item in dicts:
        for key, value in item.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result

# Test cases
print(merge_dicts_with_overlapping_keys([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]))
print(merge_dicts_with_overlapping_keys([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]))