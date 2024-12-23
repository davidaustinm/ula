from figures import *

width=175
height=width
margin = 5

beginfigure('similar-vectors', width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-4,-4,4,4])

Grid([-4,1,4], [-4,1,4]).draw()

settexenv('ACTexConfig')
axes = Axes()
axes.draw()
axes.setticks([-4,1,4], [-4,1,4])
axes.setlabels([-4,1,4], [-4,1,4])
axes.drawticks()
axes.drawlabels()

v = [3,1]
w = [3,2]
u = [-2,3]

sw = 1
ad = [sw, 4*sw]

for p in [v,w,u]:
    Vector(p, fillcolor=blue).fill()

Label(r'${\mathbf v}$', v, offset=[3,3], alignment='lb').draw()
Label(r'${\mathbf w}$', w, offset=[3,3], alignment='lb').draw()
Label(r'${\mathbf u}$', u, offset=[3,3], alignment='lb').draw()

endfigure()    
