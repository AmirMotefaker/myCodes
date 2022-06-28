# Code by @AmirMotefaker

# Recursive Functions


def add_rec(a):
   print(a)
   if a < 5:
      return add_rec(a+1)
   return a

add_rec(1)

# Output:
# 1
# 2
# 3
# 4
# 5
