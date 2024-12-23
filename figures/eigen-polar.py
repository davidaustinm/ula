from figures import *
from math import *

width=150
height=150
margin = 5

beginfigure("eigen-polar", width+2*margin, height+2*margin)
setupcoordinates([margin,margin,width+margin,height+margin],
                 [-1,-1,5,5])

axes = Axes()
axes.draw()

a = 3
b = 4

angle = atan2(b,a)

newpath()
arc(0,0,0.5,0,angle)
stroke()

newpath()
moveto(0,0)
lineto(a,0)
lineto(a,b)
closepath()
stroke(blue)

p = Point([a,b], 2.5, fillcolor=blue)
p.fill()
p.draw()

Label(r"$(a,b)$", [a,b], offset=[6,0], alignment="lc").draw()
Label(r"$a$", [a/2.,0], offset=[0,-5], alignment="ct").draw()
Label(r"$b$", [a,b/2.], offset=[6,0], alignment="lc").draw()
Label(r"$r$", smult(0.5,[a,b]), offset=[-2,2], alignment="rb").draw()
Label(r"$\theta$", [0.5*cos(angle/2), 0.5*sin(angle/2)],
      offset=[4,4], alignment="lc").draw()


endfigure()

