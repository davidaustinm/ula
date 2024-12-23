from figures import *
from fig3d import *

init3d("plane-int-3", 120, 110)
beginpage()

seteye([0.7, 0.5, 0.8, 0])
#setlight([0,20,10, 0])

def drawplane(x0, y0, f, fcolor, scolor):
    newpath()
    moveto3d(tofig([-x0,-y0,f(-x0,-y0)]))
    lineto3d(tofig([-x0,y0,f(-x0,y0)]))
    lineto3d(tofig([x0,y0,f(x0,y0)]))
    lineto3d(tofig([x0,-y0,f(x0,-y0)]))
    closepath()
    fill(fcolor)
    stroke(scolor)

def halfplane(x0, y0, f, fcolor, scolor):
    newpath()
    moveto3d(tofig([-x0,0,f(-x0,0)]))
    lineto3d(tofig([-x0,y0,f(-x0,y0)]))
    lineto3d(tofig([x0,y0,f(x0,y0)]))
    lineto3d(tofig([x0,0,f(x0,0)]))
    closepath()
    fill(fcolor)
    stroke(scolor)

def vertplane(x0, y0, z0, z1, fcolor, scolor):
    newpath()
    moveto3d(tofig([-x0,y0, z0]))
    lineto3d(tofig([x0, y0, z0]))
    lineto3d(tofig([x0, y0, z1]))
    lineto3d(tofig([-x0, y0, z1]))
    closepath()
    fill(fcolor)
    stroke(scolor)

newpath()
center()
translate(0,0)
scale(50,70,70)

def f(x,y):
    return 0.2*y

def g(x,y):
    return -0.5*y

fgray = 0.7
ggray = 0.85
hgray = 0.78
yp = -0.4
lv = 0.2
hv = -0.5
vertplane(0.5, yp, -0.4, yp*lv, hgray, 0.6)

drawplane(0.5, 0.65, f, fgray, 0.6)
vertplane(0.5, yp, yp*lv, yp*hv, hgray, 0.6)
drawplane(0.5, 0.65, g, ggray, 0.7)

halfplane(0.5, 0.65, f, fgray, 0.6)
vertplane(0.5, yp, yp*hv, 0.4, hgray, 0.6)

'''
newpath()
moveto3d(0,0,0)
lineto3d(1,0,0)
moveto3d(0,0,0)
lineto3d(0,1,0)
moveto3d(0,0,0)
lineto3d(0,0,1)
stroke()
 
Label(r"$y$", [1,0,0], alignment="lb", offset=[-3,3]).draw()
Label(r"$z$", [0,1,0], alignment="lt", offset=[3,-3]).draw()
Label(r"$x$", [0,0,1], alignment="rb", offset=[-3,3]).draw()
'''

finish()
endpage()
