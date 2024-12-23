from figures import *
from math import *

width = 150
height = width
margin = 5
imargin = 20

size = 4

u = [2,1]
c = 1.5
cu = smult(c,u)
def T(x):
    s = sin(pi/4)
    c = cos(pi/4)
    return [c*x[0] - s*x[1], s*x[0] + c*x[1]]
Tu = T(u)
Tcu = T(cu)

def drawvector(x, c):
    vect = Vector(x, fillcolor=c, color=c)
    vect.fill()
    vect.draw()
    

beginfigure("45-rotation-linear-a", 2*width+2*margin+imargin, height+2*margin)

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

drawvector(cu, blue)
drawvector(u, gray)
Label(r"${\mathbf v}$", u, offset=[3,-3], alignment="lt").draw()
Label(r"$c{\mathbf v}$", cu, offset=[3,-3], alignment="lt").draw()

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

drawvector(Tcu,blue)
drawvector(Tu,gray)
Label(r"$T({\mathbf v})$", Tu, offset=[3,-3], alignment="lt").draw()
Label(r"$T(c{\mathbf v})$", Tcu, offset=[3,-3], alignment="lt").draw()

grestore()

endfigure()
