from figures import *

def outline(p,w,h):
    newpath()
    moveto(p[0]-w/2.0, p[1]-h/2.0)
    rlineto(w,0)
    rlineto(0,h)
    rlineto(-w,0)
    closepath()

def edge(p,q):
    newpath()
    moveto(p)
    lineto(q)
    stroke()

    vec = Vector(vsum(p, smult(0.5, vdiff(q,p))), arrowdims=[1,5],
                 tail=p, color=black)
    vec.fill()

def mid(p,q):
    return [(p[0]+q[0])/2.0, (p[1]+q[1])/2.0]

width = 150
height = 100

beginfigure("eigen-3d-species", width, height)
setupcoordinates([0,0,width,height],[-2.5,-1,5.5,4])

settexenv("ACTexConfig")

jp = [2,3]
yp = [4,0]
ap = [0,0]

jpwidth = 2
jpheight= 1

ypwidth = 2.25
ypheight= 1

apwidth = 1.5
apheight = 1

edge(jp, yp)
edge(yp, ap)
edge(ap, jp)

outline(jp,jpwidth,jpheight)
fill(1)
stroke()
outline(yp,ypwidth,ypheight)
fill(1)
stroke()
outline(ap,apwidth,apheight)
fill(1)
stroke()

from math import *
newpath()
gsave()
gs = revert()
translate(gs.transform(ap[0]-apwidth/2.0, ap[1]+apheight/2.0))
arcarrow([0,0], 8, 0, pi*1.5 )
fill()
grestore()

Label(r"40\%", mid(ap,jp), alignment="rb", offset=[-4,0]).draw()
Label(r"80\%", mid(yp,jp), alignment="lb", offset=[4,0]).draw()
Label(r"90\%", mid(ap,yp), alignment="ct", offset=[0,-4]).draw()
Label(r"80\%", ap, alignment="cc", offset=[-35,20]).draw()


Label("Juveniles", jp, alignment="cc").draw()
Label("Yearlings", yp, alignment="cc").draw()
Label("Adults", ap, alignment="cc").draw() 

endfigure()
