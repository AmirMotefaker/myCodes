# Code by amotef@gmail.com

# QR Code generator

# Generator QRcode(Basic)

import qrcode

img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
