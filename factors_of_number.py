# Code by @AmirMotefaker

# Find the Factors of a Number

def factors_number(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("Enter number: "))

factors_number(num)

# Output:
# Enter number: 18
# The factors of 18 are:
# 1
# 2
# 3
# 6
# 9
# 18
