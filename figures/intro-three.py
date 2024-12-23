from figures import *

margin = 5
width = 100
height = width

def fig(lines):
    gsave()
    setupcoordinates([margin, margin, width+margin, height+margin],
                     [-4,-4,4,4])
    xr = [-4,1,4]
    Grid(xr, xr, color=lightgray).draw()
    newpath()
    axes = Axes()
    axes.setticks(xr,xr)
    axes.drawticks()
    axes.draw()

    cliptoboundingbox()
    for line in lines:
        Graph(Function(line), color=blue).draw()
    grestore()

beginfigure("intro-three", width+2*margin, height + 2*margin)

lines = [lambda x: x + 1]
lines.append(lambda x: 2*x-1)
lines.append(lambda x: -x )
fig(lines)

translate(width+2*margin,0)
translate(width+2*margin,0)


endfigure()

