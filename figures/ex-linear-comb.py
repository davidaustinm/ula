from figures import *

width = 200
height = width
margin = 5

size = 10

beginfigure("ex-linear-comb", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-size,-size,size,size])

u = [3,1.6]
v = [-1,2]

Axes().draw()

gsave()
cliptoboundingbox()
atransform(u,v)
Grid([-10,1,10],[-10,1,10]).draw()
grestore()

vector = Vector(u, color=gray, fillcolor=gray)
vector.fill()
vector.draw()

vector = Vector(v, color=gray, fillcolor=gray)
vector.fill()
vector.draw()

Label(r"${\mathbf v}$", u, offset=[4,-4], alignment="lt").draw()
Label(r"${\mathbf w}$", v, offset=[-4,4], alignment="rb").draw()
 
points = [[[-1,0], r"$p$", [-4,4], "rb"],
          [[0,3], r"$q$", [-4,4], "rb"],
          [[2,3], r"$r$", [-4,4], "rb"],
          [[2,-3], r"$s$", [-4,4], "rb"],
          [[-3,-2], r"$t$", [-4,4], "rb"],
          [[-2,0.5], r"$u$", [-4,4], "rb"],
          [[3.5,1.5], r"$v$", [-4,4], "rb"]]

for point in points:
    pp = vsum(smult(point[0][0],u), smult(point[0][1],v))
    Point(pp, 2, fillcolor=black).fill()
    Label(point[1], pp, offset=point[2], alignment=point[3]).draw()

endfigure()
