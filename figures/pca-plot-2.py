from figures import *

width = 300
height = 50
margin = 10
 
height=6*30

beginfigure('pca-plot-2', width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-500, -300, 500, 300])

Grid([-500, 100, 500], [-300,100,300]).draw()

settexenv("ACTexConfig")
axes = Axes()
axes.draw()
axes.setlabels([-500, 100, 500], [-300,100,300])
axes.setticks([-500, 100, 500], [-300,100,300])
axes.drawticks()
axes.drawlabels()

endfigure()


