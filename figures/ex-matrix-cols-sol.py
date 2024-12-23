from figures import *

width = 200
height = width
margin = 5

size = 5.5

beginfigure("ex-matrix-cols-sol", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-size,-size,size,size])

u = [2,-0.5]
v = [-1,1.5]

Axes().draw()

gsave()
cliptoboundingbox()
atransform(u,v)
Grid([-12,1,12],[-12,1,12]).draw()
grestore()

vector = Vector(u, color=gray, fillcolor=gray)
vector.fill()
vector.draw()

vector = Vector(v, color=gray, fillcolor=gray)
vector.fill()
vector.draw()
 
#Label(r"${\mathbf v}_1$", u, offset=[4,-4], alignment="lt").draw()
Label(r"${\mathbf v}_2$", v, offset=[-4,4], alignment="rb").draw()
 
points = [
    [[-3,-3], r"${\mathbf b}$", [-4,4], "rb"],
    [[1,0], r"$A\left[\begin{array}{c}1 \\ 0 \\ \end{array}\right] = {\mathbf v}_1$", [4,-4], "lt"],
    [[2,3], r"$A\left[\begin{array}{c}2 \\ 3 \\ \end{array}\right]$", [4,10], "lt"],
    [[0,-3], r"$A\left[\begin{array}{c}0 \\ -3 \\ \end{array}\right]$", [-20,-15], "rb"],
    
]

for point in points:
    pp = vsum(smult(point[0][0],u), smult(point[0][1],v))
    vect = Vector(pp, fillcolor=black)
    vect.fill()
    vect.draw()
    Label(point[1], pp, offset=point[2], alignment=point[3]).draw()

endfigure()
