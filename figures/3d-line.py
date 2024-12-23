from figures import *
from fig3d import *
import math

def avg(points):
    s = [0]*len(points[0])
    for p in points:
        s = vadd(s, p)
    return smult(1/float(len(points)), s)

width=190
margin = 0
height = 150
sc=1
init3d("3d-line", int(sc*width), int(sc*height))
beginpage()

scale(sc)

clip()

#seteye([0.3, 0.25, 1, 0])
seteye([0.5, 0.5, 1, 0])
setlight([3,5,10, 0])

gsave()
gsave3d()

s = 70
translate(90, 50)
#scale3d(s,1.19*s,s)
scale3d(s,s,s)

xa = 1.3
ya = 1.3
za = 1.3
def axes(color):
    newpath()
    moveto3d(0,0,0)
    lineto3d(ya,0,0)
    moveto3d(0,0,0)
    lineto3d(0,za,0)
    moveto3d(0,0,0)
    lineto3d(0,0,xa)
    stroke(color)

factor = 0.8

axes(0)
v1 = smult(0.5,[1,2,1])

t0 = -1.5
t1 = 1.7
newpath()
moveto3d(tofig(smult(t0,v1)))
lineto3d(tofig(smult(t1,v1)))
stroke(gray)

newpath()
arrow3dto([0,0,0], tofig(v1), black)


dx = 4
Label(r'$z$', [0,za,0], alignment="lt", offset=[dx,-dx]).draw()
Label(r'$y$', [ya,0,0], alignment="rb", offset=[-2,dx]).draw()
Label(r'$x$', [0,0,xa], alignment="rb", offset=[-dx,0]).draw()
Label(r'${\mathbf v}$', tofig(v1), alignment="rb", offset=[-dx,dx]).draw()


grestore3d()
grestore()

endpage()
finish()





