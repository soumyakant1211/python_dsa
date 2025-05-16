def count_word_frequency(sentence):
    # Your code goes here
    frequncy = {}
    for word in sentence.split():
        if word in frequncy:
            frequncy[word] += 1
        else:
            frequncy[word] = 1
    return frequncy

# Test cases
print(count_word_frequency("hello world hello"))
print(count_word_frequency("hello world hello world"))