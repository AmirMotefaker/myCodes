# Code by @AmirMotefaker

# Method Resolution Order(MRO)
 
# # Solution 1
# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def fullname(self): # title(): john -> John
#         return self.firstname.title() + ' ' + self.lastname.title()

# class Student(Person): # Inheritance
#     def __init__(self, firstname, lastname, major, uni):
#         super().__init__(firstname, lastname)
#         self.major = major
#         self.university = uni

#     def fullname(self):
#         return f'{self.firstname} {self.lastname}. I am studying in {self.major}.'

#     def education_info(self):
#         return f'{self.university}: {self.major} '


# class Teacher(Person):
#     def __init__(self, firstname, lastname, uni, department):
#         super().__init__(firstname, lastname)
#         self.uni = uni
#         self.dept = department 

#     def working_info(self):
#         return f'I am working in {self.uni} university at {self.dept} department.'

# help(Teacher)

# # Output:
# # Help on class Teacher in module __main__:

# # class Teacher(Person)
# #  |  Teacher(firstname, lastname, uni, department)
# #  |  
# #  |  Method resolution order:
# #  |      Teacher
# #  |      Person
# #  |      builtins.object
# #  |
# #  |  Methods defined here:
# #  |
# #  |  __init__(self, firstname, lastname, uni, department)
# #  |      Initialize self.  See help(type(self)) for accurate signature.
# #  |
# #  |  working_info(self)
# #  |
# #  |
# #  |  fullname(self)
# #  |
# #  |  ----------------------------------------------------------------------
# #  |  Data descriptors inherited from Person:
# #  |
# #  |  __dict__
# #  |      dictionary for instance variables (if defined)
# #  |
# #  |  __weakref__
# #  |      list of weak references to the object (if defined)



# # Solution 2
# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def fullname(self): # title(): john -> John
#         return self.firstname.title() + ' ' + self.lastname.title()

# class Student(Person): # Inheritance
#     def __init__(self, firstname, lastname, major, uni):
#         super().__init__(firstname, lastname)
#         self.major = major
#         self.university = uni

#     def fullname(self):
#         return f'{self.firstname} {self.lastname}. I am studying in {self.major}.'

#     def education_info(self):
#         return f'{self.university}: {self.major} '


# class Teacher(Person):
#     def __init__(self, firstname, lastname, uni, department):
#         super().__init__(firstname, lastname)
#         self.uni = uni
#         self.dept = department 

#     def working_info(self):
#         return f'I am working in {self.uni} university at {self.dept} department.'

# class Sample(Teacher):
#     pass

# help(Sample)

# # Output:
# # Help on class Sample in module __main__:

# # class Sample(Teacher)
# #  |  Sample(firstname, lastname, uni, department)
# #  |
# #  |  Method resolution order:
# #  |      Sample
# #  |      Teacher
# #  |      Person
# #  |      builtins.object
# #  |
# #  |  Methods inherited from Teacher:
# #  |
# #  |  __init__(self, firstname, lastname, uni, department)
# #  |      Initialize self.  See help(type(self)) for accurate signature.
# #  |
# #  |  working_info(self)
# #  |
# #  |  fullname(self)
# #  |
# #  |  ----------------------------------------------------------------------
# #  |  Data descriptors inherited from Person:
# #  |
# #  |  __dict__
# #  |      dictionary for instance variables (if defined)
# #  |
# #  |  __weakref__
# #  |      list of weak references to the object (if defined)



# Solution 3
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self): # title(): john -> John
        return self.firstname.title() + ' ' + self.lastname.title()

class Student(Person): # Inheritance
    def __init__(self, firstname, lastname, major, uni):
        super().__init__(firstname, lastname)
        self.major = major
        self.university = uni

    def fullname(self):
        return f'{self.firstname} {self.lastname}. I am studying in {self.major}.'

    def education_info(self):
        return f'{self.university}: {self.major} '


class Teacher(Person):
    def __init__(self, firstname, lastname, uni, department='o'):
        super().__init__(firstname, lastname)
        self.uni = uni
        self.dept = department 

    def working_info(self):
        return f'I am working in {self.uni} university at {self.dept} department.'

class Sample(Teacher):
    pass

s = Sample('s', 's', 's')
print(s.working_info())

# Output:
# I am working in s university at o department.
