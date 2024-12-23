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

width=150
height=150
radius = 0.5

ar = width/float(height)

beginfigure("google-cyclic", width, height)
setupcoordinates([0,0,width,height], [-3,-3,3,3])
settexenv("ACTexConfig")

points = []
angle = 0
rad = 2
for i in range(5):
    points.append([rad*cos(angle), rad*sin(angle)])
    angle += 2*pi/5

labels = ["1", "2", "3", "4", "5"]

straight = 10000
curve = 100

newpath()
box(5.25,-0.75,4.5,4.5)
fill(0.9)
stroke()

newpath()
link(0,1,straight)
link(1,2,straight)
link(2,3,straight)
link(3,4,straight)
link(4,0,straight)

for i in range(5):
    circ(points[i], labels[i])

endfigure()


