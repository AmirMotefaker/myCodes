# 


from PIL import Image, ImageOps, ImageDraw

img = Image.open('image.png') # loads an image, and displays it using an external viewerview image
img = ImageOps.grayscale(img) # Convert the image to grayscale.
img = ImageOps.equalize(img)  # Equalize the image histogram. 

dicew = 100

dicesize = int(img.width * 1.0 / dicew)
diceh = int(img.height * 1.0 / img.width * dicew)

nim = Image.new("L", (img.width, img.height), 'white') #nim=new image
nimd = ImageDraw.Draw(nim) #nimd=new image draw - ImageDraw.Draw: You can use this module to create new images
#img.show()
#print (img.width, img.height, dicew, diceh, dicesize)

for y in range(0, img.height-dicesize, dicesize):
    for x in range(0, img.width-dicesize, dicesize):
        thisSectorColor = 0 
        for dicex in range(0, dicesize):
            for dicey in range(0, dicesize):
                thisColor = img.getpixel((x+dicex, y+dicey)) # Image.getpixel: Returns the pixel value at a given position.
                thisSectorColor += thisColor
        thisSectorColor /= (dicesize ** 2)
        nimd.rectangle([(x, y), (x+dicesize,  y+dicesize)], thisSectorColor)

nim.show()
        
        #print (x, y, thisSectorColor)
        
