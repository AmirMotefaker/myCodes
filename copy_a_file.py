# Code by @AmirMotefaker

# Copy a File

from shutil import copyfile
copyfile("a.txt", "b.txt")


# methods copy():
# Method	    Preserves Permissions    	Supports Directory as Destination	    Copies Metadata	   Supports file object
# copy()	           Yes	                         Yes	                         No	                No
# copyfile()	       No                           No                              No             	No
# copy2()	           Yes	                         Yes	                         Yes            	No
# copyfileobj()      No	                         No	                             No                 Yes   
