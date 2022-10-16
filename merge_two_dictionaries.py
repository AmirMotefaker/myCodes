# Code by AmirMotefaker

# Merge Two Dictionaries

# # Solution 1 - Using the | Operator

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)

# # Output:
# # {1: 'a', 2: 'c', 4: 'd'}


# # # Solution 2 - Using the ** Operator

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print({**dict_1, **dict_2})

# # Output:
# # {1: 'a', 2: 'c', 4: 'd'}


# # Solution 3 - Using copy() and update()

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

dict_3 = dict_2.copy()
dict_3.update(dict_1)

print(dict_3)

# Output:
# {2: 'b', 4: 'd', 1: 'a'}
