from figures import *

width = 200
height = 200
margin = 5

x0 = 1
x1 = 6
beginfigure("vector-addition-a", width+2*margin, height + 2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-x0, -x0, x1, x1])

Grid([-x0, 1, x1], [-x0, 1, x1]).draw()

axes = Axes()
axes.draw()

u = [3,1]
v = [2,3]

def drawvect(v, tail, fcolor, scolor):
    vector = Vector(v, tail = tail, fillcolor=fcolor, color=scolor)
    vector.fill()
    vector.draw()
 
w = vsum(u,v)
black = gray
drawvect(u, [0,0], black, black)
drawvect(w, u, black, black) 
drawvect(w, [0,0], blue, blue)

Label(r"$\mathbf v$", smult(0.6,u), offset=[4,-4], alignment="lt").draw()
Label(r"$\mathbf w$", vsum(u, smult(0.4,v)),
      offset=[4,-4], alignment="lt").draw()
Label(r"${\mathbf v} + {\mathbf w}$", w,
      offset=[-3,4], alignment="rb", color=blue).draw()
    
mklabels(x1, r"$x$", x1, r"$y$")

endfigure()
