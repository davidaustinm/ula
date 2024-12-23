import cv2
import numpy as np
from figures import *
img = cv2.imread('utah.cropped.jpg')

ul = (760,700)
ul = (700, 760)
size = 8
lr = (ul[0]+size,ul[1]+size)
cv2.rectangle(img, ul, lr, [0,255,0], 3)
#cv2.imshow("image", img)
#cv2.imwrite("block.jpg", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

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

def labelsquare(p, l):
    newpath()
    Label(l, [p[0]+0.5,7.5-p[1]], alignment="cc",scale=0.9).draw()
    box(p[0],7-p[1], 1, 1)
    stroke(0.5)

width=100
height=width
margin = 5
beginfigure("jpeg-block-luminance", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],[0,0,8,8])

luminances = []
lumrows = []
for i in range(8):
    row = []
    for j in range(8):
        lum = 0.299*red[i][j] + 0.587*green[i][j] + 0.113998*blue[i][j]
        square([j,i], lum, lum, lum)
        lum = int(round(lum))
        if lum < 0: lum = 0
        if lum > 255: lum = 255
        luminances.append(lum)
        row.append(lum)
#        square([j,i], red[i][j], green[i][j], blue[i][j])
    lumrows.append(row)

endfigure()

width=150
height=width
margin = 5
beginfigure("jpeg-block-luminance-values", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],[0,0,8,8])

settexenv("ACTexConfig")
for i in range(8):
    for j in range(8):
        labelsquare([i,j], r"{\bf " + str(lumrows[j][i])+r"}")

endfigure()

print luminances
 
