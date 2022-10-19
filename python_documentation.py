# Code by @AmirMotefaker

# Python Documentation
# https://docs.python.org/3/


my_list = [8,2,5,4,1,6]


my_list.reverse()
print(my_list)

# Output:
# [6, 1, 4, 5, 2, 8]


my_list.sort()
print(my_list)

# Output:
# [1, 2, 4, 5, 6, 8]


my_list.sort(reverse=True)
print(my_list)

# Output:
# [8, 6, 5, 4, 2, 1]



help(my_list.reverse)
# Output:
# Help on built-in function reverse:

# reverse() method of builtins.list instance
#     Reverse *IN PLACE*.
