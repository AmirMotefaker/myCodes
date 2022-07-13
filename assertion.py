# Code by @AmirMotefaker

# Assert Keyword - Assertion

# Solution 1
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

# Output:
# Enter your income: 100
# first 
# 200   
# second
