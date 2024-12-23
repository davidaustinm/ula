from figures import *

width=200
height=width
margin = 5
size = 7

beginfigure("ex-eigen-powers-sol", width+2*margin, height+2*margin)

setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size, -size, size, size])

v1 = [2,1]
v2 = [-1,1]

gsave()
cliptoboundingbox()
atransform(v1, v2)
Grid([-7,1,7], [-7,1,7]).draw()
Axes().draw() 
grestore()

def drawvec(v, color):
    vec = Vector(v, fillcolor=color, color=color)
    vec.fill()
    vec.draw()

Axes(color=gray).draw()

drawvec(v1, black)
drawvec(v2, black)

lambda1=-1
lambda2=2

c1 = -1
c2 = -2

x = vsum(smult(c1,v1), smult(c2,v2))
Ax = vsum(smult(lambda1*c1,v1), smult(lambda2*c2,v2))
AAx = vsum(smult(lambda1**2*c1,v1), smult(lambda2**2*c2,v2))
Am1x = vsum(smult(lambda1**-1*c1,v1), smult(lambda2**-1*c2,v2))

drawvec(x, red)
drawvec(Ax, blue)
drawvec(AAx, blue)
drawvec(Am1x, blue)

Label(r"${\mathbf v}_1$", v1, alignment="lc", offset=[3,-3]).draw()
Label(r"${\mathbf v}_2$", v2, alignment="rc", offset=[-3,-1]).draw()
Label(r"${\mathbf x}$", x, alignment="lc", offset=[3,0]).draw()
Label(r"${\mathbf Ax}$", Ax, alignment="lb", offset=[3,3]).draw()
Label(r"${\mathbf A^2x}$", smult(0.7,AAx), alignment="lc", offset=[3,3]).draw()
Label(r"${\mathbf A^{-1}x}$", Am1x, alignment="lt", offset=[3,-3]).draw()

endfigure()

 
