"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın
 ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""

a = int(input("Aracınız kilometrede kaç TL yakıyor?:"))
b = int(input("Aracınızla ne kadar kilometre yol yaptınız?:"))

print("Toplam ödemeniz gereken fiyat: {} TL'dir.".format(a*b))