# Code by @AmirMotefaker

# Print the Fibonacci sequence

# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
#
# The first two terms are 0 and 1. All other terms are obtained by adding
# the preceding two terms. This means to say the nth term is the sum of (n-1)th and (n-2)th term.

# Program to display the Fibonacci sequence up to n-th term

n_terms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if n_terms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif n_terms == 1:
   print("Fibonacci sequence upto",n_terms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < n_terms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
