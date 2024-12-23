from numpy import *
import numpy.linalg
import matplotlib.pyplot as plt

from scipy import misc
img = misc.imread('utah.cropped.jpg', mode='YCbCr')
img = img[:,:,0]  # isolate Y channel

misc.imsave('utah.gray.jpg', img)

svd = numpy.linalg.svd(img, full_matrices=False)
print len(svd[1])

rank = 500
singular = svd[1]
sigma = numpy.append(singular[:rank], numpy.zeros(len(singular)-rank))
sigma = numpy.diag(sigma)


u = svd[0]
v = svd[2]

print u.shape
print sigma.shape
print v.shape

image = numpy.matmul(u, numpy.matmul(sigma, v))

misc.imsave('utah.gray.0.jpg', image)




