from figures import *

width = 150
height = width
margin = 5

beginfigure("2d-span-plane", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, width+margin],
                 [0, 0, width, height])

gsave()

box(0,0,width,height)
fill(lightgray)

size = 4
setupcoordinates([0,0,width,height], [-size, -size, size, size])

axes = Axes()
axes.draw()

v = [2,1]
w = [1,2]

Vector(v, fillcolor=darkgray, color=darkgray).shade()
Vector(w, fillcolor=darkgray, color=darkgray).shade()

Label(r"$\mathbf v$", v, offset=[4,-4], alignment="lt").draw()
Label(r"$\mathbf w$", w, offset=[-4,4], alignment="rb").draw()
grestore()

box(0,0,width,height)
stroke()



endfigure()
