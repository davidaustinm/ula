from figures import *

width=200
height=width
margin = 5
size = 5.5

beginfigure("eigen-basis", width+2*margin, height+2*margin)

setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size, -size, size, size])

v1 = [1,1]
v2 = [-1,1]

gsave()
cliptoboundingbox()
atransform(v1, v2)
Grid([-5,1,5], [-5,1,5]).draw()
Axes().draw()
grestore()

def drawvec(v, color):
    vec = Vector(v, fillcolor=color, color=color)
    vec.fill()
    vec.draw()

Axes(color=gray).draw()

drawvec(v1, black)
drawvec(v2, black)

x = vsum(smult(1,v1), smult(-2,v2))
Ax = vsum(smult(3,v1), smult(2,v2))

drawvec(x, red)
drawvec(Ax, gray)

Label(r"${\mathbf v}_1$", v1, alignment="lc", offset=[3,-1]).draw()
Label(r"${\mathbf v}_2$", v2, alignment="rc", offset=[-3,-1]).draw()
Label(r"${\mathbf x}$", x, alignment="lc", offset=[3,0]).draw()
Label(r"$A{\mathbf x}$", Ax, alignment="lc", offset=[3,0]).draw()

endfigure()

