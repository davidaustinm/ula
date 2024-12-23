from figures import *
from math import *

def fsin(n,x):
    return sin((2*x-1)*n*pi/8.0)

def fig(n):
    axes = Axes()
    axes.draw()
    axes.setticks([0,1,4], [-1,1,1])
    axes.setlabels([0,1,4], [-1,1,1])
    axes.drawticks()
    axes.drawlabels()

    Graph(Function(lambda x: fsin(n,x)), color=gray).draw()

    for i in range(1,5):
        p = Point([i, fsin(n,i)], fillcolor=blue)
        p.fill()
        p.draw()

    Label(r"${\mathbf v}_"+str(n)+r"$", [0,1.0],
          alignment="lb", offset=[4,6]).draw()

width = 150
height= 120
lmargin = 20
margin = 5

beginfigure("fourier-sine-basis", 2*width + 2*lmargin+2*margin,
            2*height + 2*margin+2*margin)

gsave()
setupcoordinates([lmargin, height+2*margin+margin,
                  lmargin+width, 2*height+2*margin+margin],
                 [0,-1.25,4,1.25])
fig(1)
grestore()

gsave()
setupcoordinates([width+2*lmargin+margin, height+2*margin+margin,
                  2*width+2*lmargin+margin, 2*height+2*margin+margin],
                 [0,-1.25,4,1.25])
fig(2)
grestore()

gsave()
setupcoordinates([lmargin, margin,
                  lmargin+width, height+margin],
                 [0,-1.25,4,1.25])
fig(3)
grestore()
 
gsave()
setupcoordinates([width+2*lmargin+margin, margin,
                  2*width+2*lmargin+margin, height+margin],
                 [0,-1.25,4,1.25])
fig(4)
grestore()

endfigure()
    
    
