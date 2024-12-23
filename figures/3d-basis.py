from fig3d import *

init3d("3d-basis", 150, 150)
beginpage()

sc = 1.33
scale3d(sc, sc, sc)
seteye([0.7, 0.5, 0.8, 0])
#setlight([0,20,10, 0])

newpath()
center()
translate(0,-15)
scale(50,60,70)

moveto3d(0,0,0)
lineto3d(1,0,0)
moveto3d(0,0,0)
lineto3d(0,1,0)
moveto3d(0,0,0)
lineto3d(0,0,1)
stroke()
 
x0 = 0.6 
y0 = 0.6
z0 = 0.6
origin = [0,0,0]
blue = [0,0,1] 
arrow3dto(origin, tofig([x0, 0, 0]), blue)
arrow3dto(origin, tofig([0, y0, 0]), blue)
arrow3dto(origin, tofig([0, 0, z0]), blue)

Label(r"${\mathbf e}_1$", tofig([x0,0,0]), alignment="lc", offset=[4,-4]).draw()
Label(r"${\mathbf e}_2$", tofig([0,y0,0]), alignment="rb", offset=[4,4]).draw()
Label(r"${\mathbf e}_3$", tofig([0,0,z0]), alignment="lc", offset=[4,2]).draw()

Label(r"$y$", [1,0,0], alignment="lb", offset=[-3,3]).draw()
Label(r"$z$", [0,1,0], alignment="lt", offset=[3,-3]).draw()
Label(r"$x$", [0,0,1], alignment="rb", offset=[-3,3]).draw()


finish()
endpage()
