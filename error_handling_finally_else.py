# Code by @AmirMotefaker

# Handling Exceptions - finally - else

a = 10
b = int(input('Enter a number: '))

try:
    print( a / b)
except ZeroDivisionError:
    print('EXCEPTION')


# Output:
# Enter a number: 0
# EXCEPTION
