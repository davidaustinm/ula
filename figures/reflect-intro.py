from figures import *

width=150
height=width
margin = 5
size = 4

beginfigure("reflect-intro", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

Grid([-size,1,size], [-size,1,size]).draw()

axes = Axes()
axes.draw()
axes.setticks([-size,1,size],[-size,1,size])
axes.drawticks()

def drawvec(v):
    vec = Vector(v, fillcolor=blue, color=blue)
    vec.fill()
    vec.draw()

v = [3,2]
Tv = [v[0],-v[1]]
drawvec(v)
drawvec(Tv)

Label(r"${\mathbf x}$", v, alignment="rb", offset=[-3,3]).draw()
Label(r"$T({\mathbf x})$", Tv, alignment="rt", offset=[-3,-3]).draw()
 
endfigure() 
