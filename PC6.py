import zipfile

comments = []

with zipfile.ZipFile("PC6.zip", "r") as z:
    for name in z.namelist():   # iterating through files inside zip file
        info = z.open(name).read()  # looking at content inside each file

        if "nothing" not in str(info):  # checking if there are any files that stand out
            print(info) # says to "collect the comments"

        comments.append(z.getinfo(name).comment.decode())   # collecting comments

print(set(comments))    # letters are "NGOYEX" ----> "OXYGEN"