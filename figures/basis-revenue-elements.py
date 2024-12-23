from figures import *

width=125
height=80
margin = 5
lmargin = 15

def chart(element, label):
    axes = Axes()
    axes.setticks([0,1,4],[-1,1,1])
    axes.setlabels([0,1,4],[-1,1,1])
    axes.draw()
    axes.drawticks()
    axes.drawlabels()

    for i in range(4):
        point = Point([i+1,element[i]], 2.5, fillcolor=blue)
        point.fill()
        point.draw()

    Label(label, [0,1.0], offset=[4,0],alignment="lb").draw()


beginfigure("basis-revenue-elements",
            2*width+2*margin+2*lmargin,
            2*height+3*margin+lmargin)

gsave()
translate(lmargin, height+2*margin+lmargin)
setupcoordinates([0, 0, width, height],
                 [0,-1.25, 4.5,1.25])

chart([1,1,1,1], r"${\mathbf v}_1$")
grestore()
 
gsave()
translate(2*lmargin + width+margin, height+2*margin+lmargin)
setupcoordinates([0, 0, width, height],
                 [0,-1.25, 4.5,1.25])

chart([1,1,-1,-1], r"${\mathbf v}_2$")
grestore()

gsave()
translate(lmargin, margin)
setupcoordinates([0, 0, width, height],
                 [0,-1.25, 4.5,1.25])

chart([1,-1,0,0], r"${\mathbf v}_3$")
grestore()

gsave()
translate(2*lmargin + width+margin, margin)
setupcoordinates([0, 0, width, height],
                 [0,-1.25, 4.5,1.25])

chart([0,0,1,-1], r"${\mathbf v}_4$")
grestore()

endfigure()
