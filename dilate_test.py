import cv2
import numpy as np
img =cv2.imread('para.jpg',0)
cv2.imshow('saying',img)
ret,thresh=cv2.threshold(img,80,255,cv2.THRESH_BINARY_INV)
#edges=cv2.Canny(img,100,200)
#x=0
kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(thresh,kernel,iterations = 1)
#cv2.imshow('img',grey)
cv2.imshow('img',thresh)
#cv2.imshow('edges',edges)
contours, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('dilation',dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()




