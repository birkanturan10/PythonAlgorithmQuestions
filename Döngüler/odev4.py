"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları
"toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın
 ve ekrana "toplam değişkenini" bastırın.

*İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü
break ile sonlandırın.*
"""

print("""
**********
Q'ya basarsanız toplam yapabilirsiniz.
**********
""")


toplam = 0

while True:
    sayi = input("Lütfen bir sayı giriniz:")
    if(sayi == "Q"):
        break
    sayi = int(sayi)
    toplam += sayi
print("Girdiğiniz sayıların toplamı:", toplam)
