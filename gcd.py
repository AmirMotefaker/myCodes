# Code by @AmirMotefaker

# Find GCD of two numbers

# GCD: The greatest common divisor (GCD),
# also called the greatest common factor,
# of two numbers is the largest number that divides them both.

# Example: Find the greatest common divisor of 13 and 48.
# Solution: We will use the below steps to determine the greatest common divisor of (13, 48).

# Divisors of 13 are 1, and 13.
# Divisors of 48 are 1, 2, 3, 4, 6, 8, 12, 16, 24 and 48.

# The common divisor of 13 and 48 is 1.
# The greatest common divisor of 13 and 48 is 1.

# Thus, GCD(13, 48) = 1.

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

# Output:
# Enter number1: 12
# Enter number2: 64
# The GCD is 4
