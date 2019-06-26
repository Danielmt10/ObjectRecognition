import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

backs=np.zeros([3,1])

while(True):
    ret, frame=cap.read()
    frame = cv2.flip(frame,1,0)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    output=frame.copy()
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,1000,
                        param1=50,param2=30,minRadius=10,maxRadius=100)
    
    circles = np.uint16(np.around(circles))
    for actualCircle in circles[0,:]:
    # draw the outer circle
        xCenter=actualCircle[0]
        yCenter=actualCircle[1]
        radius=actualCircle[2]
        
        xCenterBack=int(backs[0])
        yCenterBack=int(backs[1])
        radiusBack=int(backs[2])
        
        if xCenterBack==0 and yCenterBack==0 and radiusBack==0:
            xCenterBack=xCenter
            yCenterBack=yCenter
            radiusBack=radius
            
        xAbs=abs(xCenter-xCenterBack)
        yAbs=abs(yCenter-yCenterBack)
        radiusAbs=abs(radius-radiusBack)
        print(xAbs, yAbs, radiusAbs)
        
        backs[0]=xCenter
        backs[1]=yCenter
        backs[2]=radius
        
        if xAbs <= 10 and yAbs <=10 and radiusAbs <=10:
            # draw the center of the circle
            cv2.circle(output,(xCenter,yCenter),radius,(0,255,0),3)
        
    cv2.imshow('detected circles',output)
    key = cv2.waitKey(10)
    if key == 27:
        if cap.isOpened():
            cap=cv2.VideoCapture(1)
        break

cap.release()
cv2.destroyAllWindows()