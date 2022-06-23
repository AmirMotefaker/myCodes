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



# Solution 2 - Using itertools 
import itertools

list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c']

# loop until the short loop stops
for i,j in zip(list_1,list_2):
    print(i,j)

print("\n")

# loop until the longer list stops
for i,j in itertools.zip_longest(list_1,list_2):
    print(i,j)


# Output:
# 1 a
# 2 b
# 3 c


# 1 a
# 2 b
# 3 c
# 4 None
