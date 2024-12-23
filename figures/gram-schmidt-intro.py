from figures import *

width = 150
height = width
margin = 5

v = [1,1]
w = [0,2]

x0 = 3
beginfigure("gram-schmidt-intro", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-x0,-x0,x0,x0])

Grid([-x0,1,x0], [-x0,1,x0]).draw()

settexenv("ACTexConfig")

axes = Axes()
axes.setticks([-x0,1,x0], [-x0,1,x0])
axes.setlabels([-x0,1,x0], [-x0,1,x0])
axes.draw()
axes.drawticks()
axes.drawlabels()

Vector(v).fill()
Vector(w).fill()
 
Label(r"${\mathbf v}_1$", v, alignment="lt", offset=[4,-4]).draw()
Label(r"${\mathbf v}_2$", w, alignment="lb", offset=[4,4]).draw()
endfigure()


beginfigure("empty-3", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-x0,-x0,x0,x0])

Grid([-x0,1,x0], [-x0,1,x0]).draw()

settexenv("ACTexConfig")

axes = Axes()
axes.setticks([-x0,1,x0], [-x0,1,x0])
axes.setlabels([-x0,1,x0], [-x0,1,x0])
axes.draw()
axes.drawticks()
axes.drawlabels()

endfigure()
 




