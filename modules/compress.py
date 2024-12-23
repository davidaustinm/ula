from PIL import Image
import numpy as np
import csv

def display_image(matrix):
    return Image.fromarray(matrix.astype('uint8'))

def approximation(A, k):
    u, s, v = np.linalg.svd(A)
    sigma = np.zeros(A.shape)
    for i in range(k):
        sigma[i][i] = s[i]
    return np.dot(u, np.dot(sigma, v))

def square(ll, dims, fillcolor, strokecolor):
    x, y = ll
    w, h = dims
    points = [ll, [x+w,y], [x+w, y+h], [x, y+h]]
    return polygon(points, rgbcolor=fillcolor, axes=False) + polygon(points,rgbcolor=strokecolor, fill=False,axes=False)

def display_vector(v):
    w = copy(v)
    w /= np.max(np.abs(v))
    return display_matrix(matrix(w).T)

def display_matrix(A):
    squares=[]
    y = A.nrows()-1
    for i, row in enumerate(A.rows()):
        x = 0
        for c in row:
            fillcolor = [c]*3
            if c < 0: fillcolor=[-c,0,0]
            strokecolor = [1 - f for f in fillcolor]           
            squares.append(square([x,y], [1,1], fillcolor, strokecolor))
            x += 1
        y -= 1
    return sum(squares)


data = csv.reader(open('letter.csv'), delimiter= ' ')
values = []
for datum in data:
    datum.pop(-1) 
    values.append([(1-float(d)) for d in datum])
A = matrix(RDF, values)
for row in values:
    print row


image = Image.open("utah-gray.png").convert('LA')
A = np.array(image)
A = A[:,:,0]
display_image(A)


data = csv.reader(open('noise.csv'))
values = []
for datum in data:
    datum.pop(-1) 
    datum[0] = datum[0][1:]
    values.append([n(float(d)^2,digits=3) for d in datum])
A = matrix(RDF, values)
for row in values:
    print row
