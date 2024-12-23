from figures import *
from math import *

width = 150
height = width
margin = 5
imargin = 20
size = 6

trajectorycolor = lightblue
pointcolor = lightred

lam1 = 1
lam2 = 1.5
points = [[1,0], [1,1],[2,2],[3,3],[0,3]]
points = [[2,0], [2,2], [4,2],[6,2],[0,2]]

iters = range(12)

def poncurve(p, k):
    return [lam1**k*p[0], lam2**k*p[1]]

def pointoncurve(p, k):
    p = Point(poncurve(p,k), 2)
    p.fill()

def trajectory(p):
    k = -0.8
    s = poncurve(p, k+0.3)
    t = poncurve(p,k)
    if length(vdiff(s,t)) > 0.1:
        v = Vector(poncurve(p, k+0.3), tail=poncurve(p,k),
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

    if labels:
        mklabels(size, r"$R$", size, r"$S$")
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
          
    grestore()
  
beginfigure("ex-predator-sol-b",
            2*width+2*margin+imargin, height+2*margin)

plot([1,0],[0,1], False)

translate(width+imargin,0)
plot([1,1],[1,2], True)

endfigure()
    
