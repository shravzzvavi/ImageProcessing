import cv2
import numpy as np
#img=np.zeros((100,100,3), np.uint8)
img2 = cv2.imread('test.jpg')
#print img2.size()
#height, width, depth = img2.shape
#print height, width, depth
img = cv2.resize(img2, (500, 500))
#cv2.resize(img2, img, img.size(), 0, 0, interpolation);
img1=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
