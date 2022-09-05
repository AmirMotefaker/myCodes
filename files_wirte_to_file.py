# Code by @AmirMotefaker

# Working with files - write to files

# # Solution 1
f = open('words.txt', 'w')

f.write('123\n')
f.write('456\n')

f.writelines(['hello\n', 'hi'])

# # Output in words.txt:
# # 123
# # 456
# # hello
# # hi



# # Solution 2 - writelines - map - lambda
f = open('words.txt', 'w')

names = ['john', 'joe', 'david']

f.writelines(map(lambda name: name+'\n', names))

# # # Output in words.txt:
# # john
# # joe
# # david



# Solution 3 - write -  .join()
f = open('words.txt', 'w')

names = ['john', 'joe', 'david']

f.write('\n'.join(names))
# f.writelines(map(lambda name: name+'\n', names))

# # Output in words.txt:
# john
# joe
# david
