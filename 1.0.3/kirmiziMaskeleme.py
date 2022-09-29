import cv2
import numpy as np
from dronekit import connect

# Bu fonksiyon bir koda eklendiginde ve çagrildiginda kirmiz icin maskeleme yapilacaktir

def maskeleme():
    # Kirmizi filtreleme icin kırmızı alt ve ust degerleri
    low_red = np.array([161,155,84])
    up_red = np.array([179,255,255])
    kernel = np.ones((5,5),np.uint8)

    # iha'nin yuksekligi 3 m yi gectiginde devreye girecek
    iha = connect("127.0.0.1:14550", wait_ready=True)
    if iha.location.global_relative_frame.alt > 3:
        kamera = cv2.VideoCapture(0)
        while True:
            ret,img = kamera.read()
            # cv2.imshow("orijinal",img)#bunu yorum satirindan cikararip calistirarak islemi goruntuleyebilirsiniz
            img = cv2.dilate(img,kernel,iterations=2)
            # cv2.imshow("dilate",img)
            img = cv2.erode(img,kernel,iterations=2)
            # cv2.imshow("erode",img)
            hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            cv2.imshow("hsv",img)
            mask = cv2.inRange(hsv,low_red,up_red)
            masked = cv2.bitwise_and(hsv,hsv,mask=mask)
            cv2.imshow("maskelenmis",mask)
            if cv2.waitKey(10) & 0xFF == ord('q'): 
                break
            
        kamera.release()
        cv2.destroyAllWindows()