from figures import *
from math import *

def fcos(n,x):
    return cos((2*x+1)*n*pi/16.0)

def fig(points):
    axes = Axes()
    axes.draw()
    axes.setticks([0,1,7], [0,50,200])
    axes.setlabels([0,1,7], [0,50,200])
    axes.drawticks()
    axes.drawlabels()

    for i in range(len(points)):
        p = Point([i, points[i]], fillcolor=blue)
        p.fill()
        p.draw()

    Label(r"${\mathbf x}$", [0,1.25],
          alignment="lt", offset=[4,-4]).draw()

width = 150
height= 120
lmargin = 24
bmargin = 15
margin = 5

beginfigure("jpeg-luminance-col-graph", width + lmargin+margin,
            height + bmargin+margin)

gsave()
setupcoordinates([lmargin, bmargin,
                  lmargin+width, height+bmargin],
                 [0,0,7,200])
fig([176,181,165,139,131,131,140,150])
grestore()
  
endfigure()
    
    
