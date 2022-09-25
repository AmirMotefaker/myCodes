# Code by @AmirMotefaker

# Matplotlib - Matplotlib Line

# Solution 1 - Linestyle - Use a dotted line
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()



# # Solution 2 - Linestyle - Use a dashed line
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dashed')
plt.show()



# # Solution 3 - Linestyle - Use a dashed line
# # Shorter Syntax
# # The line style can be written in a shorter syntax:
# # linestyle can be written as ls.
# # dotted can be written as :.
# # dashed can be written as --.

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls = ':')
plt.show()



# # Solution 4 - Line Color - Set the line color to red
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()



# # Solution 5 - Line Color - Plot with a beautiful green line
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, c = '#4CAF50')
plt.show()



# # Solution 6 - Line Color - Plot with the color named "hotpink"
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, c = 'hotpink')
plt.show()



# # Solution 7 - Line Width - Plot with a 20.5pt wide line
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()



# # Solution 8 - Multiple Lines - raw two lines by specifying a plt.plot() function for each line
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()



# Solution 9 - Multiple Lines - Draw two lines by specifiyng the x- and y-point values for both lines
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
