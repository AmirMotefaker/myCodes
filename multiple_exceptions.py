# Code by AmirMotefaker

# Catch Multiple Exceptions in One Line

# Multiple exceptions can be caught using a tuple.

from re import A


string = input("Enter :")

try:
    num = int(input())
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)


# Input:
# a
# 2
# Output:
# can only concatenate str (not "int") to str

# Input:
# a
# b
# Output:
# invalid literal for int() with base 10: 'b'
