from figures import *

width = 200
height = 120
margin = 5
lmargin = 20
bmargin = 15

beginfigure("ls-crickets", width+margin+lmargin, height+margin+bmargin)
setupcoordinates([lmargin, lmargin, width+bmargin, height+bmargin],
                 [10, 60, 24, 100])

settexenv("ACTexConfig")
   
data = [
    [20, 88.6],
    [16, 71.6],
    [19.8, 93.3],
    [18.4, 84.3],
    [17.1, 80.6],
    [15.5, 75.2],
    [14.7, 69.7],
    [15.7, 71.6],
    [15.4, 69.4],
    [16.3, 83.3],
    [15, 79.6 ],
    [17.2, 82.6],
    [16, 80.6 ],
    [17, 83.5 ],
    [14.4, 76.3]
] 



Grid([10, 2, 24], [60, 5, 100]).draw()

axes = Axes(frame="lb")
axes.setlabels([10, 2, 24], [60, 5, 100])
axes.setticks([10, 2, 24], [60, 5, 100])
axes.draw()
axes.drawticks()
axes.drawlabels()

for p in data:
    p = Point(p, 2.5, fillcolor=lightblue)
    p.fill()
    p.draw()

Label(r"$C$", [24,60], offset=[-4,4], alignment="rb").draw()
Label(r"$T$", [10,100], offset=[4,0], alignment="lt").draw()

endfigure() 
