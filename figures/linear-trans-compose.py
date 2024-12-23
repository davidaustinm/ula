from figures import *
from math import *

width = 120
height = width
margin = 5
imargin = 20

size = 1.25

u = [1,0]
v = [0,1]

def T(x):
    return [x[0], -x[1]]
def S(x):
    s = sin(pi/4)
    c = cos(pi/4)
    return [c*x[0] - s*x[1], s*x[0] + c*x[1]]
Tu = T(u)
Tv = T(v)
STu = S(Tu)
STv = S(Tv)

def drawvector(x):
    vect = Vector(x, fillcolor=blue, color=blue)
    vect.fill()
    vect.draw()

beginfigure("linear-trans-compose", 3*width+2*margin+2*imargin, height+2*margin)

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
drawvector(STu)
drawvector(STv)
Label(r"$S(T({\mathbf e}_1))$", STu, offset=[0, off], alignment="cb").draw()
Label(r"$S(T({\mathbf e}_2))$", STv, offset=[0, -off], alignment="ct").draw()

grestore()

endfigure()
 
