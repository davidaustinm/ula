from figures import *
from math import *

width = 150
height = width
margin = 5
imargin = 30

def outline(v,w):
    newpath()
    moveto(0,0)
    lineto(v)
    rlineto(w)
    lineto(w)
    closepath()

def drawvector(v, color):
    v = Vector(v, fillcolor = color, color=color)
    v.fill()
#    v.draw()

size = 3

beginfigure("det-identity", 2*width+3*margin+imargin, height+2*margin)

gsave()
setupcoordinates([margin, margin, width+margin, height + margin],
                 [-2.5,-2.5,2.5,2.5])

cliptoboundingbox()

v = [1,0]
w = [0,1]

Grid([-size,1,size], [-size,1,size]).draw()
 
outline(v,w)
fill(lightblue)

gsave()
outline(v,w)
clip()
Grid([-size,1,size], [-size,1,size], color=gray).draw()
grestore()

axes = Axes()
axes.draw()
axes.setticks([-size,1,size], [-size,1,size])
axes.setlabels([-2,2,2],[-2,2,2])
axes.drawticks()
axes.drawlabels()

drawvector(v, black)
drawvector(w, black)

Label(r"${\mathbf v}_1$", v, offset=[4,-4], alignment="lt").draw()
Label(r"${\mathbf v}_2$", w, offset=[-3,3], alignment="rb").draw()

grestore()

translate(width+imargin+margin, 0)

gsave()
setupcoordinates([margin, margin, width+margin, height + margin],
                 [-2.5,-2.5,2.5,2.5])

cliptoboundingbox()

v = [-2,0]
w = [0,1]
Grid([-size,1,size], [-size,1,size]).draw()
 
outline(v,w)
fill(lightred)

gsave()
outline(v,w)
clip()
Grid([-size,1,size], [-size,1,size], color=gray).draw()
grestore()

axes = Axes()
axes.draw()
axes.setticks([-size,1,size], [-size,1,size])
axes.setlabels([-2,2,2],[-2,2,2])
axes.drawticks()
axes.drawlabels()

drawvector(v, black)
drawvector(w, black)

Label(r"${\mathbf v}_1$", v, offset=[-3,3], alignment="rb").draw()
Label(r"${\mathbf v}_2$", w, offset=[-3,3], alignment="rb").draw()

grestore() 

endfigure()


