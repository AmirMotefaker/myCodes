# Code by @AmirMotefaker

# Find Factorial of Number Using Recursion

# # Solution 1 
# def factorial_recursion(n):
#    if n == 1:
#        return n
#    else:
#        return n*factorial_recursion(n-1)

# num = int(input("Enter number: "))

# # check if the number is negative
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of", num, "is", factorial_recursion(num))

# # Output:
# # Enter number: 8
# # The factorial of 8 is 40320



# # # Solution 2 - CodingYar
# 9! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9
# 8! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8

# 9! = (factorial(7) * 8) * 9

def factorial_rec(n):
   print(n)
   if n == 1:
      return n
   else:
      return n * factorial_rec(n-1)

print(factorial_rec(5))

# Output:
# 5
# 4
# 3
# 2
# 1
# 120
