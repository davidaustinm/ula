from figures import *
from fig3d import *
import math

points = [[1,0,0], [1,1,0], [0,1,0],[-1,1,0],
          [-1,0,0],[-1,-1,0],[0,-1,0],[1,-1,0]]

filename = "eigen-3d-saddle-d"

s0 = -0.5

width=160
margin = 0
height = 150
sc=1
init3d(filename, width, height)
beginpage()

translate(5,5)
newpath()
box(0,0,width-10,height-10)
clip()

gsave()
scale(sc)

#seteye([0.3, 0.25, 1, 0])
seteye([0.45, 0.3, 1, 0])
setlight([3,5,10, 0])

t0 = -1.4
t1 = 15


gsave()
gsave3d()

s = 40
translate(60, 40)
#scale3d(s,1.19*s,s)
scale3d(s,s,s)

xa = 2.5
ya = 2.2
za = 2.5
def axes(color):
    newpath()
    moveto3d(0,0,0)
    lineto3d(tofig([0,ya,0]))
    moveto3d(0,0,0)
    lineto3d(tofig([0,0, za]))
    moveto3d(0,0,0)
    lineto3d(tofig([xa, 0,0]))
    stroke(color)

rs = 0.8
thetas = 1
lamz = 1.1
lamy = 0.8
lamx = 0.6

def orbit(p, t):
    x = p[0]
    y = p[1]
    z = p[2]

    return [x*lamx**t, y*lamy**t, z*lamz**t]

def traj(p, domain, color):
    t0 = domain[0]
    t1 = domain[1]
    N = 100
    dt = (t1-t0)/float(N)
    t = t0
    newpath()
    moveto3d(tofig(orbit(p, t)))
    for i in range(N):
        t += dt
        lineto3d(tofig(orbit(p, t)))
    stroke(color)

newpath()
symgrid([0,0,0], tofig([0.5,0,0]), tofig([0,0.5,0]), 4,4)
stroke(lightgray)

axes(black)

setarrowdims(1,5)
s1 = s0+0.5
for p in points:
    traj(p, [t0,t1], blue)
    arrow3dto(tofig(orbit(p, s0)), tofig(orbit(p,s1)), blue)

s0 = 6
s1 = s0+2
p = [0,0,0.5]
traj(p, [-10,15], blue)
arrow3dto(tofig(orbit(p, s0)), tofig(orbit(p,s1)), blue)


Label(r"$x_1$", tofig([xa,0,0]), alignment="rt", offset=[-4,-4]).draw()
Label(r"$x_2$", tofig([0,ya,0]), alignment="rt", offset=[0,-4]).draw()
Label(r"$x_3$", tofig([0,0,za]), alignment="lt", offset=[4,-4]).draw()
grestore3d()
grestore()
grestore()

endpage()
finish()







