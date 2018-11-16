import urllib.request

baseURL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
# sourceCode = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345").read().decode("utf-8")
sourceCode = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022").read().decode("utf-8")

while ("and the next nothing" in sourceCode):
    for letter in sourceCode:
        if letter.isdigit():
            baseURL += str(letter)
        else:
            continue
    sourceCode = urllib.request.urlopen(baseURL).read().decode("utf-8")
    print(sourceCode)
    baseURL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" # resetting baseURL to original

# and the next nothing is 16044
# Yes. Divide by two and keep going.

# loop ends at peak.html