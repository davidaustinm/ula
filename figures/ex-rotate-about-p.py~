from figures import *
from math import *

width = 150
height = width
margin = 5
imargin = 20

size = 2

p = [2,2.5]
angle = atan(p[1]/float(p[0]))

u = [-0.75, 1.5]
def T(x):
    s = sin(angle)
    c = cos(angle)
    return [(c*c-s*s)*x[0] + 2*s*c*x[1],
            2*s*c*x[0] + (s*s-c*c)*x[1]]

Tu = T(u)

def drawvector(x):
    vect = Vector(x, fillcolor=blue, color=blue)
    vect.fill()
    vect.draw()
    

beginfigure("ex-reflection-compose", 2*width+2*margin+imargin,
            2*height+2*margin+imargin)

# UL
gsave()
translate(0, height+imargin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

axes = Axes()
axes.draw()

gsave()
cliptoboundingbox()
Line([-2,-2.5],[2,2.5], linewidth=2).draw()
grestore()

drawvector(u)
Label(r"${\mathbf x}$", u, alignment="rt", offset=[-5,-5]).draw()
grestore()


# UR
gsave()
translate(width+imargin, height+imargin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

axes = Axes()
axes.draw()

cliptoboundingbox()
rotate(-angle)
gsave()
Line([-2,-2.5],[2,2.5], linewidth=2).draw()
grestore()

drawvector(u)
Label(r"$R({\mathbf x})$", u, alignment="lb", offset=[3,3]).draw()
grestore()


# LL
gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

axes = Axes()
axes.draw()

cliptoboundingbox()
rotate(-angle)
gsave()
Line([-2,-2.5],[2,2.5], linewidth=2).draw()
grestore()

drawvector(Tu)
Label(r"$S(R({\mathbf x}))$", Tu, alignment="lb", offset=[3,3]).draw()
grestore()


# LR
gsave()
translate(width+imargin, 0)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

axes = Axes()
axes.draw()

cliptoboundingbox()
gsave()
Line([-2,-2.5],[2,2.5], linewidth=2).draw()
grestore()

drawvector(Tu)
Label(r"$T(S(R({\mathbf x})))$", Tu, alignment="rt", offset=[-3,-5]).draw()
grestore()


endfigure()
