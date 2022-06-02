# Code by @AmirMotefaker

# Catch Multiple Exceptions in One Line

# Multiple exceptions can be caught using a tuple.

string = input("Enter :")

try:
    num = int(input())
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)
