from figures import *
import numpy as np

dx = 15
width=10*dx
height=8*dx
margin = 5

beginfigure('orthog-comp', width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-5,-5,5,3])

corner = [-3,-3]
u = [8,2]
v = [-2,2]

center = vsum(corner, smult(0.5, vsum(u,v)))
p = [-u[1], u[0]]

def plane():
    newpath()
    moveto(corner)
    rlineto(u)
    rlineto(v)
    rlineto(smult(-1,u))
    closepath()

plane()
fill(0.8)
stroke()

cliptoboundingbox()

newpath()
moveto(center)
rmoveto(p)
rlineto(smult(-2,p))
stroke()

gsave()
plane()
clip()
newpath()
moveto(center)
rlineto(smult(-1,p))
stroke(0.5)
grestore()

plane()
stroke()

Label(r'$W$', [3,-2.5], alignment='cc', offset=[0,7]).draw()
Label(r'$W^\perp$', [0, 2], alignment='cc', offset=[0,0]).draw()

gsave()
translate(center)
sc = 0.05
du = smult(sc, u)
dup = smult(sc, p)
newpath()
moveto(du)
lineto(vsum(du, dup))
lineto(dup)
stroke()
grestore()

endfigure()
