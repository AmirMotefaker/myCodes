# Code by @AmirMotefaker

# Iterate Through Two Lists in Parallel

# Solution 1 - Using zip
list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c']

for i, j in zip(list_1, list_2):
    print(i, j)

# Output:
# 1 a
# 2 b
# 3 c

