# Code by @AmirMotefaker

# Number Guessing

import random

num = random.randint(0, 1000)
print(f'''
---------------------------
Correct answer: {num}
*************
***********
*********
*******
***** @AmirMotefaker
*******
*********
***********
*************
---------------------------
''')

attempt = 10
msg = ''
while attempt > 0:
   
    user_input = int(input('Enter Number: '))
    if user_input == num:
        msg = '**** You Won! ****'
        break
    elif user_input > num:
        print(f'{user_input} is greater.\nRemaining attempts: {attempt}.')
        attempt -= 1
        

    elif user_input < num:
        print(f'{user_input} is smaller.\nRemaining attempts: {attempt}.')
        attempt -= 1

    else:
        print('Something went wrong!')
        break
    
print(msg)

# Output:
# ---------------------------
# Correct answer: 955        
# *************
# ***********
# *********
# *******
# ***** @AmirMotefaker
# *******
# *********
# ***********
# *************
# ---------------------------

# Enter Number: 15
# 15 is smaller.
# Remaining attempts: 10.
# Enter Number: 28
# 28 is smaller.
# Remaining attempts: 9.
# Enter Number: 68
# 68 is smaller.
# Remaining attempts: 8.
# Enter Number: 98
# 98 is smaller.
# Remaining attempts: 7.
# Enter Number: 100
# 100 is smaller.
# Remaining attempts: 6.
# Enter Number: 800
# 800 is smaller.
# Remaining attempts: 5.
# Enter Number: 900
# 900 is smaller.
# Remaining attempts: 4.
# Enter Number: 990
# 990 is greater.
# Remaining attempts: 3.
# Enter Number: 970
# 970 is greater.
# Remaining attempts: 2.
# Enter Number: 956
# 956 is greater.
# Remaining attempts: 1.
