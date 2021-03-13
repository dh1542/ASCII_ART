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


chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# for each brightness value there is a char representing their brightness
asciiIm = []
for i in brightnessMatrix:
	asciiIm.append(chars[round(i*0.25490)-1])
	print(chars[round(i*0.25490)-1],  end='')

	
		





