from PIL import Image

wire = Image.open("PC14.png")
newImage = Image.new(mode="RGBA", size=(100, 100))

wireX = 0

topS = 0
topE = 100
topY = 0

rightS = 1
rightE = 100
rightX = 99

bottomS = 98
bottomE = -1
bottomY = 99

leftS = 98
leftE = 0
leftX = 0

while wireX < 10000:    # wrap around until all 10000 pixels are used up
    for x in range(topS, topE):
        newImage.putpixel((x, topY), wire.getpixel((wireX, 0)))
        wireX += 1

    for y in range(rightS, rightE):
        newImage.putpixel((rightX, y), wire.getpixel((wireX, 0)))
        wireX += 1

    for x in range(bottomS, bottomE, -1):
        newImage.putpixel((x, bottomY), wire.getpixel((wireX, 0)))
        wireX += 1

    for y in range(leftS, leftE, -1):
        newImage.putpixel((leftX, y), wire.getpixel((wireX, 0)))
        wireX += 1

    # adjusting values
    topS += 1
    topE -= 1
    topY += 1

    rightS += 1
    rightE -= 1
    rightX -= 1

    bottomS -= 1
    bottomE += 1
    bottomY -= 1

    leftS -= 1
    leftE += 1
    leftX += 1

newImage.show()
# picture of a cat