from figures import *
from revenue import *
from revenuecoords import *

width = 130
height = 100
lmargin = 20
margin = 5

beginfigure("basis-revenue-approx-3",
            width+lmargin+margin, height+lmargin+margin)
setupcoordinates([lmargin, lmargin, width+lmargin, height+lmargin],
                 [0, 0, 4.5, 15])

axes = Axes()
axes.draw()
axes.setticks([0,1,4],[0,5,15])
axes.setlabels([0,1,4],[0,5,15])
axes.drawticks()
axes.drawlabels()

y0 = coords[0]+coords[1]
y1 = coords[0]-coords[1]
#Line([0,coords[0]], [4.5,coords[0]], linewidth=2, color=blue).draw()
Line([0, y0], [2.5,y0],linewidth=2,color=gray).draw()
Line([2.5, y1], [4.5,y1],linewidth=2,color=gray).draw()

Line([0,revenue[0][1]], [1.5,revenue[0][1]], linewidth=2, color=blue).draw()
Line([1.5,revenue[1][1]], [2.5,revenue[1][1]], linewidth=2, color=blue).draw()
Line([2.5,revenue[2][1]], [3.5,revenue[2][1]], linewidth=2, color=blue).draw()
Line([3.5,revenue[3][1]], [4.5,revenue[3][1]], linewidth=2, color=blue).draw()

for datum in revenue:
    p = Point(datum, 2.5, fillcolor=red)
    p.fill()
    p.draw()

settexenv("ACTexConfig")
Label(r"{\bf Quarter}", [4.5,0], offset=[-4,4], alignment="rb").draw()
Label(r"{\bf Revenue}", [0,15], offset=[4,-4], alignment="lt").draw()

endfigure()

 
