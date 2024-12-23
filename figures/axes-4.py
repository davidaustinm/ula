from figures import *

width = 140
height = width
margin = 5

size = 4

beginfigure("x-axis-4", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-size,-size,size,size])

xr = [-size,1,size]

newpath()
moveto(-size,0)
lineto(size,0)
stroke()

axes = Axes(skipzero=False)
axes.sethticks(xr)
axes.sethlabels([-size,2,size])
axes.drawhticks()
axes.drawhlabels()

endfigure()

beginfigure("y-axis-4", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-size,-size,size,size])

xr = [-size,1,size]

newpath()
moveto(0,-size)
lineto(0,size)
stroke()

axes = Axes(skipzero=False)
axes.setvticks(xr)
axes.setvlabels([-size,2,size])
axes.drawvticks()
axes.drawvlabels()

endfigure()
