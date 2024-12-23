from figures import *
from math import *

width = 200
height = width
margin = 5

size = 1.25

u = [1,0]
v = [0,1]

def T(x):
    s = sin(pi/4)
    c = cos(pi/4)
    return [c*x[0] - s*x[1], s*x[0] + c*x[1]]
Tu = T(u)
Tv = T(v)

def drawvector(x):
    vect = Vector(x, fillcolor=blue, color=blue)
    vect.fill()
    vect.draw()
    

beginfigure("45-rotation-e1", width+2*margin, height+2*margin)

gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-0.25,-0.25,1.25,1.25])

xr = [-size,0.25,size]

Grid(xr, xr).draw()

axes = Axes()
axes.setticks(xr,xr)
axes.setlabels([0,1,1],[0,1,1])
axes.draw()
axes.drawticks()
axes.drawlabels()

gsave()
newpath()
moveto(0,0)
lineto(1/sqrt(2), 0)
lineto(1/sqrt(2), 1/sqrt(2))
closepath()
setlinewidth(2)
stroke()
grestore()
 
drawvector(Tu)
off = 3
Label(r"$T({\mathbf e}_1)$", Tu, offset=[-off,off],
      alignment="rb", scale=1.2).draw()
s = sin(pi/4)
Label(r"$\displaystyle \frac1{\sqrt{2}}$", [s,s/2],
      offset=[9,0], alignment="lc", scale=1.2).draw()
Label(r"$\displaystyle \frac1{\sqrt{2}}$", [s/2,0],
      offset=[6,-5], alignment="ct", scale=1.2).draw()
Label(r"$1$", [s/2,s/2], offset=[-3,3], alignment="rb", scale=1.2).draw()

grestore()

endfigure()
