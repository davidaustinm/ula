from figures import *
from math import *

points = [[0, 1], [0, 0], [1, 1], [1, 0],
          [2, 1], [2, 0], [3, 1], [3, 0]]

radius = 15
scalefactor = 80.0

def showlabel(s):
    setfont("Palatino-Roman", 15)
    d = dimensions(s)
    moveto(0,0)
    rmoveto(-d[0]/2, -d[1]/2)
    show(s)

lightred = [1, 0.7, 0.7] 
def node(i):
    gsave()
    point = points[i]
    translate(point)
    scale(1/scalefactor)
    newpath()
    arc([0,0], radius, 0, 2*pi)
    closepath()
    fill(lightred)
    stroke()
    showlabel(str(i+1))
    grestore()

def arrow(sc):
    gsave()
    scale(1/sc)
    translate(-7,0)
    rotate(0)
    newpath()
    moveto(7,0)
    lineto(0,3)
    lineto(2,0)
    lineto(0,-3)
    closepath()
    fill()
    grestore()

def link(i, j):
    gsave()
    translate(points[i])
    diff = vdiff(points[j], points[i])
    rotate(atan2(diff[1], diff[0]))

    scale(length(diff))
    sc = scalefactor * length(diff)
    newpath()
    moveto(radius/sc,0)
    translate(1-radius/sc, 0)
    lineto(0,0)
    stroke()
    arrow(sc)
    grestore()
    
angle = 10 * pi/180
xc = 0.3 
yc = 0.08

def clink(i, j):
    gsave()
    translate(points[i])
    diff = vdiff(points[j], points[i])
    angle = atan2(diff[1], diff[0])
    rotate(angle)
    ldiff = length(diff)
    scale(ldiff)
    sc = scalefactor*ldiff
    x0 = radius/sc * cos(angle)
    y0 = radius/sc * sin(angle)
    newpath()
    moveto(x0, y0)
    curveto(xc, yc, 1-xc, yc, 1-x0, y0)
    stroke()
    translate(1-x0, y0)
    rotate(1.04*atan2(y0-yc, 1-x0-(1-xc)))
#    rotate(-angle/2)
    arrow(sc)
    grestore()

def nlink(i,j):
    link(i-1, j-1)

def nclink(i,j):
    clink(i-1, j-1)

beginfigure("reducible", 300, 150)

translate(30, 35)
scale(scalefactor)
N = len(points)

nlink(1,2)
nlink(1,3)
nclink(2,4)
nlink(3,2)
nlink(3,4)
nlink(3,5)
nclink(4,2)
nlink(4,5)
nlink(4,6)
nlink(5,6)
nclink(5,7)
nlink(5,8)
nclink(6,8)
nclink(7,5)
nclink(7,8)
nclink(8,6)
nclink(8,7)

angle = -30*pi/180
xc = 0.3
yc = -0.15
nclink(7,1)


for i in range(8):
    node(i)

endfigure()
