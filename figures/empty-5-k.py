from figures import *

width = 175
height = width
margin = 5

size = 5

beginfigure("empty-5-k", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1,-1,size,size])

xr = [-1,1,size]

settexenv('ACTexConfig')

Grid(xr, xr).draw()

axes = Axes()
axes.setticks(xr,xr)
axes.setlabels([-1,1,size], [-1,1,size])
axes.draw()
axes.drawticks()
axes.drawlabels()

endfigure()
