# Code by AmirMotefaker

# Working with files - append

# # Solution 1
f = open('names.txt', 'a') # w: write, r: read, a:append

f.write('\nanother line')

# # Output(in files names.txt):
# # john
# # zahra
# # baran
# # ali
# # hamed
# # davidanother line
# # another line



# Solution 2 - with 
with open('names.txt', 'a') as names_file:
    names_file.write('\nThis is new')

# Output(in files names.txt):
# john
# zahra
# baran
# ali
# hamed
# davidanother line
# another line
# This is new
# This is new
