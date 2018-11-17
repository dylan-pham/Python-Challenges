text = open("PC2.txt", "r")
text = text.read()

counter = {}

for symbol in text:
    if symbol in counter:
        counter[symbol] += 1
    else:
        counter[symbol] = 1

print(counter)

# rare symbols: e q u a l i t y