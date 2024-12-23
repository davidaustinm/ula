from figures import *

width=100
height = width
margin = 5

size = 4
beginfigure("subspace-quadrant", width+2*margin, height+2*margin)
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

endfigure()
 
