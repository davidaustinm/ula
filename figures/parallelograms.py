from figures import *

width = 100
height = 100
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
                     [-1,-1,size,size])

    Grid([-1,1,size], [-1,1,size]).draw()

    outline(v1, v2)
    fill(lightgray)

    gsave()
    outline(v1,v2)
    clip()
    Grid([-1,1,size], [-1,1,size], color=gray).draw()
    grestore()

    axes = Axes()
    axes.draw()
    axes.setticks([-1,1,size], [-1,1,size])
    axes.setlabels([0,1,size], [0,1,size])
    axes.drawticks()
    axes.drawlabels()

    outline(v1,v2)
    stroke()

    endfigure()

def parallelogram4(s, v1, v2, size):
    beginfigure(s, width+2*margin, height+2*margin)
    setupcoordinates([margin, margin, width+margin, height+margin],
                     [-1,-2,size,3])

    Grid([-1,1,size], [-1,1,size]).draw()

    outline(v1, v2)
    fill(lightgray)

    gsave()
    outline(v1,v2)
    clip()
    Grid([-1,1,size], [-1,1,size], color=gray).draw()
    grestore()

    axes = Axes()
    axes.draw()
    axes.setticks([-1,1,size], [-1,1,size])
    axes.setlabels([0,1,size], [0,1,size])
    axes.drawticks()
    axes.drawlabels()

    outline(v1,v2)
    stroke()

    endfigure()

parallelogram("parallelogram-a", [1,0],[0,1], 4)
parallelogram("parallelogram-b", [2,0],[0,3], 4)
parallelogram("parallelogram-c", [1,-1],[1,1], 4)
parallelogram("parallelogram-d", [2,0],[1,2], 4)
parallelogram("parallelogram-e", [2,0],[2,2], 4)
parallelogram("parallelogram-f", [2,0],[2,3], 4)
parallelogram("parallelogram-g", [1,2],[0.5,1], 4)
parallelogram("parallelogram-h", [1,0],[0,1], 4)
parallelogram("parallelogram-i", [1,0],[0,2], 4)
parallelogram4("parallelogram-j", [2,2],[2,-2], 4)
