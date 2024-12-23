from figures import *
from math import *

width = 150
height = width
margin = 5
imargin = 20
size = 6

trajectorycolor = lightblue
pointcolor = lightred

stretch = 1/1.5
rotate = 0.4
points = [[1.5,0], [2,0], [3,0], [4,0], [5,0]]

iters = [-4,-2, 0,2]

def poncurve(p, k):
    r = sqrt(p[0]**2 + p[1]**2)*stretch**k
    theta = atan2(p[1],p[0]) + k*rotate
    return [r*cos(theta), r*sin(theta)]

def pointoncurve(p, k):
    p = Point(poncurve(p,k), 2)
    p.fill()

def trajectory(p):
    k = 0.7
    v = Vector(poncurve(p, k+0.1), tail=poncurve(p,k),
               arrowdims=[1,5], fillcolor=blue).fill()
    ParametricCurve(Function(lambda x: poncurve(p,x)[0]),
                    Function(lambda x: poncurve(p,x)[1]),
                    [-10,7], color=blue).draw()


def traj(p):
    trajectory(p)
    for k in iters:
        pointoncurve(p, k)

def plot(basis0, basis1):
    gsave()
    setupcoordinates([margin, margin, width+margin, height+margin],
                     [-size,-size,size,size])

    Axes(color=gray).draw()
    gsave()
    cliptoboundingbox()
    atransform(basis0, basis1)

    MGrid([-10,1,10],[-10,1,10]).draw()
    
    for pp in points:
        for i in range(4):
            traj(pp)
            pp[0], pp[1] = -pp[1], pp[0]

    grestore()
        
    grestore()

beginfigure("eigen-phase-spirala", 2*width+2*margin+imargin, height+2*margin)

plot([1,0],[0,1])

translate(width+imargin,0)
plot([1,0.5],[-1,1])

endfigure()
    
