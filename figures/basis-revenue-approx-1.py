from figures import *
from revenue import *
from revenuecoords import *

width = 130
height = 100
lmargin = 20
margin = 5

beginfigure("basis-revenue-approx-1",
            width+lmargin+margin, height+lmargin+margin)
setupcoordinates([lmargin, lmargin, width+lmargin, height+lmargin],
                 [0, 0, 4.5, 15])

axes = Axes()
axes.draw()
axes.setticks([0,1,4],[0,5,15])
axes.setlabels([0,1,4],[0,5,15])
axes.drawticks()
axes.drawlabels()

for datum in revenue:
    p = Point(datum, 2.5, fillcolor=red)
    p.fill()
    p.draw() 

Line([0, coords[0]], [4.5,coords[0]],color=blue,linewidth=2).draw()

settexenv("ACTexConfig")
Label(r"{\bf Quarter}", [4.5,0], offset=[-4,4], alignment="rb").draw()
Label(r"{\bf Revenue}", [0,15], offset=[4,-4], alignment="lt").draw()

endfigure()

 
