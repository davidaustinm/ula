from figures import *

width=150
height=width
margin = 5

size = 1.5
beginfigure("numerical-power-norm", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

Grid([-size,0.5,size], [-size,0.5,size]).draw()
axes = Axes()
axes.draw()
axes.setticks([-1,1,size], [-1,1,size])
axes.drawticks()

def drawvec(v, c):
    vec = Vector(v, fillcolor=c)
    vec.fill()

newpath()
box(-1,-1,2,2)
stroke(gray)

v = [1,0]
drawvec(v, red)
Label(r"${\mathbf x}_0$", v, alignment="lt", offset=[3,-3]).draw()

gsave()
cliptoboundingbox()
for i in range(3):
    v = [2*v[0]+v[1], v[0]+2*v[1]]
    v = smult(1/float(v[0]), v)
    drawvec(v, gray)
    Label(r"$\bar{\mathbf x}_" + str(i+1) + "$",
          v, alignment="lc", offset=[4,0]).draw()


grestore()
endfigure()

