# Code by @AmirMotefaker

# Extract Extension From the File Name

# Solution 1 - Using splitext() method from os module
import os
file_details = os.path.splitext('file.ext')
print(file_details)
print(file_details[1])

# output:
# ('file', '.ext')
# .ext

