from figures import *

def fig(s):
    width = 175
    height = width
    margin = 5
    
    size = 4
    
    beginfigure(s, width, height)
    setupcoordinates([margin, margin, width-margin, height-margin],
                     [-size,-size,size,size])
    
    xr = [-size,1,size] 
    
    settexenv('ACTexConfig') 
    Grid(xr, xr).draw()
    
    axes = Axes()
    axes.setticks(xr,xr)
    axes.setlabels([-size,2,size], [-size,2,size])
    axes.draw()
    axes.drawticks()
    axes.drawlabels()
    
    mklabels(size, r"$x$", size, r"$y$")

    add_on()
    
    endfigure()
    
def add_on():
    Vector([3,0], fillcolor=red).fill()
    Vector([1,0]).fill()
    
    Label(r'${\mathbf e}_1$', [1,0], alignment="lb", offset=[4,4]).draw()
    Label(r'$D{\mathbf e}_1$', [3,0], alignment="lb", offset=[4,4]).draw()

fig('diag-D-a')    

def add_on():
    Vector([0,1], fillcolor=red).fill()
    Vector([0,-1]).fill()
    
    Label(r'${\mathbf e}_2$', [0,1], alignment="lt", offset=[4,-4]).draw()
    Label(r'$D{\mathbf e}_2$', [0,-1], alignment="lt", offset=[4,-4]).draw()

fig('diag-D-b')    
def add_on():
    Vector([1,2], fillcolor=red).fill()
    Vector([3,-2]).fill()
    
    Label(r'${\mathbf e}_1 + {\mathbf e}_2$', [1,2], alignment="lt", offset=[4,-4]).draw()
    Label(r'$D({\mathbf e}_2 + {\mathbf e}_2$)', [3,-2], alignment="rt", offset=[-4,-4]).draw()

fig('diag-D-c')    
