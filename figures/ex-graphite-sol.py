from figures import *
from math import *

color = lightlightblue

width=200
height=width

v1 = [1,0]
v2 = [cos(2*pi/3),sin(2*pi/3)]

hexagon = [[0,0], [1,0], [2,1], [2,2], [1,2], [0,1]]

def coords(p):
    return vsum(smult(p[0],v1),smult(p[1],v2))

def ccell(p, c):
    gsave()
    translate(coords(p))
    newpath()
    moveto(coords(hexagon[0]))
    for p in hexagon:
        lineto(coords(p))
    closepath()
    stroke()

    for p in hexagon:
        vertex(p, c)

    grestore()

def cell(p):
    ccell(p, color)
    

def vertex(p, c):
    p = Point(coords(p), 6, fillcolor=c)
    p.fill()
    p.draw()

def lvertex(p,c,l):
    vertex(p,c)
    Label(l, coords(p), alignment="cc").draw()
            

beginfigure("ex-graphite-sol", width, height)
setupcoordinates([0,0,width,height],
                 [-1,-1,5,5])

cliptoboundingbox()

translate(0,0.25)
v = Vector(v1)
v.fill()
v.draw()

v = Vector(v2)
v.fill()
v.draw()

gsave()
translate(coords([-2,-4]))
for i in range(6):
    p = [2*i,i]
    for j in range(5):
        cell(p)
        p = vsum(p, [-1,1])

grestore()

ccell([0,0], yellow)

Label(r"${\mathbf v}_1$", v1, offset=[-6,-7], alignment = "rt").draw()
Label(r"${\mathbf v}_2$", v2, offset=[-6,-7], alignment = "rt").draw()

settexenv("ACTexConfig")
lvertex([0,0], yellow, r"{\bf 0}")

lvertex([1,1], lightgray, r"{\bf C}")

ccell([4,2], lightgray)
lvertex([4,2], lightgray, r"{\bf 1}")

Label(r"i.", v1, offset=[0,0], alignment="cc").draw()
Label(r"ii.", v2, offset=[0,0], alignment="cc").draw()
Label(r"iii.", vsum(v1, vsum(v1,v2)), offset=[0,0], alignment="cc").draw()

endfigure() 
 

