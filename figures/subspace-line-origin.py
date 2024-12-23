from figures import *

width=150
height = width
margin = 5

size = 4
beginfigure("subspace-line-origin", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size, -size, size, size])

Grid([-size,1,size], [-size,1,size]).draw()

axes = Axes()
axes.draw()

Line([-size,-2], [size,2], color=blue, linewidth=2).draw()

endfigure()
 
