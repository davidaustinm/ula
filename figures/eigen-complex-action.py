from figures import *
from math import *

width=150
height=150
margin = 5
imargin = 20

P = [[1,1],[2,1]]
A = [[-2,2],[-5,4]]

r = sqrt(2)
theta = pi/4

size = 4
beginfigure("eigen-complex-action", width+2*margin,
            height+2*margin)

gsave()
setupcoordinates([margin,margin,width+margin,height+margin],
                 [-size,-size,size,size])

Grid([-size,1,size],[-size,1,size]).draw()

axes = Axes()
axes.draw()

def drawvec(v, color):
    vec = Vector(v, fillcolor=color, color=color)
    vec.fill()
#    vec.draw()

v = [1,2]
w = [v[0]-v[1], v[0]+v[1]]

drawvec(v, blue)
drawvec(w, blue)

Label(r"${\mathbf v}$", v, offset=[5,0], alignment="lc").draw()
Label(r"$C{\mathbf v}$", w, offset=[-5,0], alignment="rc").draw()

grestore()

'''
translate(width+imargin,0)

gsave()
setupcoordinates([margin,margin,width+margin,height+margin],
                 [-size,-size,size,size])

Grid([-size,1,size],[-size,1,size]).draw()

axes = Axes()
axes.draw()

def drawvec(v, color):
    vec = Vector(v, fillcolor=color, color=color)
    vec.fill()
    vec.draw()

v = [1,2]
w = [v[0]-v[1], v[0]+v[1]]

Pv = [P[0][0]*v[0] + P[0][1]*v[1],
      P[1][0]*v[0] + P[1][1]*v[1]
      ]

def matmult(m, v):
    return [m[0][0]*v[0]+m[0][1]*v[1],
            m[1][0]*v[0]+m[1][1]*v[1]]

APv = [A[0][0]*Pv[0] + A[0][1]*Pv[1],
       A[1][0]*Pv[0] + A[1][1]*Pv[1]
      ]

      

drawvec(Pv, blue)
drawvec(APv, blue)

for i in range(5):
    drawvec(Pv, blue)
    Pv = matmult(A, Pv)

Label(r"${\mathbf v}$", Pv, offset=[5,0], alignment="lc").draw()
Label(r"$A{\mathbf v}$", APv, offset=[-5,0], alignment="rc").draw()

grestore()
'''


endfigure()

 
