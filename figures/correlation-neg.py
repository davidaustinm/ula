from figures import *
from random import *
from math import *

seed(1)

width=150
height=150
margin = 5

beginfigure('correlation-neg', width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [0,-1.5, 10, 1.5])

vals = []
for i in range(11):
    vals.append(sin(i/2.0) + 0.3*random())

axes = Axes()
axes.draw()
axes.sethticks([0,1,10])
axes.drawhticks()

newpath()
moveto(0,vals[0])
for i, v in enumerate(vals):
    lineto(i,v)

stroke(blue)
for i, v in enumerate(vals):
    Point([i,v], 2.5, fillcolor=blue).fill()

color = orange
factor = -0.5    
newpath()
moveto(0,factor*vals[0])
for i, v in enumerate(vals):
    lineto(i,factor*v)

stroke(color)
for i, v in enumerate(vals):
    Point([i,factor*v], 2.5, fillcolor=color).fill()

endfigure()

    
    
    
