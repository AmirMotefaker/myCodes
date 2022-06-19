# Code by @AmirMotefaker

# Get the File Name From the File Path

# Solution 1 - Using os module
import os

# file name with extension
file_name = os.path.basename('myResume.docx')

# file name without extension
print(os.path.splitext(file_name)[0])

# Output:
# myResume
