from figures import *
from math import *

width = 150
height = width
margin = 5
imargin = 20

size = 4

u = [2,3]
def T(x):
    return [x[0],0]
Tu = T(u)

beginfigure("v-projection", 2*width+2*margin+imargin, height+2*margin)

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
