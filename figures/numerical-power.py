from figures import *
 
width=150
height=width
margin = 5

size = 8
beginfigure("numerical-power", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-1,-1,size,size])

Grid([-1,1,size], [-1,1,size]).draw()
axes = Axes()
axes.draw()
axes.setticks([-1,1,size], [-1,1,size])
axes.drawticks()

def drawvec(v, c):
    vec = Vector(v, fillcolor=c)
    vec.fill()

v = [1,0]
drawvec(v, red)
Label(r"${\mathbf x}_0$", v, alignment="lt", offset=[3,-3]).draw()

gsave()
cliptoboundingbox()
for i in range(3):
    v = [2*v[0]+v[1], v[0]+2*v[1]]
    drawvec(v, gray)
    Label(r"${\mathbf x}_" + str(i+1) + "$",
          v, alignment="lt", offset=[3,-3]).draw()


grestore()
endfigure()
