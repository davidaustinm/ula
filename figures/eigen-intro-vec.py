from figures import *

width=175
height = width
margin = 5

size = 4
beginfigure("eigen-intro-vec", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size, -size, size, size])

Grid([-size,1,size], [-size,1,size]).draw()

axes = Axes()
axes.draw()
axes.setticks([-size,1,size], [-size,1,size])
axes.drawticks()

v = [1,2]
color = blue
vect = Vector(v, fillcolor=color, color=color)
vect.fill()
vect.draw()

Label(r"${\mathbf v}$", v, alignment="lt", offset=[3,-3]).draw()

endfigure()
 
