# Code by AmirMotefaker

# Convert image to binary

# A binary image is a monochromatic image that consists
# of pixels that can have one of exactly two colors,
# usually black and white. 

## Solution 1

# Step-by-Step
# 1- Read the image from the location.
# 2- As a colored image has RGB layers in it and is more
#    complex, convert it to its Grayscale form first.
# 3- Set up a Threshold mark, pixels above the given mark
#    will turn white, and below the mark will turn black.

# import cv2
  
# # read the image file
# img = cv2.imread('image2.png', 2)
  
# ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  
# # converting to its binary form
# bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  

# cv2.imshow("Binary", bw_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


## Solution 2

## Convert color image to black and white
# import cv2

# #read image
# img_grey = cv2.imread('image2.png', cv2.IMREAD_GRAYSCALE)

# # define a threshold, 128 is the middle of black and white in grey scale
# thresh = 128

# # threshold the image
# img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

# #save image
# cv2.imwrite('image2-binary.png',img_binary) 



## Solution 3

## Convert grey scale image to black and white
import cv2

#read image as grey scale
img_grey = cv2.imread('image-binary.png', cv2.IMREAD_GRAYSCALE)

# define a threshold, 128 is the middle of black and white in grey scale
thresh = 128

# threshold the image
img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

#save image
cv2.imwrite('image-black-white.png',img_binary) 
