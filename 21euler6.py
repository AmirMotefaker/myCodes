# Code by amotef@gmail.com

# projecteuler.net
# Problem 6

# Sum square difference
# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + .... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + 3 + .... + 10)**2 = 55*55 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_square_difference(n):
      return (((n**2) * (n + 1)**2) / 4) - (n * (n + 1) * (2*n + 1) / 6)
n = int(input("Enter Number: "))
print(sum_square_difference(n))
