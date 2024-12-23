from figures import *

fwidth = 430
margin = 7
imargin = 20
fheight = fwidth

width = 2*fwidth+2*margin + imargin
height = fheight+2*margin

size = 2.5
size2 = 2*size

beginfigure("svd-logo", width, height)

gsave()
setupcoordinates([margin, margin, fwidth+margin, fheight+margin],
                 [-size, -size, size, size])

cliptoboundingbox()

u1 = [0.5257311121191336, 0.85065080835204]
u2 = [-0.85065080835204, 0.5257311121191336]
gsave()
atransform(u1, u2)
MGrid([-size2,1,size2], [-size2,1,size2]).draw()
ellipse = Ellipse([0,0], [1,1], color=blue, fillcolor=lightblue)
ellipse.fill()
ellipse.draw()

grestore()

axes = Axes()
axes.draw()
axes.setticks([-size,1,size], [-size,1,size])
axes.drawticks()

def drawvec(v, c):
    v = Vector(v, fillcolor=c, color=c)
    v.fill()
    v.draw()

drawvec(u1, blue)
drawvec(u2, blue)

grestore()

gsave()
setupcoordinates([margin+fwidth+imargin, margin, width-margin, fheight+margin],
                 [-size, -size, size, size])

cliptoboundingbox()

v1 = [0.8506508083520399, 0.5257311121191336]
v2 = [-0.5257311121191336, 0.8506508083520399]

s1 = 1.618033988749895
s2 = 0.6180339887498948

gsave()
atransform(v1,v2)

MGrid([-size2,1,size2], [-size2,1,size2]).draw()

Ellipse([0,0], [s1,s2], color=red).draw()
grestore()

axes = Axes()
axes.draw()
axes.setticks([-size,1,size], [-size,1,size])
axes.drawticks()

def drawvec(v, c):
    v = Vector(v, fillcolor=c, color=c)
    v.fill()
    v.draw()

drawvec(smult(s1, v1), red)
drawvec(smult(s2, v2), red)

grestore()

endfigure()

