from figures import *

width = 200
height = width
margin = 5

size = 4

beginfigure("orthog-lines", width, height)
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

Line([-2,4], [2,-4]).draw()
Line([-4,-2], [4,2]).draw()
Vector([-1,2], arrowdims=[2,8]).fill()

Label(r"$L$", [1,-2], alignment='lb', offset=[3,3], scale=1.2).draw()
Label(r"$L^\perp$", [3,1.5], alignment='rb', offset=[-3,3], scale=1.2).draw()
Label(r"${\mathbf v}$", [-1,2], alignment='rt', offset=[-3,-3], scale=1.2).draw()

mklabels(size, r"$x$", size, r"$y$")

endfigure()
