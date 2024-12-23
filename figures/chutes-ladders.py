from figures import *

dx = 25
width = dx*8
height = dx*3
margin = 5

def showlabel(l):
    gsave()
    gs = revert()
    translate(gs.transform([0,0]))
    setfont("Palatino-Roman", 15)
    d = dimensions(l)
    moveto(0,0)
    rmoveto(-d[0]/2, -d[1]/2)
    show(l)
    grestore()

beginfigure("chutes-ladders", width+2*margin, height+2*margin)

gsave()
setupcoordinates([margin, margin, width+margin, height+margin],
                 [0,-1,8,2])

labels = ["1", "", "2", "3", "4", "5", "", "6"]

for i in range(8):
    gsave()
    translate(i, 0)
    newpath()
    box(0,0,1,1)
    if len(labels[i]) > 0:
        fill(lightgray)
    stroke()
    translate(0.5,0.5)
    showlabel(labels[i])
    grestore()

gsave()
setlinewidth(2)
newpath()
moveto(1.5,0)
quadto([3,-1.5],[4.5,0])
stroke()

newpath()
moveto(6.5,1)
quadto([3.5,2.5], [0.5,1])
stroke()
grestore()

grestore()

y0 = 11.5
vec = Vector([84,y0], tail=[79,y0], arrowdims=[1,7])
vec.fill()
vec.draw()

y0 = 73.5
x0 = 90
vec = Vector([x0-4, y0], tail=[x0+1,y0], arrowdims=[1,7])
vec.fill()
vec.draw()

 
endfigure()

