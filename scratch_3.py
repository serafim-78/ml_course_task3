import cv2
import numpy as np
img=cv2.imread('gal_gadot.png', 0)
height, width = img.shape[:2]
imgs=[img]
#H-matrix
Haar = np.array([[1.0/2**0.5, 1.0/2**0.5], [-1.0/2**0.5, 1.0/2**0.5]])
print "Please, set count of division (>0). Advice 2:"
div=int(input())
print "Please, stand by..."
for cim in range(0,div):
    a=len(imgs)
    for k in range(0,a):
        hw=height>width
        wh=1-hw
        L=np.zeros(shape=(height/(2**hw), width/(2**wh)))
        H=np.zeros(shape=(height/(2**hw), width/(2**wh)))
        for i in range(0, height/2**hw):
            for j in range(0, width/2**wh):
                L[i, j] = np.dot(Haar, np.row_stack((imgs[0][(2**hw) *i,  (2**wh)*j], imgs[0][(2**hw)*i+hw, (2**wh)*j+wh])))[0]
                H[i,j]= np.dot(Haar, np.row_stack((imgs[0][(2**hw) *i,  (2**wh)*j], imgs[0][(2**hw)*i+hw, (2**wh)*j+wh])))[1]
        imgs.remove(imgs[0])
        imgs.append(L)
        imgs.append(H)
    height /= 2 ** hw
    width /= 2 ** wh
for i in range(0, len(imgs)):
    title="C:/Image#"+(i+1).__str__()+".png"
    cv2.imwrite(title, imgs[i])
print "Images saved on disk C"
