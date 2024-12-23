from figures import *
from math import *

def clipshadedline(points, color, closed):
    gsave()
    newpath()
    moveto(points[0])
    for v in points:
        lineto(v)
    closepath()
    clip()
    N = 10
    for i in range(N):
        gsave()
        setlinewidth((N-i)*0.8)
        newpath()
        moveto(points[0])
        for p in points:
            lineto(p)
        if closed: closepath()
        stroke(color + (1-color)*(i+1)/float(N))
        grestore()
    grestore()

def shadedline(points, color, closed):
    N = 10
    for i in range(N):
        gsave()
        setlinewidth((N-i)*0.8)
        newpath()
        moveto(points[0])
        for p in points:
            lineto(p)
        if closed: closepath()
        stroke(color + (1-color)*(i+1)/float(N))
        grestore()

def drawgraph(nodes, edges, strokecolor, fillcolor,
              pointsize = 2.5, linewidth=1,circlecolor=0.8,circles=True):
    N = len(nodes)
    newpath()
    for e in edges:
        moveto(nodes[e[0] % N])
        lineto(nodes[e[1] % N])
    setlinewidth(linewidth)
    stroke(strokecolor)
    if circles:
        for n in nodes:
            p = Point(n, pointsize, fillcolor = fillcolor, color=circlecolor)
            p.fill()
            p.draw()

def drawdirectedgraph(nodes, edges, strokecolor, fillcolor, circlecolor=0):
    N = len(nodes)
    newpath()
    for e in edges:
        mid = smult(0.5, vsum(nodes[e[0] % N], nodes[e[1] % N]))
        moveto(nodes[e[0] % N])
        lineto(nodes[e[1] % N])
        Vector(mid, nodes[e[0] % N], arrowdims=[1,5], fillcolor=fillcolor).fill()

    stroke(strokecolor)
    for n in nodes:
        p = Point(n, 2.5, fillcolor = fillcolor, color=circlecolor)
        p.fill()
        p.draw()        
        
def avg(nodes, indices):
    N = len(indices)
    p = [0,0]
    for i in indices:
        p = vsum(p, nodes[i])
    return smult(1/float(N), p)

def mycurveto(p,q,r,s):
    moveto(p)
    curveto(vsum(p,q), vsum(r,s), s)

def controlpoints(p):
    p0 = p[0]
    p1 = vsum(p[0],p[1])
    p2 = vsum(p[2],p[3])
    p3 = p[3]
    return [p0, p1, p2, p3]

def avg2(u,v):
    return smult(0.5, vsum(u,v))

def subdivide(b):
    q1 = avg2(b[0], b[1])
    q2 = avg2(b[1], b[2])
    q3 = avg2(b[2], b[3])
    q4 = avg2(q1, q2)
    q5 = avg2(q2, q3)
    q6 = avg2(q4, q5)
    return [[b[0], q1, q4, q6], [q6, q5, q3, b[3]]]

def endarrow(b, reverse, color):
    direction = vdiff(b[3], b[2])
    l = sqrt(direction[0]**2 + direction[1]**2)
    diff = smult(0.0001/l, direction)
    p = vdiff(b[3], diff)
    if reverse:
        p = vsum(b[3], diff)
    Vector(b[3], p, arrowdims=[1,6], fillcolor = color).fill()

def edgearrow(p, q, t, color):
    end = vsum(smult(1-t, p), smult(t, q))
    direction = vdiff(q,p)
    l = sqrt(direction[0]**2 + direction[1]**2)
    diff = smult(0.00001/l, direction)
    p = vdiff(end, diff)
    Vector(end, p, arrowdims=[1,5], fillcolor = color).fill()
    
    
    
