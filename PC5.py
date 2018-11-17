import urllib.request
import pickle

pickled = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p") # pickle file
unpickled = pickle.load(pickled) # unpickling pickle file

for item in unpickled:
    print("".join(a * b for a, b in item)) # using dictionary comprehension to draw solution

# channel