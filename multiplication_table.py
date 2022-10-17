# Code by @AmirMotefaker

# Display the multiplication Table

# Multiplication table (from 1 to 10) in Python


# Solution 1 
num = 13
# # To take input from the user
# # num = int(input("Display multiplication table of? "))

# # Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

# Output:
# 13 x 1 = 13
# 13 x 2 = 26
# 13 x 3 = 39
# 13 x 4 = 52
# 13 x 5 = 65
# 13 x 6 = 78
# 13 x 7 = 91
# 13 x 8 = 104
# 13 x 9 = 117
# 13 x 10 = 130



# Solution 2 - CodingYar
for i in range(1, 10):
   print()
   for j in range(1, 10):
      print(f'{i*j:3}', end=' ')

# Output:
#   1   2   3   4   5   6   7   8   9 
#   2   4   6   8  10  12  14  16  18 
#   3   6   9  12  15  18  21  24  27 
#   4   8  12  16  20  24  28  32  36 
#   5  10  15  20  25  30  35  40  45 
#   6  12  18  24  30  36  42  48  54 
#   7  14  21  28  35  42  49  56  63 
#   8  16  24  32  40  48  56  64  72
#   9  18  27  36  45  54  63  72  81
