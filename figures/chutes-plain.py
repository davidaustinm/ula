from figures import *

dx = 25
width = dx*8
height = dx*1
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

beginfigure("chutes-plain", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [0,0,8,1])

for i in range(8):
    gsave()
    translate(i, 0)
    box(0,0,1,1) 
    fill(lightgray)
    stroke()
    translate(0.5,0.5)
    showlabel(str(i+1))
    grestore()

endfigure()

