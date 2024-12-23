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

beginfigure("eigen-diag-D", 2*width+2*margin+imargin, height+2*margin)

gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])
basis = [[1,0], [0,1]]

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
Grid([-size,1,size],[-size,1,size]).draw()
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

basis = [[3,0], [0,-1]]

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


