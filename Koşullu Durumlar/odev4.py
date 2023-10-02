"""
Şimdi de geometrik şekil hesaplama işlemi yapalım.
 İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi
 , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı
 , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın.
  Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor"
   şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.
"""

sekil = input("Şekliniz üçgen mi dörtgen mi?")
if(sekil == "Üçgen"):
    birinci_kenar = int(input("Birinci kenarı giriniz:"))
    ikinci_kenar = int(input("İkinci kenarı giriniz:"))
    ucuncu_kenar = int(input("Üçüncü kenarı giriniz:"))
    if(abs(birinci_kenar + ikinci_kenar) > ucuncu_kenar and abs(birinci_kenar + ucuncu_kenar > ikinci_kenar and abs(ikinci_kenar + ucuncu_kenar) > birinci_kenar)):
        if(birinci_kenar == ikinci_kenar and birinci_kenar == ucuncu_kenar):
            print("Eşkenar Üçgen")
        elif((birinci_kenar == ikinci_kenar and birinci_kenar != ucuncu_kenar) or (birinci_kenar == ucuncu_kenar and birinci_kenar != ikinci_kenar) or (ikinci_kenar == ucuncu_kenar and ikinci_kenar != birinci_kenar)):
            print("İkizkenar Üçgen")
        else:
            print("Çeşitkenar Üçgen")
    else:
        print("Üçgen Belirtmiyor")
elif(sekil == "Dörtgen"):
    birinci_kenar = int(input("Birinci kenarı giriniz:"))
    ikinci_kenar = int(input("İkinci kenarı giriniz:"))
    ucuncu_kenar = int(input("Üçüncü kenarı giriniz:"))
    dorduncu_kenar = int(input("Dördüncü kenarı giriniz:"))
    if(birinci_kenar == ikinci_kenar and birinci_kenar == ucuncu_kenar and birinci_kenar == dorduncu_kenar):
        print("Kare")
    elif(birinci_kenar == ucuncu_kenar and ikinci_kenar == dorduncu_kenar):
        print("Dikdörtgen")
    else:
        print("Sıradan Dörtgen")
