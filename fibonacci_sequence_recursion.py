# Code by @AmirMotefaker

# Display Fibonacci Sequence Using Recursion

def fib_recursion(n):
   if n <= 1:
       return n
   else:
       return(fib_recursion(n-1) + fib_recursion(n-2))

terms = int(input("Enter terms: "))

# check if the number of terms is valid
if terms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(terms):
       print(fib_recursion(i))
  
# Output:
# Enter terms: 11
# Fibonacci sequence:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
 
