# Code by @AmirMotefaker

# enumerate() Function

# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.

names = ['ana', 'arvin', 'sara']

for item in enumerate(names):
    print(item)

# Output:
# (0, 'ana')
# (1, 'arvin')
# (2, 'sara') 



names = ['ana', 'arvin', 'sara']

for index, name in enumerate(names):
    print(f'{index}: {name}')

# Output:
# 0: ana
# 1: arvin
# 2: sara


names = ['ana', 'arvin', 'sara']
marks = [18, 19, 20]
ages = [19, 20, 21]

index = 0

for name in names:
    print(f'name = {name}, mark = {marks[index]}, age = {ages[index]}')
    index += 1

# Output:
# name = ana, mark = 18, age = 19
# name = arvin, mark = 19, age = 20
# name = sara, mark = 20, age = 21



names = ['ana', 'arvin', 'sara']
marks = [18, 19, 20]
ages = [19, 20, 21]

for index, name in enumerate(names):
    print(f'name = {name}, mark = {marks[index]}, age = {ages[index]}')

# Output:
# name = ana, mark = 18, age = 19
# name = arvin, mark = 19, age = 20
# name = sara, mark = 20, age = 21
