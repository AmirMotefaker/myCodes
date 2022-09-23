# Code by AmirMotefaker

# Linear Independence

# linear independent: 
# if no vector exists that we can represent it as the linear combination of any other two vectors.


# Solution 1
import numpy as np

v = np.array([1, -1, 2]).reshape(-1,1)
u = np.array([0, 3, 1]).reshape(-1,1)
w = np.array([2, 1, 5]).reshape(-1,1)

print('Does the equality w = 2v+u holds? Answer:', np.all(w == 2*v+u))

# Output:
# Does the equality w = 2v+u holds? Answer: True



# Solution 2
import numpy as np

v = np.array([2, 4, -3]).reshape(-1,1)
u = np.array([-2, 5, 2]).reshape(-1,1)
w = np.array([0, 9, 6]).reshape(-1,1)

print('Does the equality w = 2v+u holds? Answer:', np.all(w == 2*v+u))

# Output:
# Does the equality w = 2v+u holds? Answer: False
