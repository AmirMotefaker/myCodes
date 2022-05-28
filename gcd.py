# Code by @AmirMotefaker

# Find GCD of two numbers
# GCD: The greatest common divisor (GCD),
#  also called the greatest common factor,
#  of two numbers is the largest number that divides them both.

def gcd(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

print("The GCD is", gcd(num1, num2))

