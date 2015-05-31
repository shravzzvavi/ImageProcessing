import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #ret,thresh = cv2.threshold(imgray,127,255,0)


    
    
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    y=0
    kernal=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernal,iterations=100)
    #for y in range(0,5):
    kernal=np.ones((5,5),np.uint8)
    dilation=cv2.dilate(mask,kernal,iterations=10)

    kernal=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernal,iterations=100)
    #for y in range(0,5):
    kernal=np.ones((5,5),np.uint8)
    dilation=cv2.dilate(mask,kernal,iterations=100)

    x=0
#    for x in range(0,700):
    max =0
    print "test"    
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
	if x==0:
		max = cv2.contourArea(cnt)
		id=cnt
		x=x+1
	elif cv2.contourArea(cnt) > max:
		max = cv2.contourArea(cnt)
		id=cnt
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    x,y,w,h = cv2.boundingRect(id)
    frame2 = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
