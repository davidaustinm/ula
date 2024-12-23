from figures import *

def Av(v):
    return [v[0] + 2*v[1], 2*v[0]+v[1]]

def drawvec(v, color):
    vec = Vector(v, fillcolor=color, color=color)
    vec.fill()
    vec.draw()
    
width=150
height=150
margin = 5
size=4

beginfigure("eigen-intro-1-m1", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

Grid([-size,1,size], [-size,1,size]).draw()

axes=Axes()
axes.draw()
axes.setticks([-size,1,size], [-size,1,size])
axes.setlabels([-2,2,2],[-2,2,2])
axes.drawticks()
axes.drawlabels()

v = [-1,1] 
u = Av(v)
vec = Vector(u, fillcolor=white, color=black)
vec.fill()
vec.draw()

drawvec(v, red)

endfigure()
 
