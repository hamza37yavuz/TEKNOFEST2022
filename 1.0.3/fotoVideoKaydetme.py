import cv2

camera = cv2.VideoCapture(0)

# Fotograf Cekme ve Kaydetme
"""
ret,img = camera.read()
cv2.imwrite('test.jpg',img)
camera.release()
cv2.destroyAllWindows()
"""
# Video Cekme ve Kaydetme
#info
"""
Codec (Kod Çözücü)

Ham ses ve goruntu dosyalarinin boyutu olduka buyuktur, bu sorunu çozmeni yolu ise bu verileri sikistirmaktir.
Goruntu ve ses dosyalarini sikistirmak icin bir cok farkli algoritma gelistirilmistir, bu algoritmalar sikistirmak icin  farkli yontemler kullanmislardır.
Sikistirilan veriyi acmak icin ise bu sikistirma algoritmasini anlayacak ve veriyi gosterecek bir çozucuye ihtiyac duyulmaktadir, iste bu çözücüler codec olarak adlandırılmaktadır.
FourCC nin amaci medya verilerindeki codec’leri dort karakter ile tanimlamaktir, yani standart bir tanimlama formati olusturmaktir.
FourCC formatı aşağıdaki gibidir,

__ – __ – __ – __

8   –  8   –   8   –   8      = 4byte – 32bit
"""
#action
"""
fourrcc = cv2.VideoWriter_fourcc(*'XVID') # fourcc => codec
saveVideo = cv2.VideoWriter('video.avi', fourrcc, 9.0, (640, 480))
 
while (camera.isOpened()):
    ret, cam = camera.read()
    if ret == True: 
        saveVideo.write(cam)
        cv2.imshow('Kaydediliyor..', cam)
        if cv2.waitKey(1) &  0xFF == ord('q'):
            break
camera.release()
saveVideo.release()
cv2.destroyAllWindows()
"""