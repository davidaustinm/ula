from figures import *

width=200
height=30
margin = 10

beginfigure("numerical-power-line", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-20, -1, 20, 0.5])


l1 = 16.4
l2 = 0.75
lw = l1 - l2
newpath()
dy = 0.15
box(-l1, -dy, lw, 3.5*dy)
fill(lightgray)

newpath()
box(l2, -dy, lw, 3.5*dy)
fill(lightgray)

hash = 0.5
newpath()
moveto(l1,hash)
lineto(l1,-hash)
moveto(l2,hash)
lineto(l2, -hash)
stroke(blue)

newpath()
moveto(-20, 0)
lineto(20, 0) 
stroke()
axes = Axes()
axes.sethticks([-20,5,20])
axes.sethlabels([-20,10,20])
axes.drawhticks()
axes.drawhlabels()

Label(r"$\lambda_1$", [l1,-hash], alignment="ct", offset=[0,-4]).draw()
Label(r"$\lambda_2$", [l2,-hash], alignment="ct", offset=[0,-4]).draw()


endfigure()

