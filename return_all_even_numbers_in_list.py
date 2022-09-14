# Code by AmirMotefaker

# Return all even numbers in list

def return_all_even_numbers_in_list(num_list):
    result = []

    for num in num_list:
        if num % 2 == 0:
            result.append(num)


    return(result)

print(return_all_even_numbers_in_list([1,2,3,4,6,8,3,13,122,11,29]))

# Output:
# [2, 4, 6, 8, 122]

