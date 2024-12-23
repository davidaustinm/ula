from figures import *

width = 140
height = 70
margin = 5

def drawvector(v, color):
    v = Vector(v, fillcolor = color, color=color)
    v.fill()
#    v.draw()

beginfigure("area-shear", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+2*margin, height + 2*margin],
                 [-2,-1,5,4])

v = [3,0]
w1 = [-1,3]
w2 = [2,3]
 
Axes().draw()

Graph(Function(lambda x: w1[1]), color=0.5).draw()

drawvector(v, blue)
drawvector(w1, blue)
drawvector(w2, blue)

Label(r"${\mathbf v}$", v, offset=[4,-4], alignment="lt").draw()
Label(r"${\mathbf w}_1$", w1, offset=[-4,4], alignment="rb").draw()
Label(r"${\mathbf w}_2$", w2, offset=[4,4], alignment="lb").draw()


endfigure()


