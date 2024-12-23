from figures import *
from fig3d import *

init3d("plane-int-2", 120, 110)
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

newpath()
center()
translate(0,0)
scale(50,70,70)

def f(x,y):
    return 0.2*y

def g(x,y):
    return -0.5*y

def h(x,y):
    return -0.5*x

def triangle(p, f, g, fcolor, scolor):
    newpath()
    moveto3d(tofig([p[0][0], p[0][1], f(p[0][0], p[0][1])]))
    lineto3d(tofig([p[1][0], p[1][1], g(p[1][0], p[1][1])]))
    lineto3d(tofig([0,0,f(0,0)]))
    closepath()
    fill(fcolor)
    stroke(scolor)

def path(p0, p1):
    newpath()
    moveto3d(tofig(p0))
    lineto3d(tofig(p1))
    stroke(blue)

fgray = 0.7
ggray = 0.85
hgray = 0.78

x0 = 0.5
y0 = 0.65

xs = 1
ys = 1
zs = 0.75

gsave3d()
scale3d(xs, ys, zs)
triangle([[x0,-y0],[x0,y0]], f,g, hgray, 0.6)
grestore3d()

drawplane(x0, y0, f, fgray, 0.6)

gsave3d()
scale3d(xs, ys, zs)
triangle([[-x0,-y0],[x0,-y0]], g, f, hgray, 0.6)
path([x0,-y0, f(x0,-y0)], [0,0,0])
grestore3d()

drawplane(x0, y0, g, ggray, 0.7)

gsave3d()
scale3d(xs, ys, zs)
triangle([[-x0,y0],[x0,y0]], f, g, hgray, 0.6)
path([x0,y0, g(x0,y0)], [0,0,0])
grestore3d()

halfplane(x0, y0, f, fgray, 0.6)

gsave()
newpath()
moveto3d(tofig([x0,0,0]))
lineto3d(tofig([-x0,0,0]))
setlinewidth(2)
#stroke(blue)
grestore()

gsave3d()
scale3d(xs, ys, zs)
triangle([[-x0,-y0],[-x0,y0]], g, f, hgray, 0.6)

path([-x0,y0, f(-x0,y0)], [0,0,0])
path([-x0,-y0,g(-x0,-y0)], [0,0,0])
grestore3d()

path([x0, 0, 0], [0,0,0])
point([0,0,0], 1.5, 0,0)






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
