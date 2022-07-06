# Code by @AmirMotefaker

# OOP - Time (Operator Overloading)
import os
os.system('cls')

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'
    
time1 = Time(17, 5, 42)

print(time1)

# Output:
# 17:5:42
   
