from figures import *

grayscale = [25, 34, 30, 45, 190, 200, 195]

width=130
height=80
lmargin = 20
bmargin = 15
margin = 5

beginfigure('edges-grayscale', width+lmargin+margin, height+bmargin+margin)
setupcoordinates([lmargin, bmargin, width+lmargin, height+bmargin],
                 [0,0,6,255])

axes = Axes()
axes.setticks([0,1,6],[0,50,255])
axes.setlabels([0,1,6],[0,100,255])
axes.draw()
axes.drawticks()
axes.drawlabels()

for i in range(len(grayscale)):
    p = Point([i+1,grayscale[i]], 2.5, fillcolor=grayscale[i]/255.0)
    p.fill()
    p.draw()

endfigure()
 
