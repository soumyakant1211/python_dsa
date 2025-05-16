def check_unique(lst):
    # Your code goes here
    seen = set()

    # Check for duplicates
    unique = True
    for x in lst:
        if x in seen:
            return False
        seen.add(x)
    
    return True

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = check_unique(my_list)
    print(f"List is unique: {result}")