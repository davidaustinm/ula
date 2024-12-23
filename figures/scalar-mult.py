from figures import *

width = 200
height = 200
margin = 5

size = 6
beginfigure("scalar-mult", width+2*margin, height + 2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size, -size, size, size])

Grid([-size,1,size], [-size,1,size]).draw()

axes = Axes()
axes.draw()

u = [2,1]
v = []
l = [
    r"$-2{\mathbf v}$",
    r"$2{\mathbf v}$",
    r"$-{\mathbf v}$",
    r"${\mathbf v}$"
]

Line(smult(-3,u), smult(3,u), color = gray).draw()

for s in [-2,2,-1,1]:
    v.append(smult(s, u))
    

for i in range(len(v)):
    vector = Vector(v[i], fillcolor=black)
    vector.fill()
    vector.draw()
    Label(l[i], v[i], offset=[4,-4], alignment="lt").draw()

vector = Vector(v[-1], fillcolor=gray, color=gray)
vector.fill()
vector.draw()
    

mklabels(size, r"$x$", size, r"$y$")

endfigure()
