# Code by AmirMotefaker

# Get File Creation and Modification Date

# Solution 1 - Using os module
import os.path, time

print("Last modified: %s" % time.ctime(os.path.getmtime("my_file.txt")))
print("Created: %s" % time.ctime(os.path.getctime("my_file.txt")))

# Output:
# Last modified: Mon Jun 13 09:14:16 2022
# Created: Mon Jun 13 09:13:44 2022



# Solution 2 - Using stat() method
import datetime
import pathlib

fname = pathlib.Path('my_file.txt')
print("Last modification time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_mtime))
print("Last metadata change time or path creation time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_ctime))


# Output:
# Last modification time: 2022-06-13 09:14:16.248481
# Last metadata change time or path creation time: 2022-06-13 09:13:44.890502
