from figures import *
from math import *

width = 150
height = width
margin = 5
imargin = 20

size = 1.25

u = [1,0]
v = [0,1]

def T(x):
    return [x[0], -x[1]]
Tu = T(u)
Tv = T(v)

def drawvector(x):
    vect = Vector(x, fillcolor=blue, color=blue)
    vect.fill()
    vect.draw()
    

beginfigure("v-reflection-basis", 2*width+2*margin+imargin, height+2*margin)

gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

xr = [-size,0.25,size]

Grid(xr, xr).draw()

axes = Axes()
axes.setticks(xr,xr)
axes.setlabels([-1,1,1],[-1,1,1])
axes.draw()
axes.drawticks()
axes.drawlabels()

#mklabels(size, r"$x$", size, r"$y$")

drawvector(u)
drawvector(v)
off = 6
Label(r"${\mathbf e}_1$", u, offset=[-off,off], alignment="rb").draw()
Label(r"${\mathbf e}_2$", v, offset=[off,-off], alignment="lt").draw()

grestore()

translate(width+imargin, 0)

gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

xr = [-size,0.25,size]

Grid(xr, xr).draw()

axes = Axes()
axes.setticks(xr,xr)
axes.setlabels([-1,1,1],[-1,1,1])
axes.draw()
axes.drawticks()
axes.drawlabels()

#mklabels(size, r"$x$", size, r"$y$")
off = 6
drawvector(Tu)
drawvector(Tv)
Label(r"$T({\mathbf e}_1)$", Tu, offset=[-off, off], alignment="rb").draw()
Label(r"$T({\mathbf e}_2)$", Tv, offset=[off, off], alignment="lb").draw()

grestore()

endfigure()
