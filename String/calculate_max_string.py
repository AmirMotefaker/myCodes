# Code by AmirMotefaker

# Calculate Max String

# # Solution 1
def calc_max_string(*args):
    max_string = args[0]

    for string in args:
        if len(string) > len(max_string):
            max_string = string

    return len(max_string), max_string


print(calc_max_string('a', 'hello', 'yesterday', 'day'))

# # Output:
# # (9, 'yesterday')



# Solution 2
def calc_max_string(*args):
    max_string = args[0]

    for string in args:
        if len(string) > len(max_string):
            max_string = string

    return len(max_string), max_string


max_string_len, max_string = calc_max_string('a', 'hello', 'yesterday', 'day')

print(f'max length: {max_string_len}, string: {max_string}')

# Output:
# max length: 9, string: yesterday
