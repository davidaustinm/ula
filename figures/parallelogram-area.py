from figures import *

width = 150
height = 80
margin = 5

def outline():
    newpath()
    moveto(0,0)
    lineto(v1)
    rlineto(v2)
    rlineto(smult(-1,v1))
    closepath()

beginfigure("parallelogram-area", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
#                 [-0.5,-0.5,5,5])
                 [-0.25,-0.75,6,3])

translate(-0.25, -0.25)

v1 = [4,0] 
v2 = [2.4, 2.9]
gsave()
#rotate(0.3)

outline()
fill(lightgray)

newpath()
moveto([v2[0], 0])
lineto(v2)
stroke(0.5)

outline()
stroke()

Label(r"$b$", smult(0.5,v1), offset=[0,-5], alignment="ct").draw()
Label(r"$h$", [v2[0], 0.5*v2[1]], offset=[6,0], alignment="lc").draw()

grestore()



endfigure()
