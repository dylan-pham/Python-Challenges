from PIL import Image, ImageFile
import io

gfxAsBytes = open("PC12.gfx", "rb").read()
image1 = bytearray(b'')
image2 = bytearray(b'')
image3 = bytearray(b'')
image4 = bytearray(b'')
image5 = bytearray(b'')

i = 0

while i < len(gfxAsBytes):  # splitting bytes into 5 different arrays, "dealing 5s"
    if i % 5 == 0:
        image1.append(gfxAsBytes[i])
    elif i % 5 == 1:
        image2.append(gfxAsBytes[i])
    elif i % 5 == 2:
        image3.append(gfxAsBytes[i])
    elif i % 5 == 3:
        image4.append(gfxAsBytes[i])
    elif i % 5 == 4:
        image5.append(gfxAsBytes[i])
    i += 1

def showImage(image):   # shows bytearrays as images
    image = Image.open(io.BytesIO(image))
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    image.show()

showImage(image1)   # dis
showImage(image2)   # pro
showImage(image3)   # port
showImage(image4)   # ional
showImage(image5)   # ity

# disproportionality ---> disproportional