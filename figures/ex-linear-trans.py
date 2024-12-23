from figures import *

width = 200
height = width
margin = 5

size = 4

beginfigure("ex-linear-trans", width, height)
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

def drawvec(u):
    vect = Vector(u, fillcolor=blue, color=blue)
    vect.fill()
    vect.draw()

v1 = [2,1]
v2 = [-1,1]
v3 = [-1,-2]

drawvec(v1)
drawvec(v2) 
drawvec(v3)

off = 5
sc = 1.0
Label(r"${\mathbf v}_1$", v1, offset=[off,-off],
      alignment="lt",scale=sc).draw()
Label(r"${\mathbf v}_2$", v2, offset=[-off,off],
      alignment="rb", scale=sc).draw()
Label(r"${\mathbf v}_3$", v3, offset=[-off,off],
      alignment="rb", scale=sc).draw()

mklabels(size, r"$x$", size, r"$y$")

endfigure()
