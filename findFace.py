import cv2
import numpy as np

# For now, we are going to feed it a file.  When it's working, 
# we will simply start it and it will process files as available.

cap = cv2.VideoCapture('faceFind.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', gray)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
           break
       
cap.release()
cv2.destroyAllWindows()