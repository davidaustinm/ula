from figures import *

width = 250
height = 180
lmargin = 15
margin = 5
 
size = 5
 
beginfigure("clustering-elbow-plot", width+lmargin+margin, height+lmargin+margin)
setupcoordinates([lmargin, lmargin, width+lmargin, height+lmargin],
                 [0, 0, 9, 4])

Grid([0,1,9], [0,0.25,4], color=0.9).draw()
Grid([0,1,9], [0,0.5,4], color=0.8).draw()

settexenv("ACTexConfig")

axes = Axes()
axes.setticks([0,1,9], [0,0.5,4])
axes.setlabels([0,1,9], [0,1,4])
axes.draw()
axes.drawticks()
axes.drawlabels()

Label(r"$k$", [9,0], alignment="rb", offset=[-3,3]).draw()
Label("Objective", [0,4], alignment="lt", offset=[3,-3]).draw()

points = [[2,3.9], [3,1.87], [4,1.09], [5,0.66],
         [6,0.416], [7,0.32], [8,0.28], [9, 0.245]]

newpath()
moveto(points[0])
for p in points:
    lineto(p)
stroke()

for p in points:
    p = Point(p, 2.5, fillcolor=lightblue)
    p.fill()
    p.draw()


endfigure()
