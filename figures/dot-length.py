from figures import *

x0 = -1
x1 = 4

width=175
height=width
margin = 5
beginfigure("dot-length", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [x0,x0,x1,x1])

Grid([x0,1,x1], [x0,1,x1]).draw()

newpath()
box(0,0,3,2)
stroke(0.5)

axes = Axes()
axes.draw()
axes.setticks([x0,1,x1], [x0,1,x1])
axes.setlabels([x0,1,x1], [x0,1,x1])
axes.drawticks()
axes.drawlabels()

Vector([3,2]).fill()
Label(r"${\mathbf v}$", [3,2], alignment="lb", offset=[3,3]).draw()

endfigure()
