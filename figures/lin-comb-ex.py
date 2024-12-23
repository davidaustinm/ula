from figures import *

width = 200
height = width
margin = 5

size = 4

beginfigure("lin-comb-ex", width, height)
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

newpath()
moveto(-size, size)
lineto(size, -size)
stroke(0.5)

v = [-1,1]
vec = Vector(v,fillcolor=blue,color=blue)
vec.fill()
vec.draw()

w = [2,-2]
vec = Vector(w,fillcolor=blue,color=blue)
vec.fill()
vec.draw()

Label(r"${\mathbf v}$", v, offset=[3,3],alignment="lb").draw()
Label(r"${\mathbf w}$", w, offset=[3,3],alignment="lb").draw()

mklabels(size, r"$x$", size, r"$y$")

endfigure()
