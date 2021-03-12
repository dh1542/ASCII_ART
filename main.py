from PIL import Image 
import numpy as np

file = "/Users/dominik/Documents/Projects/Ascii/ASCII_ART/beach.jpg"

im = Image.open(file)
print("Height: ", im.height)
print("Width:  ", im.width)

# Load image into array
imSequence = im.getdata()
imArray = np.array(imSequence)

print (imArray)
