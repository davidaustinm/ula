from figures import *
from fig3d import *

init3d("animate-homogeneous", 210, 140)
beginpage()

seteye([0.63, 0.5, 0.8, 0])
#setlight([0,20,10, 0])

newpath()
center()
translate(0,-15)
scale(57,57,50)

def axes(s):
    newpath()
    moveto3d(0,0,0)
    lineto3d(s,0,0)
    moveto3d(0,0,0)
    lineto3d(0,s,0)
    moveto3d(0,0,0)
    lineto3d(0,0,s)

asc = 1.4
Label(r"$y$", [asc,0,0], alignment="lb", offset=[-3,3]).draw()
Label(r"$z$", [0,asc,0], alignment="lt", offset=[3,-3]).draw()
Label(r"$x$", [0,0,asc], alignment="rb", offset=[-3,3]).draw()

axes(asc)
stroke()

gsave3d()
scale(0.25,0.25,0.25)

newpath()
moveto3d(tofig([-4,-4,1]))
lineto3d(tofig([-4,4,1]))
lineto3d(tofig([4,4,1]))
lineto3d(tofig([4,-4,1]))
closepath3d()
fill(0.9)
clip()
newpath()
axes(4)
stroke(0.5)



newpath()
symgrid(tofig([0,0,1]), tofig([1,0,0]), tofig([0,1,0]), 4, 4)
stroke(lightgray)

newpath()
moveto3d(tofig([0,0,1]))
lineto3d(tofig([0,0,4*asc]))
stroke()
newpath()
moveto3d(tofig([0,-4,1]))
lineto3d(tofig([0,4,1]))
moveto3d(tofig([-4,0,1]))
lineto3d(tofig([4,0,1]))
stroke(0.4)

newpath()
moveto3d(tofig([0.5,0,1]))
lineto3d(tofig([0,0.5,1]))
lineto3d(tofig([-0.5,0,1]))
moveto3d(tofig([0,0.5,1]))
lineto3d(tofig([0,1.5,1]))
moveto3d(tofig([0.5,1.5,1]))
lineto3d(tofig([-0.5,0.5,1]))
stroke(blue)

from math import *
N = 200
t = 0
dt = 2*pi/N
a = 0.25
b = 0.5
x0 = 0
y0 = 2
newpath()
moveto3d(tofig([x0+a, y0,1]))
for i in range(N):
    t += dt
    lineto3d(tofig([x0+a*cos(t), y0 + b*sin(t), 1]))
closepath3d()
stroke(blue)


grestore3d()


finish()
endpage()
