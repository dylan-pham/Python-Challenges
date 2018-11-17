from PIL import Image

image = Image.open("PC7.png")

RGBvalues = []
for i in range(0, image.width): # collecting RGB values from middle of image
    RGBvalues.append(image.getpixel((i, image.height / 2)))

unduplicatedValues = []
for value in RGBvalues:
    if value[0] == value[1] == value[2]:    # taking single R value since R, G and B values are the same 
        unduplicatedValues.append(value[0])

string = []
for value in unduplicatedValues:    # converting integers in ASCII
    string.append(chr(value))

print("".join(string[::7])) # there are 7 of each value, only want 1 of each
# "smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]"

answer = []
for value in [105, 110, 116, 101, 103, 114, 105, 116, 121]: # 2nd conversion of integers to ASCII
    answer.append(chr(value))

print("".join(answer))
# integrity