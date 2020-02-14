import numpy as np 
import scipy as smp
from PIL import Image

img = Image.new('RGB', [4096,2160])
y=0
x=0
index = 0

def setBluePixel(xPos,yPos):
    img.putpixel((xPos,yPos), (0xff0000))

def setBlackPixel(xPos, yPos):
    img.putpixel((xPos,yPos), (0x000000))

print('Making image...')
while (index <= 8847359):
    if((y % 2) == 0): 
        if((x % 2) == 0):
            setBluePixel(x,y)
        else: 
            setBlackPixel(x,y)
    else: 
        if((x % 2) == 0):
            setBlackPixel(x,y)
        else: 
            setBluePixel(x,y)
    
    if(x == 4095):
        if(y == 2159):
            break
        else:
            y += 1
            x = 0
            #print('Moving to line ' + str(y))
    else: 
        x += 1 
    index += 1

img.show()

print('Done. Image saved.')
img.save('./frames/test_frame_a.tif')

