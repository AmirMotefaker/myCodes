# Code by @AmirMotefaker

# Trace Matrix

#  matrix.trace(): Return sum of a diagonal elements of a matrix

# # Solution 1
# # using matrix.trace() method can help us to find the 
# # sum of all the elements of a diagonal of given matrix.
import numpy as np
              
gfg = np.matrix('[4, 1; 12, 3]')
              
trace = gfg.trace()
    
print(trace)

# # Output:
# # [[7]]



# Solution 2
import numpy as np
              
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
              
trace = gfg.trace()
    
print(trace)

# Output:
# [[13]]
