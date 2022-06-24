# Code by @AmirMotefaker

# Find Longest String in List - Tuples Unpacking

def find_longest_str_in_list(list_of_str):
    final_result = ''

    for my_str in list_of_str:
        if len(my_str) >= len(final_result):
            final_result = my_str

    return final_result, len(final_result)


my_list = ['hello', 'hi', 'salam', 'programming', 'computer', 
           'python', 'hacker', 'python developer']

max_str, max_str_length, = find_longest_str_in_list(my_list)

print(max_str, max_str_length)


# Output:
# python developer 16
