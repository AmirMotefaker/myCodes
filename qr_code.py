# Code by AmirMotefaker

# QR Code generator

# https://pypi.org/project/qrcode/

# Generator QRcode(Basic)

# import qrcode

# img = qrcode.make('Some data here')
# type(img)  # qrcode.image.pil.PilImage
# img.save("some_file.png")



# Generator QRcode(Advanced)

# import qrcode

# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('Some data')
# qr.make(fit=True)

# # img = qr.make_image(fill_color="black", back_color="white")
# img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
# img.save("some_file.png")


# Example

# import io
# import qrcode
# qr = qrcode.QRCode()
# qr.add_data("Some text")
# f = io.StringIO()
# qr.print_ascii(out=f)
# f.seek(0)
# print(f.read())


# QRCode for URL link

# import qrcode

# URL of the homepage
# We'll encode this URL to a QR code
# URL = "https://github.com/AmirMotefaker"

# qr = qrcode.QRCode(version=4, box_size=10, border=4, \
# error_correction=qrcode.constants.ERROR_CORRECT_L)

# qr.add_data(URL)
# qr.make(fit=True)

# img = qr.make_image(fill_color='green', back_color='white')
# img.save('github_AmirMotefaker.png')


## Styled QR Code - QR Code with rounded corners

# import qrcode
# from qrcode.image.styledpil import StyledPilImage
# from  qrcode.image.styles.moduledrawers import RoundedModuleDrawer

# qr = qrcode.QRCode(version=4, box_size=10, border=4, \
# error_correction=qrcode.constants.ERROR_CORRECT_H)
# qr.add_data('https://github.com/AmirMotefaker')

# img  = qr.make_image(image_factory=StyledPilImage, 
# module_drawer = RoundedModuleDrawer())
# img.save('github_AmirMotefaker.png')


## Styled QR Code - QR Code with radial gradiant style

# import qrcode
# from qrcode.image.styledpil import StyledPilImage
# from qrcode.image.styles.colormasks import RadialGradiantColorMask


# qr = qrcode.QRCode(version=4, box_size=10, border=4, \
# error_correction=qrcode.constants.ERROR_CORRECT_H)

# qr.add_data('https://github.com/AmirMotefaker')
# img = qr.make_image(image_factory=StyledPilImage, 
#                     color_mask=RadialGradiantColorMask())
# img.save('github_AmirMotefaker.png')


## Styled QR Code - Add or Embed an image to a QR Code
# import qrcode
# from qrcode.image.styledpil import StyledPilImage

# qr = qrcode.QRCode(version=4, box_size=10, border=4, \
# error_correction=qrcode.constants.ERROR_CORRECT_H)

# qr.add_data('https://github.com/AmirMotefaker')
# img = qr.make_image(image_factory=StyledPilImage, \
# embeded_image_path="image.png")

# img.save('github_AmirMotefaker.png')


## Decode or Read a QR Code from an Image
# Install opencv-python: pip install opencv-python

import cv2
# read the QR Code image
img = cv2.imread("github_AmirMotefaker.png")
# initialize the cv2 QR Code detector
qr_detector = cv2.QRCodeDetector()

# detect QR Code and decode
Data, BBOX, Straight_QRcode = qr_detector.detectAndDecode(img)

# Check if there is a QR code or not.
if BBOX is not None:
    if Data:
        print(Data)
    else:
        print("No data is there")
else:
    print("There is not any QR code")

