# Code by AmirMotefaker

# Working with files - name list

# # Solution 1
names_file = open('names.txt', 'r')

names = names_file.read()

names = names.split('\n')

print(names)

# # Output:
# # ['john', 'zahra', 'baran', 'ali', 'hamed', 'david']



# # Solution 2
names_file = open('names.txt', 'r')

names = names_file.read()

names = names.split('\n')

print(names)

while True:
    user_input = input('Enter name: ')
    if user_input == 'exit':
        break
    names.append(user_input)
    print(names)

# # Output:
# # ['john', 'zahra', 'baran', 'ali', 'hamed', 'david']
# # Enter name: hadi
# # ['john', 'zahra', 'baran', 'ali', 'hamed', 'david', 'hadi']
# # Enter name: amir
# # ['john', 'zahra', 'baran', 'ali', 'hamed', 'david', 'hadi', 'amir']
# # Enter name: exit



# # Solution 3 - reader
with open('names.txt', 'r') as reader:
    print(reader.read())
    print('in hear')

print('END')

# # Output:
# # john
# # zahra
# # baran
# # ali
# # hamed
# # david
# # in hear
# # END



# Solution 4 - with - reader.read()
names = []

with open('names.txt', 'r') as reader:
    for line in reader.read().split('\n'):
        names.append(line)
    print('in hear')

print(names)

print('END')

# Output:
# ['john', 'zahra', 'baran', 'ali', 'hamed', 'david']
# END
