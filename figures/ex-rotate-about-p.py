from figures import *
from math import *

width = 150
height = width
margin = 5
imargin = 20

size = 4

def drawvector(x, tail=[0,0]):
    vect = Vector(x, fillcolor=blue, color=blue, tail=tail)
    vect.fill()
    vect.draw()
    
v = [-2,-1]
v = [2,2]
Rv = [1,-2]
Rv = [-v[1], v[0]]
p = [1,2]
pv = vsum(v,p)
Rpv = vsum(Rv, p)

beginfigure("ex-rotate-about-p", 2*width+2*margin+imargin,
            2*height+2*margin+imargin)

# UL
gsave()
translate(0, height+imargin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

Grid([-size,1,size],[-size,1,size]).draw()
 
axes = Axes()
axes.draw()

drawvector(pv, tail=p)

point = Point(p, fillcolor=lightblue)
point.fill()
point.draw()

grestore()


# UR
gsave()
translate(width+imargin, height+imargin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

Grid([-size,1,size],[-size,1,size]).draw()

axes = Axes()
axes.draw()

drawvector(v)

grestore()


# LL
gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

Grid([-size,1,size],[-size,1,size]).draw()

axes = Axes()
axes.draw()

drawvector(Rv)
grestore()


# LR
gsave()
translate(width+imargin, 0)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

Grid([-size,1,size],[-size,1,size]).draw()

axes = Axes()
axes.draw()

drawvector(Rpv, tail=p)

point = Point(p, fillcolor=lightblue)
point.fill()
point.draw()

grestore()


endfigure()
