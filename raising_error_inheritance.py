# Code by AmirMotefaker

# Raising Error Inheritance

# # Solution 1
class NegativeIncomeError(Exception):
    pass

def check_income(num):
    if num < 0:
        raise NegativeIncomeError

    return num

user_income = int(input('Enter your income: '))

check_income(user_income)

# # Output:
# # Enter your income: -10
# # Traceback (most recent call last):
# #   File "e:\A.Motefaker\ABC\Python\MyCode\raising_error_inheritance.py", line 16, in <module>
# #     check_income(user_income)
# #   File "e:\A.Motefaker\ABC\Python\MyCode\raising_error_inheritance.py", line 10, in check_income
# #     raise NegativeIncomeError
# # __main__.NegativeIncomeError



# # Solution 2
class NegativeIncomeError(Exception):
    pass

class NegativeAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise NegativeAgeError('Your age con not be Negative.')

    return age * 2


def check_income(num):
    if num < 0:
        raise NegativeIncomeError

    return num

#user_income = int(input('Enter your income: '))
user_age = int(input('Enter your age: '))

check_income(user_age)

# # Output:
# # Enter your age: -10
# # Traceback (most recent call last):
# #   File "e:\A.Motefaker\ABC\Python\MyCode\raising_error_inheritance.py", line 53, in <module>
# #     check_income(user_age)
# #   File "e:\A.Motefaker\ABC\Python\MyCode\raising_error_inheritance.py", line 46, in check_income
# #     raise NegativeIncomeError
# # __main__.NegativeIncomeError



# Solution 3
class NegativeIncomeError(Exception):
    pass

class NegativeAgeError(Exception):
    def __init__(self, message, age):
        self.message = message
        self.age = age

def check_age(age):
    if age < 0:
        raise NegativeAgeError(f'Your age ({age}) con not be Negative.', age)

    return age * 2


def check_income(num):
    if num < 0:
        raise NegativeIncomeError

    return num

#user_income = int(input('Enter your income: '))
user_age = int(input('Enter your age: '))

try:
    check_age(user_age)
except NegativeAgeError as e:
    print(e.message, e.age)

# Output:
# Enter your age: -10
# Your age (-10) con not be Negative. -10
