# Code by @AmirMotefaker

# Working with files

# # Solution 1
# name = input('Enter your file name: ')

# open(f'{name}.txt', 'w') # w: write r: read

# # Output:
# # Enter your file name: info 
# # create file(info.txt)



# # Solution 2 - write
# f = open('names.txt', 'w')

# f.write('hello')


# # Output:
# # in file names.txt write hello



# # Solution 3 - write
# f = open('names.txt', 'w')

# f.write('x\n')
# f.write('y')
# f.write('\nz')

# # Output:
# # write in file names.txt:
# # x
# # y
# # z



# # Solution 4 - read
# f = open('names.txt', 'w')

# f.write('john\n')
# f.write('zahra')
# f.write('\nbaran')
# f.write('\nali')
# f.write('\nhamed')
# f.write('\ndavid')


# f = open('names.txt', 'r')

# a= f.read()

# print(type(a))
# print(a)


# # Output:
# # <class 'str'>
# # john
# # zahra
# # baran
# # ali
# # hamed
# # david



# # Solution 5 - .split
# f = open('names.txt', 'r')

# a = f.read()

# print(a.split('\n'))

# # Output:
# # ['john', 'zahra', 'baran', 'ali', 'hamed', 'david']


# # Solution 6 - .split
# f = open('names.txt', 'r')

# a = f.read()

# for line in a.split('\n'):
#     print(line)

# # Output:
# # john
# # zahra
# # baran
# # ali
# # hamed
# # david


# # Solution 7 - readlines()
# f = open('names.txt', 'r')

# a = f.readlines()

# print(a)

# # Output:
# # ['john\n', 'zahra\n', 'baran\n', 'ali\n', 'hamed\n', 'david']


# # Solution 8 - read and . split
# a = f.read()

# for name in a.split('\n'):
#     print(f'Hello {name.title()}')

# # Output:
# # Hello John
# # Hello Zahra
# # Hello Baran
# # Hello Ali
# # Hello Hamed
# # Hello David


# # Solution 9 - readline()
# f = open('names.txt', 'r')

# while True:
#     line = f.readline()
#     print(line) 
#     if line == '':
#         break

# print('END')

# # Output:
# # john

# # zahra

# # baran

# # ali

# # hamed

# # david

# # END



# # Solution 10 - readline() and readlines()
# f = open('names.txt', 'r')

# #print(f.readlines())

# while True:
#     line = f.readline()
#     print(line, end='') 
#     if line == '':
#         break

# print('END')

# # Output:
# # john
# # zahra
# # baran
# # ali
# # hamed
# # davidEND



# # Solution 11 - readline() and readlines()
# f = open('names.txt', 'r')

# print(f.readlines())

# while True:
#     line = f.readline()
#     print(line, end='') 
#     if line == '':
#         break

# print('END')

# # Output:
# # ['john\n', 'zahra\n', 'baran\n', 'ali\n', 'hamed\n', 'david']
# # END



# Solution 12 - readline()
f = open('names.txt', 'r')

while True:
    line = f.readline()
    if line == '':
        break

    print(line, end='')

print('END')

# Output:
# john
# zahra
# baran
# ali
# hamed
# davidEND
