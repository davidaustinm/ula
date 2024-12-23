from figures import *
from math import*

x0 = -1
x1 = 4

width=175
height=width
margin = 5
beginfigure("dot-angle", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [x0,x0,x1,x1])

#Grid([x0,1,x1], [x0,1,x1]).draw()

axes = Axes()
axes.draw()
axes.setticks([x0,1,x1], [x0,1,x1])
axes.setlabels([x0,1,x1], [x0,1,x1])
#axes.drawticks()
#axes.drawlabels()

u = [3,1]
v = [2,3.5]
w = vdiff(v,u)

Vector(u).fill()
Vector(v).fill()
Vector(v, tail=u).fill()
Label(r"${\mathbf v}$", u, alignment="lt", offset=[3,-3]).draw()
Label(r"${\mathbf w}$", v, alignment="rb", offset=[-3,3]).draw()
Label(r"${\mathbf w}-{\mathbf v}$", vsum(smult(0.5,w), u),
      alignment="lb", offset=[3,3]).draw()

a1 = math.atan2(u[1],u[0])
a2 = math.atan2(v[1],v[0])
setrad()
newpath()
arc(0,0,0.7,a1,a2)
stroke()
Label(r"$\theta$", smult(0.15, vsum(u,v)), alignment="cc", offset=[0,0]).draw()

 
endfigure()
