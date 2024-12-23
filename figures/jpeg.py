import cv2
import numpy as np
from figures import *
img = cv2.imread('utah.cropped.jpg')

ul = (760,700)
ul = (700, 760)
size = 8
lr = (ul[1]+size,ul[0]+size)
cv2.rectangle(img, (ul[1],ul[0]), lr, [0,255,0], 3)
cv2.imshow("image", img)
#cv2.imwrite("block.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

pixels = []
blue = []
green = []
red = []

print ul
for i in range(8):
    row = []
    bluerow = []
    greenrow = []
    redrow = []
    for j in range(8):
        pix = img[ul[0] + j, ul[1] + i]
        row.append(pix)
        bluerow.append(pix[0])
        greenrow.append(pix[1])
        redrow.append(pix[2])
    blue.append(bluerow)
    green.append(greenrow)
    red.append(redrow)

def square(p, r,g,b):
    newpath()
    box(p[0],7-p[1], 1, 1)
    setcolor([r/255.0, g/255.0, b/255.0])
    fill()
    stroke(0.5)

width=100
height=width
margin = 5
beginfigure("jpeg-orig-block", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],[0,0,8,8])

for i in range(8):
    for j in range(8):
        square([j,i], red[i][j], green[i][j], blue[i][j])

endfigure()

