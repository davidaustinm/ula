from figures import *

width = 200
height = width
margin = 5

size = 6

def drawvec(v, c):
    Vector(v, fillcolor=c).fill()


beginfigure("ex2-1-1-b", width, height)
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

drawvec(smult(-3,v), gray)
drawvec(smult(2,w), gray)
drawvec(vsum(v,w), gray)
drawvec(vdiff(v,w), gray)

drawvec(v,0)
drawvec(w,0)

mklabels(size, r"$x$", size, r"$y$")

endfigure()
