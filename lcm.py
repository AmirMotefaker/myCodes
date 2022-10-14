# Code by AmirMotefaker

# Find LCM

# The Least Common Multiple (LCM) is also referred to as the
# Lowest Common Multiple (LCM) and Least Common Divisor (LCD). 
# For two integers a and b, denoted LCM(a,b), 
# the LCM is the smallest positive integer that is evenly divisible by both a and b.

# For example, LCM(2,3) = 6 and LCM(6,10) = 30.


def lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

print("The L.C.M. is", lcm(num1, num2))

# Output:
# Enter number1: 2
# Enter number2: 3
# The L.C.M. is 6

# Enter number1: 2
# Enter number2: 3
# The L.C.M. is 6
