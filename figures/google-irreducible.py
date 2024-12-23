from figures import *
from math import *

def node(p,r):
    newpath()
    arc(p,r,0,2*pi)
    closepath()

def link(i,j, r):
    halfcurvearrow(points[i], points[j], r, arrowdims=[1,6])

def circ(p, l):
    gsave()
    gs = revert()
    translate(gs.transform(p))
    newpath()
    arc([0,0], 15, 0, 2*pi)
    closepath()
    fill(lightlightblue)
    stroke()

    setfont("Palatino-Roman", 15)
    d = dimensions(l)
    moveto(0,0)
    rmoveto(-d[0]/2, -d[1]/2)
    show(l)

#    Label(l, [0,0], scale=1.8, alignment="cc").draw()
    grestore()

width=300
height=150
radius = 0.5

ar = width/float(height)

beginfigure("google-irreducible", width, height)
setupcoordinates([0,0,width,height], [-1,-1, 10, 4.5])
settexenv("ACTexConfig")

points = [[0,3], [0,0], [3,3], [3,0], [6,3], [6,0], [9,3], [9,0]]
labels = ["1", "2", "3", "4", "5", "6", "7", "8"]

straight = 10000
curve = 100

link(0,1,straight)
link(0,2,straight)
link(1,3,curve)
link(2,1,straight)
link(2,4,straight)
link(3,1,curve)
link(3,5,straight)
link(4,5,straight)
link(4,6,curve)
link(4,7,straight)
link(5,7,curve)
link(6,4,curve)
link(6,7,curve)
link(6,0,-300)
link(7,5,curve)
link(7,6,curve)

for i in range(8):
    circ(points[i], labels[i])

endfigure()


