# Code by @AmirMotefaker

# Get the Full Path of the Current Working Directory

import pathlib

# path of the given file
print(pathlib.Path("my_file.txt").parent.absolute())

# current working directory
print(pathlib.Path().absolute())

# Output:
# E:\A.Motefaker\مدارک\Python\MyCode
# E:\A.Motefaker\مدارک\Python\MyCode

