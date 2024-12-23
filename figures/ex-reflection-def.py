from figures import *
from math import *

width=150
height=width
margin = 5

beginfigure("ex-reflection-def", width+2*margin, height+2*margin)
setupcoordinates([margin,margin,width+margin,height+margin],
                 [-2,-2,2,2])

axes = Axes()
axes.draw()

p = [2,2.5]
angle = atan(p[1]/float(p[0]))

u = [-0.75, 1.5]
def T(x):
    s = sin(angle)
    c = cos(angle)
    return [(c*c-s*s)*x[0] + 2*s*c*x[1],
            2*s*c*x[0] + (s*s-c*c)*x[1]]

Tu = T(u)

gsave()
cliptoboundingbox()
Line([-2,-2.5],[2,2.5], linewidth=2).draw()
grestore()

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

vect = Vector(u, fillcolor=blue, color=blue)
vect.fill()
vect.draw()

vect = Vector(Tu, fillcolor=blue, color=blue)
vect.fill()
vect.draw()

Label(r"${\mathbf x}$", u, alignment="rt", offset=[-5,-5]).draw()
Label(r"$T({\mathbf x})$", Tu, alignment="rt", offset=[-5,-5]).draw()

Label(r"$L_\theta$", [1.5,1.5]).draw()

endfigure()

