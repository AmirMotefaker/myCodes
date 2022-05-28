# Code by @AmirMotefaker

# Find the Sum of Natural Numbers


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
  
