from figures import *

width = 200
height = width
margin = 5

size = 4

beginfigure("empty-4-diag", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-size,-size,size,size])

xr = [-size,1,size]

Grid(xr, xr).draw()

settexenv('ACTexConfig')

axes = Axes()
axes.setticks(xr,xr)
axes.setlabels([-size,2,size], [-size,2,size])
axes.draw()
axes.drawticks()
axes.drawlabels()

newpath()
moveto(-size, -size)
lineto(size,size)
moveto(-size,size)
lineto(size,-size)
stroke()

mklabels(size, r"$x$", size, r"$y$")

endfigure()
