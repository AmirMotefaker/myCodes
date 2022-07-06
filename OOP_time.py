# Code by @AmirMotefaker

# OOP - Time (Operator Overloading)

# # Solution 1
# import os
# os.system('cls')

# class Time:
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds

#     def __str__(self):
#         return f'{self.hours}:{self.minutes}:{self.seconds}'
    
# time1 = Time(17, 5, 42)

# print(time1)

# # Output:
# # 17:5:42



# Solution 2
import os
os.system('cls')

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'
    
time1 = Time(17, 5, 42)
gym_time = Time(23, 1, 4)

print(time1)
print(gym_time)


# Output:
# 17:05:42
# 23:01:04
