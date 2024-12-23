from figures import *
from math import *

def avg(u,v,w):
    return smult(1/3.0, vsum(u, vsum(v,w)))

def mid(u,v):
    return smult(0.5, vsum(u,v))

def edge(u,v):
    gsave()
    gs = revert()
    gu = gs.transform(u)
    gv = gs.transform(v)
    gm = mid(gu,gv)
    n = vdiff(gu,gv)
    n = [-n[1], n[0]]
    n = smult(100/sqrt(n[0]**2 + n[1]**2), n)
    center = vsum(gm, n)

    uc = vdiff(gu, center)
    vc = vdiff(gv, center)
    a1 = atan2(uc[1], uc[0])
    a2 = atan2(vc[1], vc[0])
    rad = sqrt(uc[0]**2 + uc[1]**2)
    newpath()
    arcnarrow(center, rad, a1, a2)

    dangle = a2-a1
    arcnarrow(center, rad, a1, a1+dangle/2.0)
    fill()
    grestore()

def loop(p, offset, angles):
    gsave()
    gs = revert()
    translate(gs.transform(p[0]+offset[0], p[1]+offset[1]))
    newpath()
    arcarrow([0,0], 10, angles[0], angles[1])
    fill()
    grestore()

dx = 18
width= 8*dx
height=3*dx

beginfigure("ex-stoch", width, height)
setupcoordinates([0,0,width,height], [-2,-1.25,6,1.75])
 
setarrowdims(1,5)

P = [0,0]
Q = [4,0]

settexenv("ACTexConfig")

edge(P,Q)
edge(Q,P)

for p in [P,Q]:
    gsave()
    translate(p)
    newpath()
    box(-0.5,-0.5,1,1)
    fill(1)
    stroke()
    grestore()

Label("P", P, alignment="cc").draw()
Label("Q", Q, alignment="cc").draw()

loop(P, [-0.5,0.5], [0,3*pi/2])
loop(Q, [0.5,0.5], [-pi/2,pi])

dx = 1.3


endfigure()
