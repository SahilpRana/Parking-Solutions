import cv2 as cv
import pickle 
import cvzone
import numpy as np

cap = cv.VideoCapture('img/video.mp4')

with open('carpark' , 'rb') as f :
    poslist = pickle.load(f)

width , height = 107, 48

while True:

    if cap.get(cv.CAP_PROP_POS_FRAMES) == cap.get(cv.CAP_PROP_FRAME_COUNT):
        cap.set(cv.CAP_PROP_POS_FRAMES , 0)
    
    success , img = cap.read()
    gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray , (3,3) , 1.1)
    threshold = cv.adaptiveThreshold(blur , 255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY_INV , 25 ,16)
    median = cv.medianBlur(threshold,5)
    kernal = np.ones((3,3) , np.uint8)
    imgDilate = cv.dilate(median , kernal , iterations= 1)


    for pos in poslist:
        x,y = pos
        crop = imgDilate[y:y+height , x:x+width]
        count = cv.countNonZero(crop)
        cvzone.putTextRect(img , str(count), (x,y+height) , 1.5 ,2 , offset=0)

        if count < 900:
            color = (0,255,0)
            thickness = 5
        else:
            color = (0,0,255)
            thickness = 2
        cv.rectangle(img ,pos ,(pos[0]+ width , pos[1]+height), color=color , thickness= thickness)
    cv.imshow("park", img)
    # cv.imshow("thresh", threshold)
    # cv.imshow("Dilate", imgDilate)
    cv.waitKey(10)