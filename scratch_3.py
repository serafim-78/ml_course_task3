import cv2
import numpy as np

def r_haar(imgs, div, height, width):
    Haar = np.array([[1.0/2**0.5, 1.0/2**0.5], [-1.0/2**0.5, 1.0/2**0.5]])
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
    return imgs

img=cv2.imread('gal_gadot.jpg', 1)
height, width = img.shape[:2]
B, G, R= [img[:,:,0]], [img[:,:,1]], [img[:,:,2]]
print "Please, set count of division (>0). Advice 2:"
div=int(input())
print "Please, stand by..."
massB=r_haar(B, div, height, width)
print "33%..."
massG=r_haar(G, div, height, width)
print "66%..."
massR=r_haar(R, div, height, width)
print "99%..."
for i in range(0, 4):
    k=cv2.merge((massB[i], massG[i],massR[i]))
    cv2.imwrite("Img#"+(i+1).__str__()+".jpg", k)
