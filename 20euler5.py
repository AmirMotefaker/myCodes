# Code by amotef@gmail.com

# projecteuler.net
# Problem 5

# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# LCM: the lowest multiple shared by two or more numbers.
# example: common multiples of 4 and 6 are 12, 24 and 36, 
# but the lowest of those is 12; therefore, 
# the lowest common multiple of 4 and 6 is 12.


from math import gcd  # gcd: Return the greatest common divisor of the specified integer arguments.
from functools import reduce  # reduce: Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.
def LCM(a, b):  # LCM: Return the least common multiple of the specified integer arguments.
    return a // gcd(a, b) * b  
N = int(input("The LCM for numbers 1 through "))
print ("is", reduce(LCM, range(N//2+1, N+1)))