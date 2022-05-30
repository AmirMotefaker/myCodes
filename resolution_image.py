# Code by @AmirMotefaker

# Find the Resolution of a Image


# Solution 1 - Using PIL
import PIL
from PIL import Image
  
# loading the image
img = PIL.Image.open("image.png")
  
# fetching the dimensions
wid, hgt = img.size
  
# displaying the dimensions
print(str(wid) + "x" + str(hgt))
