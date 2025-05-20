def reverse_list(lst):
    # Your code goes here
    reverseList = []
    for i in range(len(lst) -1, -1, -1):
        reverseList.append(lst[i])
    return reverseList

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(my_list)
    print(f"Reversed list: {reversed_list}")