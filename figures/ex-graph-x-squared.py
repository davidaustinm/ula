from figures import *

width = 200
height = width
margin = 5

size = 4

beginfigure("ex-graph-x-squared", width, height)
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

gsave()
cliptoboundingbox()
Graph(Function(lambda x: x**2), color=blue).draw()
grestore()

mklabels(size, r"$x$", size, r"$y$")
 
endfigure()
