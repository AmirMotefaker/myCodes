# Code by @AmirMotefaker

# Working with files - Relative Path

with open('grades.txt', 'r') as reader:
    print(reader.read())

with open('student/grades.txt', 'r') as reader:
    print(reader.read())


# Relative Path
with open('../grades.txt', 'r') as reader:
    print(reader.read())
