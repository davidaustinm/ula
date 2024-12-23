from figures import *

width=175
height=175
lmargin = 20
rmargin = 5
beginfigure("partial-pivot-ex", width+lmargin+rmargin,
            height+lmargin+rmargin)

setupcoordinates([lmargin, lmargin, width+lmargin, height+lmargin],
                 [0,0,2,2])

Grid([0,0.5,2], [0,0.5,2]).draw()

axes = Axes()
axes.setticks([0,0.5,2], [0,0.5,2])
axes.setlabels([0,1,2], [0,1,2])
axes.draw()
axes.drawticks()
axes.drawlabels()

Graph(Function(lambda x: 2-x), color=blue).draw()
Graph(Function(lambda x: 1-0.0001*x), color=blue).draw()

endfigure()
 
