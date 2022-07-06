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



# # Solution 2
# import os
# os.system('cls')

# class Time:
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds

#     def __str__(self):
#         return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'
    
# time1 = Time(17, 5, 42)
# gym_time = Time(23, 1, 4)

# print(time1)
# print(gym_time)


# # Output:
# # 17:05:42
# # 23:01:04



# # Solution 3
# import os
# os.system('cls')

# class Time:
#     def __init__(self, hours, minutes, seconds):
#         if hours > 24:
#             raise ValueError('Hours number should be less than 23.')
#         if minutes > 59:
#             raise ValueError('Minutes number should be less than 60.')
#         if seconds > 59:
#             raise ValueError('Seconds number should be less than 60.')

#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds

#     def __str__(self):
#         return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'
    
# time1 = Time(17, 5, 42)
# gym_time = Time(23, 1, 4)

# print(time1)
# print(gym_time)

# time2 = Time(23, 79, 20)

# # Output
# # 17:05:42
# # 23:01:04
# # Traceback (most recent call last):
# #   File "e:\A.Motefaker\ABC\Python\MyCode\OOP_time.py", line 79, in <module>
# #     time2 = Time(23, 79, 20)
# #   File "e:\A.Motefaker\ABC\Python\MyCode\OOP_time.py", line 62, in __init__
# #     raise ValueError('Minutes number should be less than 60.')
# # ValueError: Minutes number should be less than 60.



# Solution 4 - Operator Overloading
import os
os.system('cls')

class Time:
    def __init__(self, hours, minutes, seconds):
        if hours > 24:
            raise ValueError('Hours number should be less than 23.')
        if minutes > 59:
            raise ValueError('Minutes number should be less than 60.')
        if seconds > 59:
            raise ValueError('Seconds number should be less than 60.')

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'
    
    def __add__(self, other):
        seconds = self.seconds + other.seconds # 46
        minutes = self.minutes + other.minutes + (seconds // 60) # 6
        hours = self.hours + other.hours + (minutes // 60) # 40
        return Time(hours%24, minutes%60, seconds%60)
     

time1 = Time(17, 5, 42)
gym_time = Time(23, 1, 4)

# print(time1)
# print(gym_time)

print(time1 + gym_time)

# Output:
# 16:06:46
