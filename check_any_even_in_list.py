# Code by @AmirMotefaker

# Check any even in list

# [1,2,3,4] -> True
# [1,3,5,7,9] -> False

def check_any_even_in_list(list_of_numbers):

    for num in list_of_numbers:
        if num % 2 == 0:
            return True
           
    return False


print(check_any_even_in_list([1,13,11,17,19,4]))

# Output:
# True
