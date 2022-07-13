# Code by @AmirMotefaker

# Raise Exception

# Solution 1
def calc_income(income):
    if income < 0:
        raise Exception('Income should not be a negative number!')
        
    return income * 2

user_income = int(input('Enter your income: '))
print(calc_income(user_income))


# Output:
# Enter your income: -100
# Traceback (most recent call last):
#   File "e:\A.Motefaker\ABC\Python\MyCode\raise_exception.py", line 12, in <module>
#     print(calc_income(user_income))
#   File "e:\A.Motefaker\ABC\Python\MyCode\raise_exception.py", line 7, in calc_income
#     raise Exception('Income should not be a negative number!')
# Exception: Income should not be a negative number!
