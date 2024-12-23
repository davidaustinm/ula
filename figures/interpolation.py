points = [[0,2], [1,3], [2,0], [3, 1]]

from figures import *
width = 150
height = width
margin = 5

x0 = -1
x1 = 4
y0 = -1
y1 = 4

def f(x):
    return 2 + float(17)/3*x -6*x*x + float(4)/3*x*x*x

def fig(mode):
    beginfigure("interpolation-"+str(mode), width+2*margin, height + 2*margin)
    setupcoordinates([margin,margin,width+margin, height+margin],
                     [x0, y0, x1, y1])

    Grid([x0,1,x1],[y0,1,y1]).draw()
    axes = Axes()
    axes.draw()
    axes.setticks([x0,1,x1],[y0,1,y1])
    axes.setlabels([0,1,x1],[0,1,y1])
    axes.drawticks()
    axes.drawlabels()

    
    if mode == 1:
        gsave()
        cliptoboundingbox()
        Graph(Function(f), color=magenta).draw()
        grestore()

    for p in points:
        p = Point(p, 2.5, fillcolor=blue)
        p.fill()
        p.draw()

    endfigure()

fig(0)
fig(1)
    
    
        


        
        
