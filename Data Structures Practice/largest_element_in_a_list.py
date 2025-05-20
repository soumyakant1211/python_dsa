def find_largest(numbers):
    # Your code goes here
    # return max(numbers)
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

# Example usage
if __name__ == "__main__":
    numbers = [3, 5, 7, 2, 8]
    largest_number = find_largest(numbers)
    print(f"The largest number in the list is: {largest_number}")