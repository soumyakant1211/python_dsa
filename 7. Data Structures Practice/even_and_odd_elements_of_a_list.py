def count_even_odd(lst):
    # Your code goes here
    evenCount = 0
    oddCount = 0
    for number in lst:
        if number % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    return (evenCount, oddCount)
    
# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    even_count, odd_count = count_even_odd(my_list)
    print(f"Even count: {even_count}, Odd count: {odd_count}")