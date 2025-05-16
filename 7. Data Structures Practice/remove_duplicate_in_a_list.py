def remove_duplicates(lst):
    # Your code goes here
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 2, 3, 4, 4, 5]
    result = remove_duplicates(my_list)
    print(f"List after removing duplicates: {result}")