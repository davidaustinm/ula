from figures import *
from math import *


width = 180
height = width
margin = 5
x0 = 4

u = [2,1]
v = [1,2]
  
beginfigure("linearcomb", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-x0, -x0, x0, x0])
cliptoboundingbox()

grid = Grid([-5,1,5], [-5,1,5])
grid.draw()

axes = Axes()
axes.draw()

for i in range(-5,6):
    ui = smult(i,u)
    vi = smult(i,v)
    Line(vsum(ui,smult(-10,v)), vsum(ui, smult(10,v)),
         infinite=True, color=gray).draw()
    Line(vsum(vi,smult(-10,u)), vsum(vi, smult(10,u)),
         infinite=True, color=gray).draw()

Vector(u).fill()
Vector(v).fill()

Label(r"${\mathbf v}_1$", u, offset=[3,-3], alignment="lt").draw()
Label(r"${\mathbf v}_2$", v, offset=[3,0], alignment="lt").draw()
#Label(r"$E_{-1}$", [-4,4], offset=[-3,-3], alignment="rt").draw()
#Label(r"$E_{3}$", [-4,-4], offset=[-3,3], alignment="rb").draw()

endfigure()
