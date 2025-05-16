# Maximum difference between two consecutive elements in a list.

def max_consecutive_difference(lst):
    # Your code goes here
    if len(lst) < 2:
        return 0
    maxDifference = 0
    for i in range(len(lst)-1):
        currentDifference = abs(lst[i] - lst[i + 1])
        if currentDifference > maxDifference:
            maxDifference = currentDifference
    return maxDifference

# Test cases
print(max_consecutive_difference([1, 2, 3, 4, 5]))
print(max_consecutive_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))