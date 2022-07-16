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



# Solution 4 - read
f = open('names.txt', 'w')

f.write('john\n')
f.write('zahra')
f.write('\nbaran')
f.write('\nali')
f.write('\nhamed')
f.write('\ndavid')


f = open('names.txt', 'r')

a= f.read()

print(type(a))
print(a)


# Output:
# <class 'str'>
# john
# zahra
# baran
# ali
# hamed
# david
