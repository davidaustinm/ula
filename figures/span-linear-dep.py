from figures import *

width = 200
height = width
margin = 5

size = 4

beginfigure("span-linear-dep", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-size,-size,size,size])

u = [-1, 1]
v = [2, -2]

#Grid([-4,1,4], [-4,1,4], color=lightgray).draw()

newpath()
moveto(-size, size)
lineto(size, -size)
stroke(lightgray)

axes = Axes()
axes.draw()
axes.setticks([-4,1,4], [-4,1,4])
axes.setlabels([-4,1,4], [-4,1,4])
axes.drawticks()
axes.drawlabels()

vector = Vector(u, color=blue, fillcolor=blue)
vector.fill()
vector.draw()

vector = Vector(v, color=blue, fillcolor=blue)
vector.fill()
vector.draw()

Label(r"${\mathbf v}$", u, offset=[3,3], alignment="lb").draw()
Label(r"${\mathbf w}$", v, offset=[3,3], alignment="lb").draw()
 
endfigure()
