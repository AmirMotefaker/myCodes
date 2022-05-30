# Code by @AmirMotefaker

# Find the Resolution of a Image


import PIL
from PIL import Image
  
# loading the image
img = PIL.Image.open("image.png")
  
# fetching the dimensions
wid, hgt = img.size
  
# displaying the dimensions
print(str(wid) + "x" + str(hgt))
