# Code by @AmirMotefaker

# Get the Class Name of an Instance

# Solution 1 - Using __class__.__name__
# class Vehicle:
#     def name(self, name):
#         return name

# v = Vehicle()
# print(v.__class__.__name__)

# Output:
# Vehicle


# Solution 2 - Using type() and __name__ attribute
class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(type(v).__name__)

# Output:
# Vehicle
