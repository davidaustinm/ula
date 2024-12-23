import cv2
import numpy as np
from figures import *
img = cv2.imread('utah.cropped.jpg')

ul = (760,700)
#ul = (700, 760)
size = 8
lr = (ul[0]+size,ul[1]+size)
#cv2.rectangle(img, ul, lr, [0,255,0], 3)
#cv2.imshow("image", img)
#cv2.imwrite("block.jpg", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

for i in range(len(img)):
    for j in range(len(img[0])):
        rgb = img[i][j]
        l = -0.16874*rgb[2] + -0.33126*rgb[1] + 0.5*rgb[0]+127.5
        l = int(round(l))
        if l < 0: l = 0
        if l > 255: l = 255
        img[i][j] = [l,l,l]

cv2.imwrite('spring-canyon-blue-chrominance.jpg', img)
        
        


