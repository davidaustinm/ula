from figures import *

width = 175
height = width
margin = 5

size = 5

beginfigure("k-means-6-1", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1,-1,size,size])

xr = [-1,1,size]

settexenv('ACTexConfig')

Grid(xr, xr).draw()

axes = Axes()
axes.setticks(xr,xr)
axes.setlabels([-1,1,size], [-1,1,size])
axes.draw()
axes.drawticks()
axes.drawlabels()

v1 = [1,1]
v2 = [4,1]
v3 = [4,4]

centroid = [3,2]

def label(p, x):
    Label(r'${\mathbf v}_' + str(x) + '$', p,
          alignment="lt", offset=[3,-3]).draw()

for i, v in enumerate([v1,v2,v3]):
    c = Point(v, 2.5, fillcolor=lightblue)
    c.fill()
    c.draw()
    i += 1
    label(v, i)
          

c = Point(centroid, 2.5, fillcolor=lightred)
c.fill()
c.draw()

endfigure()
