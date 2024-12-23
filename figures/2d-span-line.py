from figures import *

width = 150
height = width
margin = 5

beginfigure("2d-span-line", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, width+margin],
                 [0, 0, width, height])

gsave()
size = 5
setupcoordinates([0,0,width,height], [-size, -size, size, size])

axes = Axes()
axes.draw()

v = [1,2]
w = [-2,-4]

gsave()
cliptoboundingbox()
Line([-5,-10], [5,10], color=gray).draw()
grestore()

Vector(v, fillcolor=gray, color=gray).shade()
Vector(w, fillcolor=gray, color=gray).shade()

Label(r"$\mathbf v$", v, offset=[-4,4], alignment="rb").draw()
Label(r"$\mathbf w$", w, offset=[4,-4], alignment="lt").draw()
grestore()

box(0,0,width,height)
stroke()



endfigure()
