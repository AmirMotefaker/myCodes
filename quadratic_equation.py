# Code by AmirMotefaker

# Solve Quadratic Equation

# ax**2 + bx + c = 0,
# where a, b and c are real numbers
# and a !< 0

# (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

# Output:
# The solution are (-3+0j) and (-2+0j)
