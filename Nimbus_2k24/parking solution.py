import cv2 as cv
import pickle

width , height = 105, 45

try:
    with open('carpark' , 'rb') as f :
        poslist = pickle.load(f)
except:
    poslist = []


def mouseClick(events,x,y,flags,params):
    if events == cv.EVENT_LBUTTONDOWN:
        poslist.append((x,y))
    if events == cv.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(poslist):
            x1 , y1 = pos
            if x1 < x <x1+width and y1<y<y1+height:
                poslist.pop(i)
    
    with open('carpark' , 'wb') as f :
        pickle.dump(poslist , f) 

while True:
    img = cv.imread('img/car.jpg')
    for pos in poslist:
        cv.rectangle(img ,pos ,(pos[0]+ width , pos[1]+height), (255,0,255) , 2)
    cv.imshow('image',img)
    cv.setMouseCallback('image' , mouseClick )
    cv.waitKey(1)