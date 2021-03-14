from PIL import Image 
import numpy as np
import imageio

def get_pixel_matrix(img, height):
    img.thumbnail((height, 200))
    pixels = list(img.getdata())
    return [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]


file = "/Users/dominik/Documents/Projects/Ascii/ASCII_ART/beach.jpg"

im = Image.open(file)
print("Height: ", im.height)
print("Width:  ", im.width)

# Load image into array


imArr = get_pixel_matrix(im, im.height)
countE = 0
countI = 0
for e in imArr:
	for i in imArr[countE]:
		print(imArr[countE][countI])
		countI =+ 1
	countE += 1
	
	
	


	


# New brightness matrix with averages of rgb values
countE = 0
countI = 0
brightnessMatrix = []
for e in imArr:
	for i in imArr[countE]:
		average = round(sum(imArr[countE][countI])/3)
		brightnessMatrix.append(average)
		countI =+ 1
		print(average)
	countE =+ 1
	

# for e in brightnessMatrix:
	# print(e)
		
	
	

	
chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# for each brightness value there is a char representing their brightness
asciiIm = []
for i in brightnessMatrix:
	val = round(i*0.25490)-1
	# print(chars[val],  end='')
		
	# asciiIm.append(chars[round(i*0.25490)-1])	

	
		





