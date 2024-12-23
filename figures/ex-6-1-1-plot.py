from figures import *

width = 200
height = width
margin = 5

size = 4

beginfigure("ex-6-1-1-plot", width, height)
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

v = [3,2]
w = [-1,3]
x = [-2,3]

ad = [1,4]
for p in [v, w, x]:
    Vector(p, fillcolor=black).fill()

Label(r'${\mathbf v}$', v, offset=[2,2], alignment="lb").draw()
Label(r'${\mathbf w}$', w, offset=[-2,2], alignment="rb").draw()
Label(r'${\mathbf x}$', x, offset=[-2,2], alignment="rb").draw()

mklabels(size, r"$x$", size, r"$y$")

endfigure()
