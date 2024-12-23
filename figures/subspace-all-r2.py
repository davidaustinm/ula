from figures import *

width=100
height = width
margin = 5

size = 4
beginfigure("subspace-all-r2", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size, -size, size, size])

Grid([-size,1,size], [-size,1,size]).draw()

axes = Axes()
axes.draw()

def drawvect(v, c):
    v = Vector(v, fillcolor=c, color=c)
    v.fill()
#    v.draw()

v = [3,2]
w = [-2,2]
drawvect(v, blue)
drawvect(w, blue)

Label(r"${\mathbf v}$", v, alignment="lt", offset=[3,-3]).draw()
Label(r"${\mathbf w}$", w, alignment="rt", offset=[-3,-3]).draw()


endfigure()
 
