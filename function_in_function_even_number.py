# Code by AmirMotefaker

# Function in Function Even Number

def is_even(num):
    if num % 2 == 0:
        return True
    return False


def return_all_even_numbers_in_list(num_list):
    result = []

    for num in num_list:
        if is_even(num):
            result.append(num)

    return(result)


print(return_all_even_numbers_in_list([1,2,3,4,6,-123,8,3,13,122,11,29,-2]))

# Output:
# [2, 4, 6, 8, 122, -2]
