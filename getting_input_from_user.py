# Code by @AmirMotefaker

# Getting Input From User

# # Solution 1
user_input = input("Enter your number:  ")

print(int(user_input))

# # Output:
# # Enter your number:  12
# # 12

# # Enter your number:  12.1
# # Traceback (most recent call last):
# #   File "e:\A.Motefaker\ABC\Python\MyCode\getting_input_from_user.py", line 7, in <module>
# #     print(int(user_input))
# # ValueError: invalid literal for int() with base 10: '12.1'


# # Solution 2
user_input = input("Enter your number:  ")

print(float(user_input))

# # Output:
# # Enter your number:  12.1
# # 12.1

# # Enter your number:  12
# # 12.0

# # Enter your number:  hello
# # Traceback (most recent call last):
# #   File "e:\A.Motefaker\ABC\Python\MyCode\getting_input_from_user.py", line 24, in <module>
# #     print(float(user_input))
# # ValueError: could not convert string to float: 'hello'



# # Solution 3
user_input = input("Enter your number:  ")

result = int(user_input)

# # Output:
# # Enter your number:  13.1
# # Traceback (most recent call last):
# #   File "e:\A.Motefaker\ABC\Python\MyCode\getting_input_from_user.py", line 44, in <module>
# #     result = int(user_input)
# # ValueError: invalid literal for int() with base 10: '13.1'



# # Solution 4
user_input = input("Enter your number:  ")
result = None

try:
    result = int(user_input)
except ValueError:
    print('Not an integer')

print(f'Result: {result}')

# # Output:
# # Enter your number:  12.1
# # Not an integer
# # Result: None



# # Solution 5
user_input = input("Enter your number:  ")
result = None

try:
    result = int(user_input)
except ValueError:
    result = float(user_input)

print(f'Result: {result}')

# # Output:
# # Enter your number:  12
# # Result: 12

# # Enter your number:  12.1
# # Result: 12.1

# # Enter your number:  123a
# # Traceback (most recent call last):
# #   File "e:\A.Motefaker\ABC\Python\MyCode\getting_input_from_user.py", line 78, in <module>
# #     result = int(user_input)
# # ValueError: invalid literal for int() with base 10: '123a'

# # During handling of the above exception, another exception occurred:

# # Traceback (most recent call last):
# #   File "e:\A.Motefaker\ABC\Python\MyCode\getting_input_from_user.py", line 80, in <module>
# #     result = float(user_input)
# # ValueError: could not convert string to float: '123a'



# # Solution 6
user_input = input("Enter your number:  ")
result = None

try:
    result = int(user_input)
except ValueError:
    try:
        result = float(user_input)
    except ValueError:
        print('You have to enter a number.')

print(type(result))
print(f'Result: {result}')

# # Output:
# # Enter your number:  12
# # <class 'int'>
# # Result: 12 

# # Enter your number:  12.1
# # <class 'float'>
# # Result: 12.1

# # Enter your number:  dsadsa1
# # You have to enter a number.
# # <class 'NoneType'>
# # Result: None



# Solution 7
result = None

while True:
    user_input = input("Enter your number:  ")
    
    try:
        result = int(user_input)
        break
    except ValueError:
        try:
            result = float(user_input)
            break
        except ValueError:
            print('You have to enter a number. Please try again.')

print(type(result))
print(f'Result: {result}')

# Output:
# Enter your number:  hello
# You have to enter a number. Please try again.
# Enter your number:  123a
# You have to enter a number. Please try again.
# Enter your number:
# You have to enter a number. Please try again.
# Enter your number:  123.2
# <class 'float'>
# Result: 123.2
