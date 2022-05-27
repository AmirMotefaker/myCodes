# Code by @AmirMotefaker

# Compute the Power of a Number

# Solution 1: Calculate power of a number using a while loop

# base = 3
# exponent = 4
#
# result = 1
#
# while exponent != 0:
#     result *= base
#     exponent-=1
#
# print("Answer = " + str(result))



# Solution 2: Calculate power of a number using a for loop

# base = 3
# exponent = 4

# result = 1

# for exponent in range(exponent, 0, -1):
#     result *= base

# print("Answer = " + str(result))



# Solution 3: Calculate the power of a number using pow() function

base = 3
exponent = -4

result = pow(base, exponent)

print("Answer = " + str(result))
