# Code by @AmirMotefaker

# Map

## Standard
my_nums = [1,2,3,4,5,6]

def power_two(num):
    return num ** 2

for num in my_nums:
    print(power_two(num))

# Output:
# 1
# 4 
# 9 
# 16
# 25
# 36


## Map
my_nums = [1,2,3,4,5,6]

def power_two(num):
    return num ** 2

for item in map(power_two, my_nums):
    print(item)

# Output:
# 1
# 4 
# 9 
# 16
# 25
# 36


## Map2 - List
my_nums = [1,2,3,4,5,6]

def power_two(num):
    return num ** 2

print(list(map(power_two, my_nums)))

# Output:
# [1, 4, 9, 16, 25, 36]



## Map3 - List
numbers = [5,6,20]

def plus_one(num):
    return num + 1

print(list(map(plus_one, numbers)))

# Output:
# [6, 7, 21]


## names
names = ['ali alavi', 'ana johnson', 'baran barani']

def extract_name(full_name):
    return full_name.split()[0]

print(extract_name(names[0]))


# Output:
# ali



## Map 4 - extract first name
names = ['ali alavi', 'ana johnson', 'baran barani']

def extract_name(full_name):
    return full_name.split()[0]

print(list(map(extract_name, names)))


# Output:
# ['ali', 'ana', 'baran']
