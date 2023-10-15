import time
import random
liste= [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
a=random.choice(liste)
f=int((a/2))
print("Sayı Tahmin Etme Oyununa Hoş Geldiniz")
time.sleep(2)
while True:
   print("Lütfen Aklınızdan bir sayı tutunuz.")
   b=str(input("Tuttunmu ? Evet/Hayır: "))
   time.sleep(2)
   if b=="Evet":
      c=str(input("Eminmisin ? Evet/Hayır: "))

      if c == "Evet" :
         print("Şimdi bu sayıyı 2 ile çarp")
         time.sleep(2)
         print("Şimdi bu sayıya",a,"ekle")
         time.sleep(2)
         print("2 ye böl ve tuttuğun sayıyı içinden çıkar ")
         time.sleep(2)
         print("Kalan sayı",f,"?")
         d=input("Evet/Hayır")

         if d=="Evet":
             print("Bildim!")
             time.sleep(4)
         elif d =="Hayır" :
            print("bence hata yaptın tekrar dene")
            time.sleep(4)
         else:
            print("Lütfen Geçerli bir değer giriniz")
            time.sleep(4)
      elif c=="Hayır":
         print("BU BENİM SORUNUM DEĞİL")
         time.sleep(4)
      else:
         print("Lütfen Geçerli bir değer giriniz")
         time.sleep(4)
   elif b == "Hayır":
      print("O zaman tutsaydın şapşal")
      time.sleep(4)
   else:
      print("Lütfen Geçerli bir değer giriniz")
      time.sleep(4)

if b==0 or c== 0 or d==0:
   quit()