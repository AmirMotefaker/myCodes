# Code by AmirMotefaker

# Vector Space

# # Solution 1
# # create a horizontal vector and a vertical vector 
import numpy as np
  
# # 1-D list (Horizontal)
list1 = [1, 2, 3]
  
# # 1-D list (Vertical)
list2 = [[10],
        [20],
        [30]]
  
vector1 = np.array(list1)
  
vector2 = np.array(list2)
  
print("Horizontal Vector")
print(vector1)
  
print("----------------")
  
print("Vertical Vector")
print(vector2)

# # Output:
# # Horizontal Vector
# # [1 2 3]
# # ----------------
# # Vertical Vector
# # [[10]
# #  [20]
# #  [30]]



# # Basic Arithmetic operation
import numpy as np
  
list1 = [5, 6, 9]
  
list2 = [1, 2, 3]
  
vector1 = np.array(list1)
  
print("First Vector          : " + str(vector1))
  
vector2 = np.array(list2)
  
print("Second Vector         : " + str(vector2))
  
# # a + b = (a1 + b1, a2 + b2, a3 + b3)
addition = vector1 + vector2
  
print("Vector Addition       : " + str(addition))
  
# # a - b = (a1 - b1, a2 - b2, a3 - b3)
subtraction = vector1 - vector2
  
print("Vector Subtraction   : " + str(subtraction))
  
# # a * b = (a1 * b1, a2 * b2, a3 * b3)
multiplication = vector1 * vector2
  
print("Vector Multiplication : " + str(multiplication))
  
# # a / b = (a1 / b1, a2 / b2, a3 / b3)
division = vector1 / vector2
  
print("Vector Division       : " + str(division))

# # Output:
# # First Vector          : [5 6 9]
# # Second Vector         : [1 2 3]
# # Vector Addition       : [ 6  8 12]
# # Vector Subtraction   : [4 4 6]
# # Vector Multiplication : [ 5 12 27]
# # Vector Division       : [5. 3. 3.]



# # Vector Dot Product 
# # the dot product or scalar product is an algebraic operation that takes
# # two equal-length sequences of numbers and returns a single number. 
import numpy as np
  
list1 = [5, 6, 9]
  
list2 = [1, 2, 3]
  
vector1 = np.array(list1)
  
print("First Vector  : " + str(vector1))
  
vector2 = np.array(list2)
  
print("Second Vector : " + str(vector2))
  
# # a . b = (a1 * b1 + a2 * b2 + a3 * b3)
# # a . b = (a1b1 + a2b2 + a3b3)
dot_product = vector1.dot(vector2)
  
print("Dot Product   : " + str(dot_product))

# # Output:
# # First Vector  : [5 6 9]
# # Second Vector : [1 2 3]
# # Dot Product   : 44



# Vector-Scalar Multiplication 
# To perform scalar multiplication, we need to multiply the 
# scalar by each component of the vector.
import numpy as np
  
list1 = [1, 2, 3]
  
vector = np.array(list1)
  
print("Vector  : " + str(vector))
  
scalar = 2
  
print("Scalar  : " + str(scalar))
   
# s * v = (s * v1, s * v2, s * v3)
scalar_mul = vector * scalar
  
print("Scalar Multiplication : " + str(scalar_mul))

# Output:
# Vector  : [1 2 3]
# Scalar  : 2
# Scalar Multiplication : [2 4 6]
