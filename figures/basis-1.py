from figures import *

v1 = [2,1]
v2 = [1,2]

width=175
height=width
margin = 3

size = 4
beginfigure("basis-1", width, height)
setupcoordinates([margin,margin,width-margin,height-margin],
                 [-size,-size,size,size])

Grid([-size,1,size], [-size,1,size]).draw()
Axes().draw()

cliptoboundingbox()
gsave()
atransform(v1,v2)
MGrid([-10,1,10],[-10,1,10], color=gray).draw()
grestore()

vect = Vector(v1, color=black, fillcolor=black)
vect.fill()
vect.draw()
vect = Vector(v2, color=black, fillcolor=black)
vect.fill()
vect.draw()

Label(r"${\mathbf v}_1$", v1, alignment="lt", offset=[4,-4]).draw()
Label(r"${\mathbf v}_2$", v2, alignment="rb", offset=[-4,4]).draw()
 
endfigure()

