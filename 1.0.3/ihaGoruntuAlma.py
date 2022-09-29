import cv2
from dronekit import connect

def videoCek():
    iha = connect("127.0.0.1:14550", wait_ready=True)
    camera = cv2.VideoCapture(0)
    fourrcc = cv2.VideoWriter_fourcc(*'XVID') # fourcc => codec
    # bir alt satirda video.avi kisminda ismi degistirebilirsiniz dosyayi ayni dizine kaydetmesini istemiyorsaniz dosya yolunu degistirebilirsiniz
    saveVideo = cv2.VideoWriter('video.avi', fourrcc, 9.0, (640, 480))   
    while (camera.isOpened()):
        ret, cam = camera.read()
        if ret == True:
            if iha.location.global_relative_frame.alt > 3: # 3 m nin ustune ciktiginda video kaydedilmeye baslayacaktir
                saveVideo.write(cam)
                cv2.imshow('Kaydediliyor..', cam)
                if cv2.waitKey(1) &  0xFF == ord('q'):
                    break
    camera.release()
    saveVideo.release()
    cv2.destroyAllWindows()