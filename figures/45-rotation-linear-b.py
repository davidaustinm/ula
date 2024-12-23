from figures import *
from math import *

width = 150
height = width
margin = 5
imargin = 20

size = 4

v = [2,1]
w = [-1,3]
vw = vsum(v,w)
def T(x):
    s = sin(pi/4)
    c = cos(pi/4)
    return [c*x[0] - s*x[1], s*x[0] + c*x[1]]
Tv = T(v)
Tw = T(w)
Tvw = T(vw)

def drawvector(x, c, tail=[0,0]):
    x = vsum(x, tail)
    vect = Vector(x, tail=tail, fillcolor=c, color=c)
    vect.fill()
    vect.draw()
    

beginfigure("45-rotation-linear-b", 2*width+2*margin+imargin, height+2*margin)

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

drawvector(v, gray)
drawvector(w, gray)
drawvector(v, gray, tail=w)
drawvector(w, gray, tail=v)
drawvector(vw, blue)

Label(r"${\mathbf v}$", smult(0.7, v), offset=[3,-3], alignment="lt").draw()
Label(r"${\mathbf w}$", smult(0.5, w), offset=[-3,3], alignment="rt").draw()
Label(r"${\mathbf v} + {\mathbf w}$", vw, offset=[10,-3], alignment="lt").draw()

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

drawvector(Tv, gray)
drawvector(Tw, gray)
drawvector(Tv, gray, tail=Tw)
drawvector(Tw, gray, tail=Tv)
drawvector(Tvw, blue)

Label(r"$T({\mathbf v})$", smult(0.5,Tv), offset=[3,0], alignment="lt").draw()
Label(r"$T({\mathbf w})$", smult(0.5,Tw), offset=[0,3], alignment="rt").draw()
Label(r"$T({\mathbf v}+{\mathbf w})$", Tvw, offset=[2,-1], alignment="rb").draw()

grestore()

endfigure()
 
