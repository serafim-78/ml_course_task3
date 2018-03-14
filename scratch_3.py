import cv2
import numpy as np
img=cv2.imread('gal_gadot.png', 0)
height, width = img.shape[:2]
#H-matrix
H = np.array([[1.0/2**0.5, 1.0/2**0.5], [-1.0/2**0.5, 1.0/2**0.5]])
for k in range(1,5):
    if height>width:
        L=np.zeros(shape=(height/2, width))
        for i in range(0, height/2):
            for j in range(0, width):
                L[i, j] = np.dot(H, np.row_stack((img[2 *i,  j], img[2*i+1, j ])))[0]
        height/=2
    else:
        L = np.zeros(shape=(height , width/ 2))
        for i in range(0, height):
            for j in range(0, width/2):
                L[i, j] = np.dot(H, np.row_stack((img[i, 2 * j], img[i, 2 * j + 1])))[0]
        width/=2
    title="Image #"+k.__str__()
    img=L
    cv2.imshow(title,L)
    cv2.waitKey(0)
