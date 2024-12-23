from figures import *

width=100
height = width
margin = 5

def drawvect(v, c):
    v = Vector(v, fillcolor=c, color=c)
    v.fill()
    v.draw()

size = 4
beginfigure("subspace-quadrant-vector", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size, -size, size, size])

gsave()
cliptoboundingbox()
newpath()
moveto(20,0)
lineto(0,0)
lineto(0,20)
closepath()
fill(gray)
grestore()

Grid([-size,1,size], [-size,1,size]).draw()

axes = Axes()
axes.draw()

newpath()
moveto(size,0)
lineto(0,0)
lineto(0,size)
setlinewidth(2)
stroke(gray)

v = [3,2]
drawvect(v, blue)
drawvect(smult(-1,v), red)

endfigure()
 
