from figures import *
from math import *

width=100
height = width
margin = 5

size = 4
beginfigure("subspace-quadrant-2-vectors", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size, -size, size, size])

gsave()
cliptoboundingbox()

for i in range(2):
    newpath()
    moveto(20,0)
    lineto(0,0)
    lineto(0,20)
    closepath()
    fill(gray)
    rotate(pi)
grestore()

Grid([-size,1,size], [-size,1,size]).draw()

newpath()
moveto(size,0)
lineto(-size,0)
moveto(0,size)
lineto(0,-size)
setlinewidth(2)
stroke(gray)

def drawvect(v, c):
    v = Vector(v, fillcolor=c, color=c)
    v.fill()
    v.draw()

v = [0,3]
w = [-2,0]

drawvect(v, blue)
drawvect(w,blue)
drawvect(vsum(v,w), red)

endfigure()
 
