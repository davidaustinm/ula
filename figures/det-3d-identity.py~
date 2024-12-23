from fig3d import *

width=150
height=150
init3d("det-3d", width, height)
beginpage()

center()
translate(-25, -22)
#translate(-30, 0)
#scale3d(22, 10, 50)
scalefactor=23
scale3d(scalefactor, scalefactor, scalefactor)
seteye([0.4, 0.5, 1, 0])
setlight([3, 5, 10, 0])

gray = 0.8
fillcolor = [gray, gray, gray]
gray = 0.6
strokecolor=[gray, gray, gray]
facecolor=[0.8]*3

v1 = tofig([3,2,-0.5])
v2 = tofig([-0.7,2,0])
v3 = tofig([0,1, 3.5])
basis = [v1, v2, v3]

#basis = [tofig([1,0,0]), tofig([0,1,0]), tofig([0,0,1])]

cube = [[[0,0,0], [0,1,0], [1,1,0], [1,0,0]],
        [[0,0,1], [1,0,1], [1,1,1], [0,1,1]],
        [[1,0,0], [1,1,0], [1,1,1], [1,0,1]],
        [[0,0,0], [0,0,1], [0,1,1], [0,1,0]],
        [[0,0,0], [1,0,0], [1,0,1], [0,0,1]],
        [[0,1,0], [0,1,1], [1,1,1], [1,1,0]]]

def drawvec(v, color):
    newpath()
    print "in drawvec"
    arrow3dto([0,0,0], v, color)

faces = []
for f in cube:
    face = []
    for v in f:
        vertex = [0,0,0]
        for i in range(3):
            vertex = vadd(vertex, smult(v[i], basis[i]))
        face.append(vertex)
        print vertex
    faces.append(Face(face, facecolor))

          
solid = convexsurface(faces)
solidr = solid.reversed()

x0 = 4
y0 = 4
z0 = 4
figaxes(x0, y0, z0)
stroke()

axescolor=[0.4]*3

def interior(color, alpha):
    paint(solidr, blend(color,alpha, facecolor))
    figaxes(x0,y0,z0)
    stroke(blend(color, alpha, axescolor))
    outline(solidr, blend(color,alpha,axescolor))
    
    for vec in basis:
        drawvec(vec, blend(color, alpha, [0]*3))

for f in faces:
    if f.isvisible(get_eye()) == True:
        transparentface(f, facecolor, 0.5, interior)
        facetrace(f)
#        stroke(0.5)

newpath()
outline(solid,0.5)

basis.pop(1)
for v in basis:
    drawvec(v, [0.2]*3)

Label(r"${\mathbf v}_1$", v1, alignment="rc", offset=[-6,0]).draw()
Label(r"${\mathbf v}_2$", v2, alignment="lb", offset=[3,0], color=0.3).draw()
Label(r"${\mathbf v}_3$", v3, alignment="rb", offset=[-4,4]).draw()

 
endpage()
finish()
