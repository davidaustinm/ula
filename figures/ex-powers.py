from figures import *

width = 175
height = width
margin = 5

size = 4

def fig(s, m, x):

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
        x = [m[0][0]*x[0]+m[0][1]*x[1],
             m[1][0]*x[0]+m[1][1]*x[1]]
        v = Vector(x, fillcolor=blue, color=blue)
        v.fill()
        v.draw()
        d = data[i]
        if i == 0:
            Label(d[0], x, offset=d[1], alignment=d[2]).draw()
    
    #mklabels(size, r"$x$", size, r"$y$")
    
    endfigure()

fig("ex-power-a", [[1.4,0],[0,0.7]], [1,2])
fig("ex-power-b", [[0.6,0],[0,0.9]], [4,3])
fig("ex-power-c", [[1.2,0],[0,1.4]], [2,1])
fig("ex-power-d", [[0.95,0.25],[0.25,0.95]], [3,0])
