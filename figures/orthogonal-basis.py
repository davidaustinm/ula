from figures import *

width=150
height=width
margin = 5

beginfigure('orthogonal-basis', width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-2,-2,2,2])

Grid([-2,1,2], [-2,1,2]).draw()

settexenv('ACTexConfig')
axes = Axes()
axes.draw()
axes.setticks([-2,1,2], [-2,1,2])
axes.setlabels([-2,1,2], [-2,1,2])
axes.drawticks()
axes.drawlabels()

u = [1,2]
v = [-2,1]

Vector(u, fillcolor=blue).fill()
Vector(v, fillcolor=blue).fill()

Label(r'${\mathbf w}_1$', u, alignment="lt", offset=[3,-3]).draw()
Label(r'${\mathbf w}_2$', v, alignment="lb", offset=[3,3]).draw()
     
endfigure()
