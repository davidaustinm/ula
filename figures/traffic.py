from graph import *
from figures import *

dx = 60
margin = 10
width = 3*dx + 2*margin
height = dx + 20 + margin

upper = [0,5]
left = [-5,-2]
extras = [[[0.5,1], upper, "cb"],
          [[1.5,1], upper, "cb"],
          [[2.5,1], upper, "cb"],
          [[1,0.5], left, "rc"],
          [[2,0.5], left, "rc"],
          [[0.5,0], upper, "cb"],
          [[1.5,0], upper, "cb"],
          [[2.5,0], upper, "cb"]]

def fig(s, labels):
    beginfigure("traffic-"+s, width, height)
    setupcoordinates([margin, margin, 3*dx + margin, dx + margin],
                     [0,0,3,1])

    nodes = [[0,1],[1,1],[2,1],[3,1], [0,0],[1,0],[2,0],[3,0]]
    edges = [[0,1],[1,2],[2,3],[4,5], [5,6], [6,7], [1,5], [6,2]] 

    drawdirectedgraph(nodes, edges, 0, 0)

    for i in range(len(labels)):
        extra = extras[i]
        Label(labels[i], extra[0], offset=extra[1], alignment=extra[2]).draw()

    endfigure()

fig("a", ["650", r"$y$", "580", r"$x$", r"$w$", "150", r"$z$", "220"])
fig("b", [r"$x$", "100", r"260", r"$y$", r"$w$", "250", r"$z$", "390"])
