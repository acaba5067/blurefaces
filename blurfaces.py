import cv2
import numpy as np
images=["girl.jpg","group.jpg","Robert-Downey.jpg"]
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
for image_name in images:
 img = cv2.imread(image_name)
 cv2.imshow("input",img)
 detections = face_cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=6)
 for face in detections:
    x,y,w,h = face

    img[y:y+h,x:x+w]=cv2.GaussianBlur(img[y:y+h,x:x+w],(99,99),0)
    #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
 cv2.imshow("output",img)
 cv2.waitKey(0)



