# Code by AmirMotefaker

# zip() Function

# The zip() function returns a zip object, which is an iterator of
# Tuples where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together etc.

names = ['ana', 'arvin', 'sara']
marks = [18, 19, 20]

for item in zip(names,marks):
    print(item)

# Output:
# ('ana', 18)
# ('arvin', 19)
# ('sara', 20)



names = ['ana', 'arvin', 'sara']
marks = [18, 19, 20]

for name,mark in zip(names,marks):
    print(f'name = {name}, mark = {mark}')


# Output:
# name = ana, mark = 18
# name = arvin, mark = 19
# name = sara, mark = 20



names = ['ana', 'arvin', 'sara']
marks = [18, 19, 20]
ages = [19, 20 , 21]

for name,mark,age in zip(names,marks,ages):
    print(f'name = {name}, mark = {mark}, age = {age}')


# Output:
# name = ana, mark = 18, age = 19
# name = arvin, mark = 19, age = 20
# name = sara, mark = 20, age = 21
