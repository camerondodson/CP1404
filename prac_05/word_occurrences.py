"""Program to get a user input string and count how many times each word appears."""

input_string_dict = {}

# Get a user input and count how many times each word appears
input_string = input("Please enter the string you would like to analyze: ")
words_in_string = input_string.split()
for word in words_in_string:
    frequency_of_word = input_string_dict.get(word, 0)
    input_string_dict[word] = frequency_of_word + 1


words_in_string = list(input_string_dict.keys())
# Sort the words alphabetically
words_in_string.sort()

# Format the spacing to print evenly based off the longest word
longest_word = max(len(word) for word in words_in_string)
for word in words_in_string:
    print("{:{}} : {}".format(word, longest_word, input_string_dict[word]))
