from figures import *
from math import *

width = 150
height = width
margin = 5
imargin = 20

size = 4

u = [3,1]
def T(x):
    s = sin(pi/4)
    c = cos(pi/4)
    return [c*x[0] - s*x[1], s*x[0] + c*x[1]]
Tu = T(u)

beginfigure("45-rotation", 2*width+2*margin+imargin, height+2*margin)

gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

xr = [-size,1,size]

Grid(xr, xr).draw()

axes = Axes()
axes.setticks(xr,xr)
axes.setlabels([-size,2,size], [-size,2,size])
axes.draw()
axes.drawticks()
#axes.drawlabels()

#mklabels(size, r"$x$", size, r"$y$")

vect = Vector(u, fillcolor=blue, color=blue)
vect.fill()
vect.draw()

Label(r"${\mathbf x}$", u, offset=[3,3], alignment="lb").draw()

grestore()

translate(width+imargin, 0)

gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

xr = [-size,1,size] 

Grid(xr, xr).draw()

axes = Axes()
axes.setticks(xr,xr)
axes.setlabels([-size,2,size], [-size,2,size])
axes.draw()
axes.drawticks()
#axes.drawlabels()

#mklabels(size, r"$x$", size, r"$y$")

vect = Vector(Tu, fillcolor=blue, color=blue)
vect.fill()
vect.draw()

Label(r"$T({\mathbf x})$", Tu, offset=[3,3], alignment="lb").draw()

grestore()

endfigure()
