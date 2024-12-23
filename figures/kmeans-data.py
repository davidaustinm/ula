from figures import *

width = 175
height = width
margin = 5

size = 3

points = [[-2,1], [1,1], [1,2], [3,2]]

beginfigure("kmeans-data", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2,-2,3,3])

xr = [-2,1,size]

settexenv('ACTexConfig')

Grid(xr, xr).draw()

axes = Axes()
axes.setticks(xr,xr)
axes.setlabels([-2,1,size], [-2,1,size])
axes.draw()
axes.drawticks()
axes.drawlabels()

for p in points:
    p = Point(p, 3, fillcolor=lightblue)
    p.fill()
    p.draw()

Label(r"${\mathbf v}_1$", points[0], alignment="lt", offset=[4,-4]).draw()    
Label(r"${\mathbf v}_2$", points[1], alignment="lt", offset=[4,-4]).draw()    
Label(r"${\mathbf v}_3$", points[2], alignment="rb", offset=[-4,4]).draw()    
Label(r"${\mathbf v}_4$", points[3], alignment="rb", offset=[-4,4]).draw()    

endfigure()
