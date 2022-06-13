# Code by @AmirMotefaker

# Delete an Element From a Dictionary


# Solution 1  -Using del keyword
my_dict = {31: 'a', 21: 'b', 14: 'c'}

del my_dict[31]

print(my_dict)

# output:
# {21: 'b', 14: 'c'}


# Solution 2 - Using pop()
my_dict = {31: 'a', 21: 'b', 14: 'c'}

print(my_dict.pop(31))

print(my_dict)

# output:
# a
# {21: 'b', 14: 'c'}
