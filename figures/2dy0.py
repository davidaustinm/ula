from figures import *

width = 100
height = width
margin = 5

beginfigure("2dy0", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-2,-2,2,2])

axes = Axes()
axes.draw()

newpath()
moveto(-2,0)
lineto(2,0)
setlinewidth(2.5)
stroke(blue)

mklabels(2, r"$x$", 2, r"$y$")

endfigure()
