# Code by @AmirMotefaker

# Convert Decimal to Binary Using Recursion

def convert_to_binary(n):
   if n > 1:
       convert_to_binary(n//2)
   print(n % 2,end = '')

# decimal number
dec = int(input("Enter decimal number: "))

convert_to_binary(dec)
print()
