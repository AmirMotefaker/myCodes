# Code by @AmirMotefaker

# Working with files - Open the file and write in it

# # Solution 1
with open('grades.txt', 'r') as reader:
    for line in list(reader):
        print(line, end='')


# # Output:
# # sara 18
# # ali 17
# # david 19
# # hadi 12
# # amir 20
# # setareh 20
# # Sahar 11
# # Delsa 17



# Solution 2
with open('grades.txt', 'r') as reader:
    for line in reader:
        print(line, end='')

# Output:
# sara 18
# ali 17
# david 19
# hadi 12
# amir 20
# setareh 20
# Sahar 11
Delsa 17
