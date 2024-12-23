from figures import *
from math import *

width=150
height = width
margin = 5
imargin = 20

def outline(basis):
    v = basis[0]
    w = basis[1]
    newpath()
    moveto(0,0)
    lineto(v)
    rlineto(w)
    lineto(w)
    closepath()

def drawvec(v, c):
    vec = Vector(v, fillcolor=c, color=c)
    vec.fill()
#    vec.draw()

size = 4
gsize = 3*size

beginfigure("eigen-diag-A", 2*width+2*margin+imargin, height+2*margin)

sq2 = sqrt(2)

gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])
basis = [[1/sq2, 1/sq2], [-1/sq2, 1/sq2]]

settexenv('ACTexConfig')

outline(basis)
fill(lightgray)

axes = Axes()
axes.draw()

axes.setticks([-size,1,size], [-size,1,size])
axes.setlabels([-2,2,2],[-2,2,2])
axes.drawticks()
axes.drawlabels()

gsave()
cliptoboundingbox()
atransform(basis[0], basis[1])
MGrid([-gsize,1,gsize],[-gsize,1,gsize]).draw()

newpath()
moveto(-gsize,0)
lineto(gsize,0)
moveto(0,-gsize)
lineto(0,gsize)
stroke(0.5)
grestore()

axes.draw()
axes.drawticks()
outline(basis)
stroke(gray)

#drawvec(basis[0], black)
#drawvec(basis[1], black)

#Label(r"${\mathbf v}_1$", basis[0], alignment="lc", offset=[3,0]).draw()
#Label(r"${\mathbf v}_2$", basis[1], alignment="rc", offset=[-3,0]).draw()

grestore()
 
translate(width+imargin,0)
gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

basis = [[3/sq2,3/sq2], [1/sq2, -1/sq2]]

outline(basis)
fill(lightred)

gsave()
cliptoboundingbox()
atransform(basis[0], basis[1])
MGrid([-gsize,1,gsize],[-gsize,1,gsize]).draw()

newpath()
moveto(-gsize,0)
lineto(gsize,0)
moveto(0,-gsize)
lineto(0,gsize)
stroke(0.5)
grestore()

axes = Axes()
axes.draw()
axes.setticks([-size,1,size], [-size,1,size])
axes.setlabels([-2,2,2],[-2,2,2])
axes.drawticks()
axes.drawlabels()

outline(basis)
stroke(gray)

#drawvec(basis[0], black)
#drawvec(basis[1], black)

#Label(r"$3{\mathbf v}_1$", basis[0], alignment="rb", offset=[-4,0]).draw()
#Label(r"$-{\mathbf v}_2$", basis[1], alignment="ct", offset=[0,-4]).draw()


grestore()

endfigure()


