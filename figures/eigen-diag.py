from figures import *
from math import *

sq2 = sqrt(2)

width=150
height = width
margin = 5
imargin = 40

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

beginfigure("eigen-diag", 2*width+2*margin+imargin, 2*height+2*margin + imargin)


## upper left
gsave()
translate(0, height+imargin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])
basis = [[1/sq2, 1/sq2], [-1/sq2, 1/sq2]]

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


## upper right
gsave()
translate(width+imargin,height+imargin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

basis = [[1,0],[0,1]]

outline(basis)
fill(lightgray)

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

## lower left

gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

basis = [[3,0],[0,-1]]

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

## lower right

gsave()
translate(width+imargin,0)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

basis = [[3/sq2, 3/sq2], [1/sq2, -1/sq2]]

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

ad = [1,4]

gsave()
translate(0,20)
Vector([width+margin+imargin-5, 1.5*height+margin+imargin],
       tail=[width+margin+5, 1.5*height+margin+imargin],
       arrowdims=ad).fill()
Label(r"$Q^T$", [width+margin+imargin/2.0, 1.5*height+margin+imargin],
      alignment='cc',
      offset=[0,10]).draw()
grestore()

Vector([width+margin+5, height+margin+5], 
       tail=[width+margin+imargin-5, height+margin+imargin-5],
       arrowdims=ad).fill()
Label(r"$D$", [width+margin+imargin/2.0, height+margin+imargin/2.0],
      alignment='cc',
      offset=[0,12]).draw()

gsave()
translate(0,20)
Vector([width+margin+imargin-5, 0.5*height+margin],
       tail=[width+margin+5, 0.5*height+margin],
       arrowdims=ad).fill()
Label(r"$Q$", [width+margin+imargin/2.0, 0.5*height+margin],
      alignment='cc',
      offset=[0,10]).draw()
grestore()




endfigure()


