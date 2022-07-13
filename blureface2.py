import cv2
import numpy as np

haarcascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
images=["girl.jpg","group.jpg","Robert-Downey.jpg"]
for image_name in images:
  image=cv2.imread(image_name)
  gray=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
  faces=haarcascade.detectMultiScale(gray)
  for face in faces:
     x,y,w,h=face
    #cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0))
    #image[y:y+h,x:x+w] = cv2.GaussianBlur(image[y:y+h,x:x+w],(99,99),0)
     step_count=10
     stepX=np.linspace(x,x+w,step_count+1,dtype=np.int)
     stepY=np.linspace(y,y+h,step_count+1,dtype=np.int)
     for i in range(step_count):
         for j in range(step_count):

           color=cv2.mean(image[stepY[j]:stepY[j+1],stepX[i]:stepX[i+1]])
           #image[stepY[j]:stepY[j+1],stepX[i]:stepX[i+1]]=color
           cv2.rectangle(image,(stepX[i],stepY[j]),(stepX[i+1],stepY[j+1]),color,-1)




  cv2.imshow("image",image)
  cv2.waitKey(5000)


