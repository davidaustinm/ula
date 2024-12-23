from figures import *
from math import *

width=150
height=width
margin = 5

beginfigure("ex-complex-polar", width+2*margin, height+2*margin)
setupcoordinates([margin,margin,width+margin,height+margin],
                 [-2,-2,2,2])

axes = Axes()
axes.draw()

p = [1,1.5]
angle = atan(p[1]/float(p[0]))

u = p

t = 0
N = 20
dt = angle/N
r = 0.5
moveto(r,0)
for i in range(N):
    t += dt
    lineto(r*cos(t), r*sin(t))
stroke()

rd = 1.3
Label(r"$\theta$", [r*rd*cos(angle/2), r*rd*sin(angle/2)],
      alignment="lc").draw()
Label(r"$\left[\begin{array}{rr} a \\ b \end{array}\right]$",
      u, alignment="lt", offset=[3,-3]).draw()

vect = Vector(u, fillcolor=blue, color=blue)
vect.fill()
vect.draw()

Label(r"$r$", smult(0.5,p), alignment="rb", offset=[-3,3]).draw()

endfigure()


