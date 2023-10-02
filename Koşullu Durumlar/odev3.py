"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF

"""

vize1 = int(input("1. Vizenizi Giriniz:"))
vize2 = int(input("2. Vizenizi Giriniz:"))
final = int(input("Finalinizi Giriniz:"))

ortalama = vize1 * 3/10 + vize2 * 3/10 + final * 4/10

if(ortalama >= 90):
    print("AA")
elif(ortalama >= 85):
    print("BA")
elif(ortalama >= 80):
    print("BB")
elif(ortalama >= 75):
    print("CB")
elif(ortalama >= 70):
    print("CC")
elif(ortalama >= 65):
    print("DC")
elif(ortalama >= 60):
    print("DD")
elif(ortalama >= 55):
    print("FD")
else:
    print("FF")