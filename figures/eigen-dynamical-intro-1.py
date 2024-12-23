from figures import *

width = 150
height = width
margin = 5
imargin = 20
size = 8

trajectorycolor = lightblue
pointcolor = lightred

lam1 = 1.3
lam2 = 0.5
points = [[2,1]]

iters = [0,1,2,3,4]

def poncurve(p, k):
    return [lam1**k*p[0], lam2**k*p[1]]

def pointoncurve(p, k):
    p = Point(poncurve(p,k), 2)
    p.fill()

def trajectory(p):
    k = -1.3
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
    
    axes = Axes()
    axes.draw()

    vec = Vector([1,0])
    vec.fill()
    vec = Vector([0,1])
    vec.fill()
    
    
    for pp in points:
        traj(pp)

    Label(r"${\mathbf x}_0$", points[0],
          offset=[0,5], alignment="cb").draw()

    Label(r"${\mathbf v}_1$", [1,0],
          offset=[0,5], alignment="cb").draw()

    Label(r"${\mathbf v}_2$", [0,1],
          offset=[0,5], alignment="cb").draw()

    
    grestore()
        
    grestore()

beginfigure("eigen-dynamical-intro-1", width+2*margin, height+2*margin)

'''
plot([1,0],[0,1])
translate(width+imargin,0)
'''
plot([2,1],[-2,1])
 
endfigure()
    


