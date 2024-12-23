from figures import *

width = 200
height = width
margin = 5

size = 5

def fig(filename, mode):
    beginfigure(filename, width, height)
    setupcoordinates([margin, margin, width-margin, height-margin],
                     [-size,-size,size,size])

    if mode == 0:
        u = [1,0]
        v = [0,1]
        l = r"$(2,-3)$"
        l1 = r"${\mathbf e}_1$"
        l2 = r"${\mathbf e}_2$"
    else:
        v = [1,2]
        u = [2,1]
        l = r"$\{2,-3\}$"
        l1 = r"${\mathbf v}_1$"
        l2 = r"${\mathbf v}_2$"

    gsave()
    atransform(u,v)
    Grid([-10,1,10],[-10,1,10]).draw()
    grestore()
    
    Axes().draw()
    
    vector = Vector(u, color=gray, fillcolor=gray)
    vector.fill()
    vector.draw()
    
    vector = Vector(v, color=gray, fillcolor=gray)
    vector.fill()
    vector.draw()
    
    w = vsum(smult(2,u), smult(-3,v))
    vector = Vector(w, color=black, fillcolor=black)
    vector.fill()
    vector.draw()
    
    Label(l1, u, offset=[4,-4], alignment="lt").draw()
    Label(l2, v, offset=[-4,4], alignment="rb").draw()
    Label(l, w, offset=[4,0], alignment="lc").draw()
    
    endfigure()

fig("ex-coord-std", 0)
fig("ex-coord-nonstd", 1)
 
