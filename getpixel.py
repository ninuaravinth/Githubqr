
# Importing Image from PIL package 
from PIL import Image 

# creating a image object 
im = Image.open(r"py.png") 
px = im.load() 
print (px[4, 4]) 
px[4, 4] = (0, 0, 0) 
print (px[4, 4]) 
cordinate = x, y = 150, 59

# using getpixel method 
print (im.getpixel(cordinate)); 
