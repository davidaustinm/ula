from figures import *
from math import *

width = 100
height = 100
margin = 5
imargin = 30

def drawvector(v, color):
    v = Vector(v, fillcolor = color, color=color)
    v.fill()
#    v.draw()

beginfigure("det-orientation", 2*width+3*margin+imargin, height+2*margin)

gsave()
setupcoordinates([margin, margin, width+margin, height + margin],
                 [-1,-1,4,4])

v = [3,1]
w = [1.5,3]
av = atan2(v[1], v[0])
aw = atan2(w[1], w[0])
 
Axes().draw()

newpath()
arc([0,0], 1, av, aw)
stroke()

drawvector(v, blue)
drawvector(w, blue)

Label(r"${\mathbf v}_1$", v, offset=[4,-4], alignment="lt").draw()
Label(r"${\mathbf v}_2$", w, offset=[0,4], alignment="rb").draw()

grestore()

translate(width+imargin+margin, 0)

gsave()
setupcoordinates([margin, margin, width+margin, height + margin],
                 [-1,-1,4,4])

Axes().draw()

newpath()
arcn([0,0], 0.8, av, aw)
stroke()

drawvector(v, blue)
drawvector(w, blue)

Label(r"${\mathbf v}_2$", v, offset=[4,-4], alignment="lt").draw()
Label(r"${\mathbf v}_1$", w, offset=[0,4], alignment="rb").draw()

grestore()

endfigure()


