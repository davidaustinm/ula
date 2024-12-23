from figures import *

width = 200
height = 200
margin = 5

size = 6
beginfigure("line-param", width+2*margin, height + 2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size, -size, size, size])

Grid([-size,1,size], [-size,1,size]).draw()

axes = Axes()
axes.draw()

u = [2,1]
w = [-1,3]
v = []
l = [
    r"$-2{\mathbf v}$",
    r"$2{\mathbf v}$",
    r"$-{\mathbf v}$",
    r"${\mathbf v}$"
]

Line(smult(-3,u), smult(3,u), color = gray).draw()
gsave()
cliptoboundingbox()
Line(vsum(w, smult(-4,u)), vsum(w, smult(4,u)), color = gray).draw()
grestore()

for s in [-2,2,-1,1]:
    v.append(smult(s, u))
    

for i in range(len(v)):
    vector = Vector(vsum(w, v[i]), tail=w,
                    fillcolor=lightgray, color = lightgray) 
    vector.fill()
    vector.draw()
    Label(l[i], vsum(w,v[i]), offset=[-4,4], alignment="rb").draw()

for i in range(len(v)):
    vector = Vector(vsum(w,v[i]), fillcolor=gray, color = gray)
    vector.fill()
    vector.draw()

gray = black
vector = Vector(u, fillcolor=gray, color=gray)
vector.fill()
vector.draw()
Label(r"$\mathbf v$", smult(1,u), offset=[4,-4], alignment="lt").draw()
    

vector = Vector(w, fillcolor=gray, color=gray)
vector.fill()
vector.draw()
Label(r"$\mathbf w$", smult(0.5,w), offset=[-6,4], alignment="rc").draw()

mklabels(size, r"$x$", size, r"$y$")

endfigure()
 
