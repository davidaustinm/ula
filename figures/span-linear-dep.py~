from figures import *

width = 200
height = width
margin = 5

size = 4

beginfigure("span-linear-indep", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-size,-size,size,size])

u = [2, 0]
v = [-1, 1]

#Grid([-4,1,4], [-4,1,4], color=lightgray).draw()

gsave()
cliptoboundingbox()
atransform(u,v)
MGrid([-20,1,20],[-20,1,20]).draw()
grestore()

axes = Axes()
axes.draw()
axes.setticks([-4,1,4], [-4,1,4])
axes.setlabels([-4,1,4], [-4,1,4])
axes.drawticks()
axes.drawlabels()

vector = Vector(u, color=gray, fillcolor=gray)
vector.fill()
vector.draw()

vector = Vector(v, color=gray, fillcolor=gray)
vector.fill()
vector.draw()

Label(r"${\mathbf v}$", u, offset=[3,3], alignment="lb").draw()
Label(r"${\mathbf w}$", v, offset=[3,3], alignment="lb").draw()
 
endfigure()
