# Code by AmirMotefaker

# Get an unlimited number of inputs in the function

def sum_numbers(*args):
    result_sum = 0
    for n in args:
        result_sum += n

    return result_sum

print(sum_numbers(1,2,3,4,5,9))

# Output:
# 24


def sum_numbers(*args, **kwargs):  # Keyword Arguments
    # print(type(kwargs))
    # <class 'dict'>
    print(kwargs)
    print(args)
    print(kwargs.keys())
    print(kwargs.values())

sum_numbers(10, 1, 'hello', a='bye', b=10, c='night')

# Output:
# {'a': 'bye', 'b': 10, 'c': 'night'}
# (10, 1, 'hello')
# dict_keys(['a', 'b', 'c'])
# dict_values(['bye', 10, 'night'])
