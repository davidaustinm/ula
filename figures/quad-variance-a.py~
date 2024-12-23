from figures import *

width=150
height=150
margin = 5

def project(p, v):
    return smult(dot(p,v)/float(dot(v,v)), v)

def fig(s, v):
    beginfigure(s, width+2*margin, height+2*margin)
    setupcoordinates([margin, margin, width+margin, height+margin],
                     [-4,-4,4,4])

    Grid([-4,1,4],[-4,1,4]).draw()
    settexenv('ACTexConfig')
    axes = Axes()
    axes.draw()
    axes.setticks([-4,1,4], [-4,1,4])
    axes.setlabels([-4,1,4], [-4,1,4])
    axes.drawticks()
    axes.drawlabels()
    
    points = [[-3,-3], [0,3], [3,0]]
    
    u1 = [1,1]
    u2 = [-1,1]

    newpath()
    moveto(smult(4, v))
    lineto(smult(-4, v))
    stroke(0.5)

    for p in points:
        newpath()
        p1 = project(p, v)
        newpath()
        moveto(p)
        lineto(p1)
        stroke(lightblue)
        newpath()
        pp = Point(p, 2.5, fillcolor=blue)
        pp.fill()
        pp.draw()
        pp = Point(p1, 2.5, fillcolor=lightgray)
        pp.fill()
        pp.draw()

    endfigure()

fig('quad-variance-a', [1,1])
fig('quad-variance-b', [-1,1])

    
