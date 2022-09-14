# Code by AmirMotefaker

# Represent enum

from enum import Enum

class Day(Enum):
    SUNDAY =  1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7

# print the enum member
print(Day.WEDNESDAY)

# get the name of the enum member
print(Day.WEDNESDAY.name)

# get the value of the enum member
print(Day.WEDNESDAY.value)
