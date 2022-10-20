# Code by AmirMotefaker

# Reverse a Number

# Solution 1: Reverse a Number using a while loop

# 1- the remainder of the num divided by 10 is stored in the variable digit.
#   Now, the digit contains the last digit of num, i.e. 4.
#   digit is then added to the variable reversed after multiplying it by 10.
#   Multiplication by 10 adds a new place in the reversed number.
#   One-th place multiplied by 10 gives you tenth place, tenth gives you hundredth,
#   and so on. In this case, reversed_num contains 0 * 10 + 4 = 4.
#   num is then divided by 10 so that now it only contains the first three digits: 123.
# 2- After second iteration, digit equals 3, reversed equals 4 * 10 + 3 = 43 and num = 12.
# 3- After third iteration, digit equals 2, reversed equals 43 * 10 + 2 = 432 and num = 1.
# 4- After fourth iteration, digit equals 1, reversed equals 432 * 10 + 1 = 4321 and num = 0.
# 5- Now num = 0, so the test expression num != 0 fails and while loop exits. reversed already contains the reversed number 4321.

num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

# print("Reversed Number: " + str(reversed_num))


# Output:
# Reversed Number: 4321



# Solution 2: Reverse a Number Using String slicing

num = 123456789
print(str(num)[::-1])

# Output:
# 987654321
