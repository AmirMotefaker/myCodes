# Code by @AmirMotefaker

# Raising Error Inheritance

class NegativeIncomeError(Exception):
    pass

def check_income(num):
    if num < 0:
        raise NegativeIncomeError

    return num

user_income = int(input('Enter your income: '))

check_income(user_income)

# Output:
# Enter your income: -10
# Traceback (most recent call last):
#   File "e:\A.Motefaker\ABC\Python\MyCode\raising_error_inheritance.py", line 16, in <module>
#     check_income(user_income)
#   File "e:\A.Motefaker\ABC\Python\MyCode\raising_error_inheritance.py", line 10, in check_income
#     raise NegativeIncomeError
# __main__.NegativeIncomeError

