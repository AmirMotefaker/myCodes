# Code by AmirMotefaker

# The average string length for user input

def get_inputs():
    user_input = input('Enter a word: ')

    list_of_words = []

    while user_input != 'done':
        list_of_words.append(user_input)

        user_input = input('Enter another word: ')

    return list_of_words

def get_strings_avg(list_of_strs):
    count_letters = 0

    for word in list_of_strs:
        count_letters += len(word)

    return count_letters / len(list_of_strs)


user_inputs = get_inputs()

print(get_strings_avg(user_inputs))

# Output:
# Enter a word: a
# Enter another word: ab
# Enter another word: abc
# Enter another word: abcd
# Enter another word: qwert
# Enter another word: done
# 3.0
