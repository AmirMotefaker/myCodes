# Code by @AmirMotefaker

# Get an unlimited number of inputs in the function

def sum_numbers(*args):
    result_sum = 0
    for n in args:
        result_sum += n

    return result_sum

print(sum_numbers(1,2,3,4,5,9))

# Output:
# 24

