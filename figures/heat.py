from figures import *

dx = 30
width = 4*dx
height = 3*dx
margin = 20

beginfigure("heat", width + 2*margin, height + 2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [0,0,4,3])

Grid([0,1,4],[0,1,3], color=black).draw()

off = 5
labels = [[[1,0], "10", "ct", [0,-off]],
          [[2,0], "20", "ct", [0,-off]],
          [[3,0], "30", "ct", [0,-off]],
          [[0,1], "10", "rc", [-off,0]],
          [[0,2], "10", "rc", [-off,0]],
          [[4,1], "40", "lc", [off,0]],
          [[4,2], "30", "lc", [off,0]],
          [[1,3], "15", "cb", [0,off]],
          [[2,3], "20", "cb", [0,off]],
          [[3,3], "25", "cb", [0,off]]]
          
for j in range(4):
    r = range(5)
    if j == 0 or j == 3:
        r.pop(0)
        r.pop(-1)
    for i in r:
        Point([i,j], 2, fillcolor=black).fill()

for l in labels:
    Label(l[1], l[0], offset=l[3], alignment=l[2]).draw()

off = 4

labels = [[[1,1], r"$T_4$", "rb", [-off,off]],
         [[2,1], r"$T_5$", "rb", [-off,off]],
         [[3,1], r"$T_6$", "rb", [-off,off]],
         [[1,2], r"$T_1$", "rb", [-off,off]],
         [[2,2], r"$T_2$", "rb", [-off,off]],
         [[3,2], r"$T_3$", "rb", [-off,off]]
         ]

for l in labels:
    Label(l[1], l[0], offset=l[3], alignment=l[2]).draw()


endfigure()
