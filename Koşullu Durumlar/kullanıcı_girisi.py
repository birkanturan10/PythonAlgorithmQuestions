print("""
**********
Kullanıcı Girişi
**********
""")

sys_kullanici_adi = "birkan"
sys_parola = "123"

kullanici_adi = input("Kullanıcı adı:")
parola = input("Parola:")

if (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
    print("Parolanızı hatalı girdiniz!")
elif (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
    print("Kullanıcı adınızı yanlış girdiniz!")
elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
    print("Kullanıcı adınızı ve parolanızı hatalı girdiniz!")
else:
    print("Sisteme başarıyla giriş yaptınız!")