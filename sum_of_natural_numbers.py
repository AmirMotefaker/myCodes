# Code by @AmirMotefaker

# Find the Sum of Natural Numbers

# We could have solved the above problem without using a loop
# by using the following formula:
#     n*(n+1)/2
# For example, if n = 16, the sum would be (16*17)/2 = 136.

num = int(input("Enter number: "))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
   
 
