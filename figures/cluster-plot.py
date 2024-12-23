from figures import *

input = open('clusters_data.csv')
lines = input.readlines()
data = []
bound = [0,0,0,0]
for line in lines:
    line = line.strip()
    tokens = line.split(",")
    p = [float(tokens[0]), float(tokens[1])]
    data.append(p)
    if p[0] < bound[0]: bound[0] = p[0]
    if p[0] > bound[2]: bound[2] = p[0]
    if p[1] < bound[1]: bound[1] = p[1]
    if p[1] > bound[3]: bound[3] = p[1]

print (bound)

x0 = -3.5
x1 = 6.2
y0 = -1.5
y1 = 5.2

dx = 25
width= (x1-x0)*dx
height=(y1-y0)*dx
margin = 5
 
beginfigure('cluster-plot', width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [x0, y0, x1, y1])

settexenv('ACTexConfig')

Grid([-4,1,6], [-2,1,5]).draw()

axes = Axes()
axes.draw()
axes.setticks([-3,1,5], [-1,1,5])
axes.setlabels([-3,1,5], [-1,1,5])
axes.drawticks()
axes.drawlabels()

for p in data:
    Point(p, 1.5, fillcolor=blue).fill()

endfigure()
