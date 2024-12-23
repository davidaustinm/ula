from figures import *
from math import *

def fcos(n,x):
    return cos((2*x+1)*n*pi/16.0)

def fig(n):
    axes = Axes()
    axes.draw()
    axes.setticks([0,1,7], [-1,1,1])
    axes.setlabels([0,1,7], [-1,1,1])
    axes.drawticks()
    axes.drawlabels()

    Graph(Function(lambda x: fcos(n,x)), color=gray).draw()

    for i in range(8):
        p = Point([i, fcos(n,i)], fillcolor=blue)
        p.fill()
        p.draw()

    Label(r"${\mathbf v}_"+str(n)+r"$", [0,1.0],
          alignment="lb", offset=[4,6]).draw()

width = 150
height= 120
lmargin = 20
margin = 5

beginfigure("jpeg-fourier-basis", 2*width + 2*lmargin+2*margin,
            2*height + 2*margin+2*margin)

gsave()
setupcoordinates([lmargin, height+2*margin+margin,
                  lmargin+width, 2*height+2*margin+margin],
                 [0,-1.25,7,1.25])
fig(0)
grestore()

gsave()
setupcoordinates([width+2*lmargin+margin, height+2*margin+margin,
                  2*width+2*lmargin+margin, 2*height+2*margin+margin],
                 [0,-1.25,7,1.25])
fig(1)
grestore()

gsave()
setupcoordinates([lmargin, margin,
                  lmargin+width, height+margin],
                 [0,-1.25,7,1.25])
fig(2)
grestore()
 
gsave()
setupcoordinates([width+2*lmargin+margin, margin,
                  2*width+2*lmargin+margin, height+margin],
                 [0,-1.25,7,1.25])
fig(7)
grestore()

endfigure()
    
    
