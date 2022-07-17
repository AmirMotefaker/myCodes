# Code by @AmirMotefaker

# Working with files - Storage of grades and GPA

# # Solution 1
# print('--- Current grades: ---')

# with open('grades.txt', 'r') as reader:
#     all_data = reader.read()
#     print(all_data)

# # Output:
# # --- Current grades: ---
# # sara 18 
# # ali 17  
# # david 19



# # Solution 2
print('--- Current grades: ---')

with open('grades.txt', 'r') as reader:
    all_data = reader.read()
    print(all_data)

# Output:
# --- Current grades: ---
# sara 18 
# ali 17  
# david 19



# # Solution 3
# print('--- Current grades: ---')

# with open('grades.txt', 'r') as reader:
#     all_data = reader.read()
#     print(all_data)


# new_grades = []

# yes_no_new_grades = input('Do you want to add new grades? ')

# if yes_no_new_grades == 'yes':
#     while True:
#         name = input('Enter name: ')
        
#         if name == 'exit':
#             break

#         grade = input('Enter grade: ')
#         new_grades.append({
#             'name': name,
#             'grade': grade
#         })

# with open('grades.txt', 'a') as grades_file:
#     for student_grade in new_grades:
#         grades_file.write(f"\n{student_grade['name']} {student_grade['grade']}")

# # Output
# # --- Current grades: ---
# # sara 18
# # ali 17
# # david 19
# # Do you want to add new grades? yes
# # Enter name: hadi
# # Enter grade: 12
# # Enter name: amir
# # Enter grade: 20
# # Enter name: exit



# # Solution 4
# new_grades = []

# yes_no_new_grades = input('Do you want to add new grades? ')

# if yes_no_new_grades == 'yes':
#     while True:
#         name = input('Enter name: ')
        
#         if name == 'exit':
#             break

#         grade = input('Enter grade: ')
#         new_grades.append({
#             'name': name,
#             'grade': grade
#         })

# with open('grades.txt', 'a') as grades_file:
#     for student_grade in new_grades:
#         grades_file.write(f"\n{student_grade['name']} {student_grade['grade']}")


# all_students_grades =[]
# with open('grades.txt', 'r') as reader:
#     all_data = reader.read()
#     for line in all_data.split('\n'):
#         x = line.split(' ')
#         grade = x[1]
#         all_students_grades.append(grade)

# print(all_students_grades)

# # Output:
# # --- Current grades: ---
# # sara 18
# # ali 17
# # david 19
# # hadi 12
# # amir 20
# # Do you want to add new grades? no
# # ['18', '17', '19', '12', '20']



# # Solution 5 - .append(int(grade))
# new_grades = []

# yes_no_new_grades = input('Do you want to add new grades? ')

# if yes_no_new_grades == 'yes':
#     while True:
#         name = input('Enter name: ')
        
#         if name == 'exit':
#             break

#         grade = input('Enter grade: ')
#         new_grades.append({
#             'name': name,
#             'grade': grade
#         })

# with open('grades.txt', 'a') as grades_file:
#     for student_grade in new_grades:
#         grades_file.write(f"\n{student_grade['name']} {student_grade['grade']}")


# all_students_grades =[]
# with open('grades.txt', 'r') as reader:
#     all_data = reader.read()
#     for line in all_data.split('\n'):
#         x = line.split(' ')
#         grade = x[1]
#         all_students_grades.append(int(grade))

# print(all_students_grades)

# # Output:
# # --- Current grades: ---
# # sara 18
# # ali 17
# # david 19
# # hadi 12
# # amir 20
# # Do you want to add new grades? no
# # [18, 17, 19, 12, 20]



# # Solution 6 - SUM and AVERAGE
# new_grades = []

# yes_no_new_grades = input('Do you want to add new grades? ')

# if yes_no_new_grades == 'yes':
#     while True:
#         name = input('Enter name: ')
        
#         if name == 'exit':
#             break

#         grade = input('Enter grade: ')
#         new_grades.append({
#             'name': name,
#             'grade': grade
#         })

# with open('grades.txt', 'a') as grades_file:
#     for student_grade in new_grades:
#         grades_file.write(f"\n{student_grade['name']} {student_grade['grade']}")


# all_students_grades =[]
# with open('grades.txt', 'r') as reader:
#     all_data = reader.read()
#     for line in all_data.split('\n'):
#         x = line.split(' ')
#         grade = x[1]
#         all_students_grades.append(int(grade))

# print(all_students_grades)

# print(sum(all_students_grades)/len(all_students_grades))

# # Output:
# # --- Current grades: ---
# # sara 18
# # ali 17
# # david 19
# # hadi 12
# # amir 20
# # setareh 20
# # Do you want to add new grades? no
# # [18, 17, 19, 12, 20, 20]
# # 17.666666666666668



# Solution 7 - SUM and AVERAGE
new_grades = []

yes_no_new_grades = input('Do you want to add new grades? ')

if yes_no_new_grades == 'yes':
    while True:
        name = input('Enter name: ')
        
        if name == 'exit':
            break

        grade = input('Enter grade: ')
        new_grades.append({
            'name': name,
            'grade': grade
        })

with open('grades.txt', 'a') as grades_file:
    for student_grade in new_grades:
        grades_file.write(f"\n{student_grade['name']} {student_grade['grade']}")


all_students_grades =[]
with open('grades.txt', 'r') as reader:
    all_data = reader.read()
    for line in all_data.split('\n'):
        grade = line.split(' ')[1]
        all_students_grades.append(int(grade))

print(all_students_grades)

print(sum(all_students_grades)/len(all_students_grades))

# Output:
# --- Current grades: ---
# sara 18
# ali 17
# david 19
# hadi 12
# amir 20
# setareh 20
# Sahar 11
# Delsa 17
# Do you want to add new grades? no
# [18, 17, 19, 12, 20, 20, 11, 17]
# 16.75
   
