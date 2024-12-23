from figures import *

width = 150
height = width
margin = 5

size = 4

def fig(s, x, r):

    beginfigure(s, width, height)
    setupcoordinates([margin, margin, width-margin, height-margin],
                     [-size,-size,size,size])

    xr = [-size,1,size]
    
    Grid(xr, xr).draw() 

    axes = Axes()
    axes.setticks(xr,xr)
    axes.setlabels([-size,2,size], [-size,2,size])
    axes.draw()
    axes.drawticks()
    #axes.drawlabels()

    data = [[r"$A{\mathbf x}$", [3,3], "lb"],
            [r"$A^2{\mathbf x}$", [-3,5], "rb"],
            [r"$A^3{\mathbf x}$", [3,-3], "lt"],
            [r"$A^4{\mathbf x}$", [-3,5], "rb"]]
    
    for i in range(4):
        x = [-r*x[1], r*x[0]]
        v = Vector(x, fillcolor=blue, color=blue)
        v.fill()
        v.draw()
        d = data[i]
        Label(d[0], x, offset=d[1], alignment=d[2]).draw()
    
    #mklabels(size, r"$x$", size, r"$y$")
    
    endfigure()

fig("ex-comp-power-a", [1,0], 1.4)
fig("ex-comp-power-b", [3,0], 0.8)
fig("ex-comp-power-c", [2,0], 1)
