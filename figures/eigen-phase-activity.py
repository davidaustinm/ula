from figures import *

width = 150
height = width
margin = 5
imargin = 20
size = 6

trajectorycolor = lightblue
pointcolor = lightred

lam1 = 1.4
lam2 = 0.8
points = [[1,0], [1,1], [2,2], [3,3], [4,4], [5,5], [0,1]]

iters = [-4,-2,0,2,4]

def poncurve(p, k):
    return [lam1**k*p[0], lam2**k*p[1]]

def pointoncurve(p, k):
    p = Point(poncurve(p,k), 2)
    p.fill()

def trajectory(p):
    k = 1.3
    v = Vector(poncurve(p, k+0.1), tail=poncurve(p,k),
               arrowdims=[1,5], fillcolor=blue).fill()
    ParametricCurve(Function(lambda x: poncurve(p,x)[0]),
                    Function(lambda x: poncurve(p,x)[1]),
                    [-20,10], color=blue).draw()


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

    Axes().draw()
 
    '''
    for pp in points:
        traj(pp)
        traj([-pp[0], pp[1]])
        traj([pp[0], -pp[1]])
        traj([-pp[0], -pp[1]])
    '''
    

    grestore()
        
    grestore()

beginfigure("eigen-phase-activity", 2*width+2*margin+imargin, height+2*margin)

plot([1,0],[0,1])

translate(width+imargin,0)
plot([1,1],[-1,1])

endfigure()
    
