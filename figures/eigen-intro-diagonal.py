from figures import *

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

beginfigure("eigen-intro-diagonal", 2*width+2*margin+imargin, height+2*margin)

gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])
basis = [[1,0],[0,1]]

outline(basis)
fill(lightgray)

Grid([-size,1,size],[-size,1,size]).draw()

axes = Axes()
axes.draw()

ld = 3
axes.setticks([-size,1,size], [-size,1,size])
axes.setlabels([-ld, ld, ld], [-ld, ld, ld])
axes.drawticks()
axes.drawlabels()

outline(basis)
stroke(gray)

drawvec([1,0], black)
drawvec([0,1], black)

Label(r"${\mathbf e}_1$", [1,0], alignment="lt", offset=[3,-3]).draw()
Label(r"${\mathbf e}_2$", [0,1], alignment="rb", offset=[-3,3]).draw()

grestore()

translate(width+imargin,0)
gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])
basis = [[3,0],[0,-1]]

outline(basis)
fill(lightred)

gsave()
cliptoboundingbox()
atransform(basis[0], basis[1])
Grid([-size,1,size],[-size,1,size]).draw()
grestore()

axes = Axes()
axes.draw()
axes.setticks([-size,1,size], [-size,1,size])
axes.setlabels([-ld, ld, ld], [-ld, ld, ld])
axes.drawticks()

outline(basis)
stroke(gray)
axes.drawlabels()

drawvec(basis[0], black)
drawvec(basis[1], black)

Label(r"$3{\mathbf e}_1$", basis[0], alignment="lb", offset=[3,3]).draw()
Label(r"$-{\mathbf e}_2$", basis[1], alignment="rt", offset=[-3,-3]).draw()

grestore()

endfigure()


