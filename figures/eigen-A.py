from figures import *

def fig(s):
    width = 175
    height = width
    margin = 5
    
    size = 5
    
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
    Vector([3,3], fillcolor=red).fill()
    Vector([1,1]).fill()
    
    Label(r'${\mathbf v}_1$', [1,1], alignment="lt", offset=[4,-4]).draw()
    Label(r'$A{\mathbf v}_1$', [3,3], alignment="lt", offset=[4,-4]).draw()

fig('eigen-A-a')    

def add_on():
    Vector([1,-1], fillcolor=red).fill()
    Vector([-1,1]).fill()
    
    Label(r'${\mathbf e}_2$', [-1,1], alignment="rb", offset=[-4,4]).draw()
    Label(r'$A{\mathbf e}_2$', [1,-1], alignment="lt", offset=[4,-4]).draw()

fig('eigen-A-b')    
def add_on():
    Vector([5,1], fillcolor=red).fill()
    Vector([-1,3]).fill()
    
    Label(r'${\mathbf v}_1 + {\mathbf v}_2$', [-1,3], alignment="rb",
          offset=[-4,4]).draw()
    Label(r'$A({\mathbf v}_2 + {\mathbf v}_2$)', [5,1], alignment="rb",
          offset=[-4,4]).draw()

fig('eigen-A-c')    
