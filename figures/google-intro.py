from figures import *
from math import *

def node(p,r):
    newpath()
    arc(p,r,0,2*pi)
    closepath()

def link(i,j):
    halfcurvearrow(points[i], points[j], 100, arrowdims=[1,6])

width=150
height=width
radius = 0.5

beginfigure("google-intro", width, height)
setupcoordinates([0,0,width,height], [-1,-1, 4,4])

points = [[0,3],[0,0],[3,1.5]]
labels = ["1", "2", "3"]

link(0,1)
link(1,0)
link(0,2)
link(2,0)
link(2,1)

for p in points:
    node(p, radius)
    fill(lightlightblue)
    stroke()

settexenv("ACTexConfig")
for i in range(len(labels)):
    Label(labels[i], points[i], scale=1.8, alignment="cc").draw()

endfigure()


