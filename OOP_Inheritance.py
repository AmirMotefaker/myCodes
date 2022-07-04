# Code by @AmirMotefaker

# OOP - Inheritance 

class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def who_am_i(self):
        return f'{self.firstname} {self.lastname}'


john_stu = Student('john', 'doe')
david_stu = Student('david', 'stuart')

print(john_stu.who_am_i())
print(david_stu.who_am_i())

# Output:
# john doe
# david stuart

