# Code by @AmMotefaker

# Assert Keyword - Assertion

# # Solution 1
def calc_income(income):
    # if income < 0:
    #     raise Exception('Income should not be a negative number!')

    assert income>=0, 'Income should not be a negative number!'

    print('first')    
    return income * 2

user_income = int(input('Enter your income: '))

try:
    print(calc_income(user_income))
except:
    print('EXCEPTION')

print('second')

# # Output:
# # Enter your income: 100
# # first 
# # 200   
# # second



# # Solution 2
def calc_income(income):
    # if income < 0:
    #     raise Exception('Income should not be a negative number!')

    assert income>=0, 'Income should not be a negative number!'

    print('first')    
    return income * 2

user_income = int(input('Enter your income: '))

#try:
print(calc_income(user_income))
#except:
#     print('EXCEPTION')

# print('second')

# # Output:
# # Enter your income: -10
# # Traceback (most recent call last):
# #   File "e:\A.Motefaker\ABC\Python\MyCode\assertion.py", line 45, in <module>
# #     print(calc_income(user_income))
# #   File "e:\A.Motefaker\ABC\Python\MyCode\assertion.py", line 37, in calc_income
# #     assert income>=0, 'Income should not be a negative number!'
# # AssertionError: Income should not be a negative number!



# Solution 3
def square(x):
    assert x>=0, 'Only positive numbers are allowed'
    return x*x

try:
    square(-2)
except AssertionError as msg:
    print(msg)

# Output:
# Only positive numbers are allowed
