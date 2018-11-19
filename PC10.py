currentNumber = "1"

for x in range(0, 30):
    i = 0
    counter = 1
    newNumber = ""

    while i < (len(currentNumber) - 1): 
        if currentNumber[i] == currentNumber[i+1]:
            counter += 1
        else:
            newNumber += str(counter)
            newNumber += currentNumber[i]
            counter = 1
        i += 1

    newNumber += str(counter)
    newNumber += currentNumber[i]

    currentNumber = newNumber   # setting new current number

print(len(currentNumber))
# 5808