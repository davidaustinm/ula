from figures import *

width = 200
height = width
margin = 5

size = 6

def drawvec(v):
    Vector(v).fill()

beginfigure("ex2-1-1-a", width, height)
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

v = [1,-1]
w = [3,1]

drawvec(v)
drawvec(w)

mklabels(size, r"$x$", size, r"$y$")

endfigure()
