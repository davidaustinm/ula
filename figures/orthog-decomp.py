from figures import *

width = 175
height = width
margin = 5

v = [2,1]
w = [2,4]
a = dot(v,w)/float(dot(v,v))
bhat = smult(a,v)
bperp = vdiff(w,bhat)

print(w)
print(bhat)
print(bperp)

beginfigure("orthog-decomp", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-5,-5,5,5])

Grid([-5,1,5], [-5,1,5]).draw()

settexenv("ACTexConfig")

axes = Axes()
axes.setticks([-5,1,5],[-5,1,5])
axes.setlabels([-4,2,4], [-4,2,4])
axes.draw()
axes.drawticks()
axes.drawlabels()

gsave()
cliptoboundingbox()
Graph(Function(lambda x: 0.5*x), color=blue).draw()
Graph(Function(lambda x: -2*x), color=blue).draw()
grestore()

Vector(w).fill()
Vector(bhat).fill()
Vector(bperp).fill()

sc = 1.2
Label(r"$\widehat{\mathbf b}$", bhat, alignment="lt", scale=sc,
      offset=[2,-2]).draw()
Label(r"${\mathbf b}^\perp$", bperp, alignment="rt", scale=sc,
      offset=[-1,0]).draw()
Label(r"${\mathbf b}$", w, alignment="rb", scale=sc,
      offset=[-2,2]).draw()
Label(r"$L$", [5,2.5], alignment="rb", scale=sc, offset=[-2,2]).draw()
Label(r"$L^\perp$", [-2,4], alignment="rt", scale=sc, offset=[0,4]).draw()

endfigure()
 

