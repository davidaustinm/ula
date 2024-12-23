from figures import *

width=175
height=width
margin = 5
size = 6
beginfigure("ex-basis", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, width+margin],
                 [-size,-size,size,size])

Grid([-size,1,size],[-size,1,size]).draw()
axes = Axes()
axes.draw()
axes.setticks([-size,1,size],[-size,1,size])
axes.setlabels([-4,2,4],[-4,2,4])
axes.drawticks()
axes.drawlabels()


v1 = [-2,2]
v2 = [2,1]

gsave()
cliptoboundingbox()
atransform(v1,v2)
MGrid([-5,1,5],[-5,1,5], color=gray).draw()
grestore()

v = Vector(v1)
v.fill()
v.draw()

v = Vector(v2)
v.fill()
v.draw()

Label(r"${\mathbf v}_1$", v1, alignment="rb", offset=[-4,0]).draw()
Label(r"${\mathbf v}_2$", v2, alignment="lb", offset=[2,6]).draw()

endfigure()
 
