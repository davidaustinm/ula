from figures import *

width = 175
height = width
margin = 5

size = 4

beginfigure("empty-ls", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1,-1,size,size])

settexenv("ACTexConfig")

xr = [-1,1,size]

Grid(xr, xr).draw()

axes = Axes()
axes.setticks(xr,xr)
axes.setlabels([-1,1,size], [-1,1,size])
axes.draw()
axes.drawticks()
axes.drawlabels()

mklabels(size, r"$x$", size, r"$y$")

endfigure() 
