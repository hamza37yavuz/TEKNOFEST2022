# TEKNOFEST2022



#### TEKNOFEST 2022 Doner Kanat iha 2. gorev python kodlari

**KLASÖRLER HAKKINDA**


1.0. ile baslayan klasorler testlerin bulundugu klasorlerdir. 


1.0.1 isimli klasordeki testlerin hepsi numaralandirma sirasina göre once simulasyon programi sonra iha uzerinde test edilmelidir.
Alinan hatalara gore kod uzerinde duzeltmeler yapilmasi gerekebilir.

1.0.1 ile başlayan klasor iha'nın çalışmasını test etme amaçlı yazılmıştır.
    
    1. Test arm_test1.py
    2. Test takeOff_test2.py
    3. Test goAndLand_test3.py
    (bu testte goEarth() yerine goIha yazarak ihanın yaptigi hareket gozlemlenmelidir.)
    4. Test goAndReturn_test4.py 
    (bu testte goEarth() yerine goIha yazarak ihanın yaptigi hareket gozlemlenmelidir.)
    5. Test goAndSavePoint_test5.py   
        (bu testte ihanin konum alabilmesi ve hassasiyeti test edilmistir. Test ortaminda ihanin 30 m ilerisine bir isaret konulmali alcaldigi noktanin isaretli noktaya    uzakligi olculmelidir.)
    6. Test servo_test6.py (Sonsuz dönen servo motor 17. pine baglanmistir. Servo sonsuz donen oldugu icin MAV_CMD_DO_REPEAT_SERVO kulanarak yapilmamistir.)
    
1.0.2 isimli klasor arayuz tasarlanmasindan once olusturulmus ogrenme amacli dosyadir.

1.0.3 isimli klasör görevi yapacak şekilde görüntü işlemenin çalıştırılması amacıyla hazırlanmıştır raspberry pi 4'te çalıştırılma amacıyla hazırlanmıştır.

info klasoru icerisinde requirements.txt içerisinde gerekli kütüphane lsitesi verilmiştir. ayrıca gereken kütüphanelerin bazı fonksiyonlarının kullanımı gösterilmiştir. 


Bu islemlerden sonra 2 . ile baslayan klasorlerin son surumu kullanılarak iha'nin goreve uygun sekilde calismasi saglanabilir.
