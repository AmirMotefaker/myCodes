# Code b @AmirMotefaker

# OOP - Inheritance 

# # Solution 1
# class Student:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def who_am_i(self):
#         return f'{self.firstname} {self.lastname}'


# john_stu = Student('john', 'doe')
# david_stu = Student('david', 'stuart')

# print(john_stu.who_am_i())
# print(david_stu.who_am_i())

# # Output:
# # john doe
# # david stuart



# # Solution 2
# class Student:
#     def __init__(self, firstname, lastname, major, uni):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.major = major
#         self.university = uni

#     def who_am_i(self):
#         return f'{self.firstname} {self.lastname}'

# class Teacher:
#     def __init__(self, firstname, lastname, department, uni):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.department = department
#         self.university = uni

#     def who_am_i(self):
#         return f'{self.firstname} {self.lastname}. I am a teacher at {self.university} university.'


# john = Teacher('john', 'doe', 'math', 'MIT')
# print(john.who_am_i())

# # Output:
# # john doe. I am a teacher at MIT university.



# # Solution 3
# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def fullname(self): # title(): john -> John
#         return self.firstname.title() + ' ' + self.lastname.title()

# class Student(Person): # Inheritance
#     pass


# ali_stu = Student('ali', 'alavi')
# print(ali_stu.fullname())

# # Output:
# # Ali Alavi



# # Solution 4
# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def fullname(self): # title(): john -> John
#         return self.firstname.title() + ' ' + self.lastname.title()

# class Student(Person): # Inheritance
#     def __init__(self, firstname, lastname, major):
#         Person.__init__(self, firstname, lastname)
#         self.major = major


# ali_stu = Student('ali', 'alavi', 'Computer Engineering')
# print(ali_stu.fullname())

# # Output:
# # Ali Alavi



# Solution 5
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self): # title(): john -> John
        return self.firstname.title() + ' ' + self.lastname.title()

class Student(Person): # Inheritance
    def __init__(self, firstname, lastname, major):
        #Person.__init__(self, firstname, lastname)
        super().__init__(firstname, lastname)
        self.major = major

  
ali_stu = Student('ali', 'alavi', 'Computer Engineering')
print(ali_stu.fullname())

# Output:
# Ali Alavi
