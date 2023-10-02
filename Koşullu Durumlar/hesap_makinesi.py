print("""
**********
Hesap Makinesi Programı

İşlemler;

1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
**********
""")

a = int(input("Birinci sayı:"))
b = int(input("İkinci sayı:"))
işlem = input("İşlemi giriniz:")

if işlem == "1":
    print("{} ile {} toplam değeri {} olur.".format(a,b,a+b))
elif işlem == "2":
    print("{} ile {} çıkarma değeri {} olur.".format(a,b,a-b))
if işlem == "3":
    print("{} ile {} çarpım değeri {} olur.".format(a, b, a * b))
if işlem == "4":
    print("{} ile {} bölüm değeri {} olur.".format(a, b, a / b))
else:
    print("Geçersiz işlem!")