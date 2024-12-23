from figures import *
from math import *

width = 150
height = width
margin = 5
imargin = 20
size = 6

trajectorycolor = lightblue
pointcolor = lightred

lam1 = 0.5
lam2 = 2
points = [[1,0], [1,1],[2,2],[3,3],[0,3]]

iters = range(12)
iters = [-1,0,1,2]

def poncurve(p, k):
    return [lam1**k*p[0], lam2**k*p[1]]

def pointoncurve(p, k):
    p = Point(poncurve(p,k), 2)
    p.fill()

def trajectory(p):
    k = -0.5
    v = Vector(poncurve(p, k+0.1), tail=poncurve(p,k),
               arrowdims=[1,5], fillcolor=blue).fill()
    ParametricCurve(Function(lambda x: poncurve(p,x)[0]),
                    Function(lambda x: poncurve(p,x)[1]),
                    [-10,10], N=200, color=blue).draw()
 

def traj(p):
    trajectory(p)
    for k in iters:
        pointoncurve(p, k)

def plot(basis0, basis1, labels):
    gsave()
    setupcoordinates([margin, margin, width+margin, height+margin],
                     [-size,-size,size,size])

    Axes().draw()

    gsave()
    cliptoboundingbox()
    atransform(basis0, basis1)

    grid = 30
    MGrid([-grid,1,grid],[-grid,1,grid]).draw()

    for pp in points:
        traj(pp)
        traj([-pp[0], pp[1]])
        traj([pp[0], -pp[1]])
        traj([-pp[0], -pp[1]])


    grestore()
          
    if labels:
        mklabels(size, r"$R$", size, r"$S$")
    grestore()
  
beginfigure("ex-predator-sol-a",
            2*width+2*margin+imargin, height+2*margin)

plot([1,0],[0,1], False)

translate(width+imargin,0)
plot([1,0],[0.5,1.5], True)

endfigure()
    
