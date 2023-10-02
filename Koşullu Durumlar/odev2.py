"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""

birinci_sayi = int(input("Birinci sayıyı giriniz:"))
ikinci_sayi = int(input("İkinci sayıyı giriniz:"))
ucuncu_sayi = int(input("Üçüncü sayıyı giriniz:"))

if(birinci_sayi > ikinci_sayi and birinci_sayi > ucuncu_sayi):
    print(birinci_sayi)
elif(ikinci_sayi > birinci_sayi and ikinci_sayi > ucuncu_sayi):
    print(ikinci_sayi)
else:
    print(ucuncu_sayi)