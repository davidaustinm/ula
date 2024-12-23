from figures import *
from math import *
from animate import *

size = 4

def head():
    a = 0.25
    b = 0.5
    x0 = 0
    y0 = 2
    t=0
    N = 200
    dt = 2*pi/N
    moveto(a+x0, y0)
    for i in range(N):
        t += dt
        lineto(a*cos(t) + x0, b*sin(t) + y0)
    closepath()

def draw():
    newpath()
    moveto(0.5,0)
    lineto(0,0.5)
    lineto(-0.5,0)
    moveto(0,0.5)
    lineto(0,1.5)
    moveto(0.5,1.5)
    lineto(-0.5,0.5)
    stroke(blue)
    Ellipse([0,2], [0.25,0.5], color=blue).draw()

beginfigure("animate-closeup-c", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-size,-size,size,size])

xr = [-size,1,size]

Grid(xr, xr).draw()

axes = Axes()
axes.draw()

scale(2)
translate(0,-2)
draw()

endfigure()
