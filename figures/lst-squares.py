from figures import *
import random
import numpy as np
import numpy.linalg as LA

width=150
height=150
margin = 5

def line(x):
    return 0.5*x+1

random.seed(1)
N = 20
points = []
ppoints = []

for i in range(N):
    x = 5*random.random()-1
    y = line(x) + 0.25*random.random()
    points.append([1,x,y])
    ppoints.append([1,x,y])
    x = round(100*x)/100.0
    y = round(100*y)/100.0

pts = np.array(points)
print(pts.shape)
A = pts[:,:2]
b = pts[:,2]
print(A.shape)
print(b.shape)

y0, m = LA.lstsq(A, b)[0]

def line(x):
    return y0 + m*x

def fig(s, mode):
    beginfigure(s, width+2*margin, height+2*margin)
    setupcoordinates([margin, margin, width+margin, height+margin],
                     [-1,-1,4,4])

    settexenv('ACTexConfig')
    Grid([-1,1,4], [-1,1,4]).draw()

    axes=Axes()
    axes.draw()
    axes.setticks([-1,1,4], [-1,1,4])
    axes.setlabels([-1,1,4], [-1,1,4])
    axes.drawticks()
    axes.drawlabels()

    if mode == 1:
        Graph(Function(line), color=blue).draw()

    for p in ppoints:
        p = Point(p[1:], 2.5, fillcolor=lightred)
        p.fill()
        p.draw()

    Label(r'$x$', [4,0], offset=[-3,3], alignment='rb').draw()
    Label(r'$y$', [0,4], offset=[3,-3], alignment='lt').draw()

    endfigure()

fig('lst-squares-1', 0)    
fig('lst-squares-2', 1)    
        
