from figures import *

width=175
height=width
margin = 5

beginfigure('ex-eq-line', width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-2,-2,5,5])

Grid([-2,1,5],[-2,1,5]).draw()

settexenv('ACTexConfig')

axes = Axes()
axes.draw()
axes.setticks([-2,1,5], [-2,1,5])
axes.setlabels([-2,2,5], [-2,2,5])
axes.drawticks()
axes.drawlabels()

def f(x):
    return 3 - 0.5*x

gsave()
cliptoboundingbox()
Graph(Function(f), color=blue).draw()
grestore()

ad = [1,4]
Vector([2,2], arrowdims=ad).fill()
Vector([4,1], arrowdims=ad).fill()
Vector([3,4], tail=[2,2], arrowdims=ad).fill()
 
Label(r'${\mathbf n}$', [3,4], alignment='lt', offset=[3,-3]).draw()
Label(r'${\mathbf p}$', [1.5,1.5], alignment='rb', offset=[-1,1]).draw()
Label(r'${\mathbf x}$', [4,1], alignment='lb', offset=[3,3]).draw()

endfigure()

