from PIL import Image

image = Image.open("PC11.jpg")
newImage = Image.new(mode="RGBA", size=(320, 240))  # create new image

x = 0
y = 0

for x in range(320):
    for y in range(240):
        a = (x * 2, y * 2)
        newImage.putpixel((x,y), image.getpixel((a)))   # placing new pixels

newImage.show()