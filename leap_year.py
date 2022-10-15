# Code by @AmirMotefaker

# Check Leap Year

# https://en.wikipedia.org/wiki/Leap_year

# To determine whether a year is a leap year, follow these steps:
# 1- If the year is evenly divisible by 4, go to step 2. ...
# 2- If the year is evenly divisible by 100, go to step 3. ...
# 3- If the year is evenly divisible by 400, go to step 4. ...
# 4- The year is a leap year (it has 366 days).
# 5- The year is not a leap year (it has 365 days).

# Python program to check if year is a leap year or not

year = int(input("Enter a number: "))

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))

# Output
# Enter a number: 2022
# 2022 is not a leap year

# Enter a number: 2021
# 2021 is not a leap year

# Enter a number: 2024
# 2024 is a leap year

# Enter a number: 1979
# 1979 is not a leap year
