from PIL import Image 
import numpy as np

file = "/Users/dominik/Documents/Projects/Ascii/ASCII_ART/beach.jpg"

im = Image.open(file)
print("Height: ", im.height)
print("Width:  ", im.width)

# Load image into array
imSequence = im.getdata()
imArray = np.array(imSequence)

# New brightness matrix with averages of rgb values
brightnessMatrix = []
for e in imArray:
	average = round(sum(e)/3)
	brightnessMatrix.append(average)

print(brightnessMatrix)



