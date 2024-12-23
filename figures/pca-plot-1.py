from figures import *

width = 300
height = 50
margin = 10

beginfigure('pca-plot-1', width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-500, -5, 500, 5])

settexenv("ACTexConfig")
axes = Axes()
axes.sethlabels([-500, 100, 500])
axes.sethticks([-500, 100, 500])
axes.drawhticks()
axes.drawhlabels()

Label(r"0", [0,0], alignment="ct", offset=[0,-6]).draw()

newpath()
moveto(-500, 0)
lineto(500, 0)
stroke()

endfigure()

 
