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
init3d("pca-proj", int(sc*width)+10, int(sc*height)+10)
beginpage()

translate(5,5)
newpath()
box(0,0,width,height)
clip()
newpath()

gsave()
 
scale(sc)


#seteye([0.3, 0.25, 1, 0])
seteye([0.45, 0.5, 1, 0])
setlight([3,5,10, 0])

gsave()
gsave3d()

s = 70
translate(90, 60)
#scale3d(s,1.19*s,s)
scale3d(s,s,s)

xa = 1.6
ya = 1.3
za = 1.2
def axes(color):
    newpath()
    moveto3d(0,0,0)
    lineto3d(2*ya,0,0)
    moveto3d(0,0,0)
    lineto3d(0,za,0)
    moveto3d(0,0,0)
    lineto3d(0,0,xa)
    stroke(color)

e1 = smult(0.5, tofig([1,0.3,-0.15]))
e2 = smult(0.5, tofig([-0.2,1,0.2]))
e3 = cross(e1,e2)

a = 1.5
b = 1.7
w = vsum(smult(5.6, e3), vsum(smult(a,e1), smult(b,e2)))
proj = vsum(smult(a,e1), smult(b,e2))

def lincomb(a,v1,b,v2):
    return vadd(smult(a,v1), smult(b,v2))

t0 = 2.5
t1 = t0

gsave()
newpath()
moveto3d(lincomb(-t0,e1,-t1, e2))
lineto3d(lincomb(t0,e1,-t1, e2))
lineto3d(lincomb(t0,e1,t1, e2))
lineto3d(lincomb(-t0,e1,t1, e2))
closepath()
fill(0.8)
clip()

newpath()
symgrid([0,0,0], e1, e2, 4,4)
stroke(gray)
origin = [0,0,0]

grestore()

newpath()
axes(black)

newpath()
moveto3d(w)
lineto3d(proj)
stroke()

delta = 0.2
dz = smult(0.4, e3)
dy = smult(delta, e2)

newpath()
moveto3d(proj)
rmoveto3d(dz)
rlineto3d(dy)
rlineto3d(smult(-1,dz))
stroke()

newpath()
arrow3dto(origin, e1, black)
arrow3dto(origin, e2, black)
arrow3dto(origin, w, black)
arrow3dto(origin, proj, black)
arrow3dto(proj, w, black)
 
dx = 4
#Label(r'$z$', [0,za,0], alignment="lt", offset=[dx,-dx]).draw()
#Label(r'$y$', [ya,0,0], alignment="rt", offset=[4,-dx]).draw()
#Label(r'$x$', [0,0,xa], alignment="rb", offset=[-dx,0]).draw()
Label(r'${\mathbf u}_1$', e1, alignment="lt", offset=[dx,-2]).draw()
Label(r'${\mathbf u}_2$', e2, alignment="rb", offset=[-dx,5]).draw()
Label(r'${\mathbf x}$', w, alignment="lt", offset=[dx+3,0]).draw()
Label(r'$\widehat{\mathbf x}$', proj, alignment="rt",
      offset=[-dx-4,-dx+2]).draw()
 
grestore3d()
grestore()

grestore()
box(1,1,width-2,height-2)
stroke()

endpage()
finish()





