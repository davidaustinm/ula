from figures import *

width = 200
height = width
margin = 5

size = 4

beginfigure("vector-u", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-size,-size,size,size])

xr = [-size,1,size]

Grid(xr, xr).draw()

axes = Axes()
axes.setticks(xr,xr)
axes.setlabels([-size,2,size], [-size,2,size])
axes.draw()
axes.drawticks()
axes.drawlabels()

u = Vector([2,1], fillcolor=blue, color=blue)
u.fill()
u.draw()

Label(r"${\mathbf v}$", [2,1], offset=[3,-3],alignment="lt").draw()

mklabels(size, r"$x$", size, r"$y$")

endfigure()
