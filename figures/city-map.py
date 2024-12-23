from figures import *
from math import *

width = 175
height =width

size = 3.5

beginfigure("city-map", width, height)

gsave()
setupcoordinates([0,0,width,height],
                 [-size,-size,size,size])

u = [1,0.5]
v = [-0.5, 0.75]

angle = atan2(u[1],u[0])
vangle = atan2(v[1],v[0])

def lincomb(p):
    s = p[0]
    t = p[1]
    return vsum(smult(s,u), smult(t,v))

gsave()
atransform(u,v)
s = 20
MGrid([-s,1,s],[-s,1,s],color=0.5).draw()

Line([-5,-1], [5,-1], color=0.2).draw()
Line([2,-5], [2,5], color=0.2).draw()
grestore()

house = [-2,-1]
p = Point(lincomb(house), 2.5,fillcolor=blue)
p.fill()
p.draw()

store = [2,2]
p = Point(lincomb(store), 2.5,fillcolor=red)
p.fill()
p.draw()

settexenv("ACTexConfig")

Label(r"{\bf House}", lincomb(house), alignment="lt", offset=[5,-2]).draw()
Label(r"{\bf Store}", lincomb(store), alignment="rb", offset=[-5,2]).draw()

Label(r"{\bf Maple}", lincomb([-1,-1]), alignment="lb",
      offset=[3,3], angle = angle).draw()

Label(r"{\bf Main}", lincomb([2,1]), alignment="lb",
      offset=[3,3], angle = vangle-pi).draw()

grestore()

newpath()
vect = Vector([15, 130], tail=[15,100], color=black)
vect.fill()
vect.draw()

Label(r"{\bf N}", [15,120], alignment="lc", offset=[6,0], scale=1.2).draw()

newpath()
box(0,0,width,height)
setlinewidth(2)
stroke()


endfigure()
