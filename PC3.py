import re

text = open("C:\_Code_\Python\python challenges\PC3.txt", "r")
text = text.read()

matches = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", text)

print("".join(matches))

# linkedlist