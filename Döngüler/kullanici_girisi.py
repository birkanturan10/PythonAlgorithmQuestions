print("""
**********
Kullanıcı Girişi Programı
**********
""")

sys_kullaniciadi = "birkan"
sys_parola = "123"
giris_hakki = 3

while True:
    kullanici_adi = input("Kullanıcı adı:")
    parola = input("Parola:")
    if(kullanici_adi != sys_kullaniciadi and parola == sys_parola):
        print("Kullanıcı adınızı hatalı girdiniz!")
        giris_hakki -=1
    elif(kullanici_adi == sys_kullaniciadi and parola != sys_parola):
        print("Parolanızı hatalı girdiniz!")
        giris_hakki -=1
    elif (kullanici_adi != sys_kullaniciadi and parola != sys_parola):
        print("Kullanıcı adı ve parolanızı hatalı girdiniz!")
        giris_hakki -= 1
    else:
        print("Sisteme başarıyla giriş yapıldı!")
        break
    if(giris_hakki == 0):
        print("Giriş hakkınız bitti!")