import cv2
import pickle
import numpy as np
import cvzone

cap = cv2.VideoCapture("carpark.mp4")

with open ('carpos','rb') as f:
    pos_list = pickle.load(f)
width ,height = 100,40

def checking_space(imgpro):
    for pos in pos_list:
        x ,y = pos
        imgcrop = imgpro[y:y+height,x:x+width]
        #cv2.imshow(str(x*y),imgcrop)
        count = cv2.countNonZero(imgcrop)
        cvzone.putTextRect(img,str(count),(x,y+height-3),scale=1.1,offset=0)
        if count >500:
            color = (0,0,255)
            thickeness = 2
        else :
            color = (0,225,0)
            thickeness = 5
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),color,thickeness)



while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        
    success , img = cap.read()
    imggrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur = cv2.GaussianBlur(imggrey,(3,3),1)
    imgtheshold =cv2.adaptiveThreshold(imgblur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgmedian = cv2.medianBlur(imgtheshold,5)
    kernal = np.ones((3,3),np.uint8)
    imgdilate = cv2.dilate(imgmedian,kernal,iterations=1)

    checking_space(imgdilate)
    

    cv2.imshow("Image",img)
    cv2.waitKey(1)