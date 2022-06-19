# Code by @AmirMotefaker

# Get the Class Name of an Instance

class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(v.__class__.__name__)

# Output:
# Vehicle
