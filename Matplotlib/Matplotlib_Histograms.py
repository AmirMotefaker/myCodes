# Code by AmirMotefaker

# Matplotlib - Matplotlib Histograms


# # Solution 1 - Create Histogram
import numpy as np

x = np.random.normal(170, 10, 250)

print(x)



# Solution 2 - A simple histogram
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 
