from figures import *

width = 150
height = 150
margin = 5

def outline(v1, v2):
    newpath()
    moveto(0,0)
    lineto(v1)
    rlineto(v2)
    rlineto(smult(-1,v1))
    closepath()
    
def parallelogram(s, v1, v2, size):
    beginfigure(s, width+2*margin, height+2*margin)
    setupcoordinates([margin, margin, width+margin, height+margin],
                     [-size,-size,size,size])

    Grid([-size,1,size], [-size,1,size]).draw()

    axes = Axes()
    axes.draw()
    axes.setticks([-size,1,size], [-size,1,size])
    axes.setlabels([-size,1,size], [-size,1,size])
    axes.drawticks()
    axes.drawlabels()

    outline(v1,v2)
    stroke(gray)

    endfigure()

def parallelogram4(s, v1, v2, size):
    beginfigure(s, width+2*margin, height+2*margin)
    setupcoordinates([margin, margin, width+margin, height+margin],
                     [-1,-2,size,3])

    Grid([-1,1,size], [-1,1,size]).draw()

    axes = Axes()
    axes.draw()
    axes.setticks([-1,1,size], [-1,1,size])
    axes.setlabels([0,1,size], [0,1,size])
    axes.drawticks()
    axes.drawlabels()

    outline(v1,v2)
    stroke(gray)

    endfigure()

parallelogram("parallelogram-g", [1,2],[-1,-2], 3)

