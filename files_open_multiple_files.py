# Code by @AmirMotefaker

# Working with files - Open multiple files simultaneously

# # Solution 1
# file_text = None

# with open('grades.txt', 'r') as reader:
#     file_text = reader.read()

# with open('hello.txt', 'w') as writer:
#     writer.write(file_text)


# # Output( create file hello.txt with this items):
# # sara 18
# # ali 17
# # david 19
# # hadi 12
# # amir 20
# # setareh 20
# # Sahar 11
# # Delsa 17



# Solution 2
file_text = None

with open('grades.txt', 'r') as reader, open('hello.txt', 'w') as writer:
    writer.write(reader.read())


# Output(grade.txt and hello.txt):
# sara 18
# ali 17
# david 19
# hadi 12
# amir 20
# setareh 20
# Sahar 11
# Delsa 17
