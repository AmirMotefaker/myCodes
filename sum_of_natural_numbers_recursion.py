# Code by AmirMotefaker

# Find the Sum of Natural Numbers Using Recursion

def sum_recursion(n):
   if n <= 1:
       return n
   else:
       return n + sum_recursion(n-1)

num = int(input("Enter number: "))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",sum_recursion(num))
   
# Output:
# Enter number: 17
# The sum is 153

# Enter number: -83
# Enter a positive number
