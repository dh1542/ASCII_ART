from PIL import Image 

file = "/Users/dominik/Documents/Projects/ASCII/beach.jpg"

im = Image.open(file)
print("Height: ", im.height)
print("Width:  ", im.width)