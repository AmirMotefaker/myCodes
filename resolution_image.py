# Code by @AmirMotefaker

# Find the Resolution of a Image


# Solution 1 - Using PIL

# import PIL
# from PIL import Image
  
# # loading the image
# img = PIL.Image.open("image.png")
  
# # fetching the dimensions
# wid, hgt = img.size
  
# # displaying the dimensions
# print(str(wid) + "x" + str(hgt))



# solution 2 - Using OpenCV

import cv2
  
# loading the image
img = cv2.imread("image.png")
  
# fetching the dimensions
wid = img.shape[1]
hgt = img.shape[0]
  
# displaying the dimensions
print(str(wid) + "x" + str(hgt))


