# Code by AmirMotefaker

# Convert Kilometers to Miles

# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

# Output:
# Enter value in kilometers: 124
# 124.00 kilometers is equal to 77.05 miles
