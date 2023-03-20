import cv2
import pickle

try:
  with open ('carpos','rb') as f:
    pos_list = pickle.load(f)
except :
      pos_list =[]

width ,height = 100,40
def mouseClick(events,x,y,flags,param):
    if events == cv2.EVENT_FLAG_LBUTTON:
        pos_list.append((x,y))
    if events == cv2.EVENT_FLAG_RBUTTON:
        for i,pos in enumerate(pos_list):
            x1,y1 = pos
            if x1< x< x1+width and y1 < y < y1 + height:
                pos_list.pop(i)

    with open("carpos",'wb') as f :
        pickle.dump(pos_list,f)

while True:
    img = cv2.imread("carParkimg.png")
    for pos in pos_list:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)
    cv2.imshow("image",img)
    cv2.setMouseCallback("image",mouseClick)
    cv2.waitKey(1)