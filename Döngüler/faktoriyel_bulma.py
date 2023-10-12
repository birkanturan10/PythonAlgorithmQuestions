print("""
**********
Faktöriyel Bulma Programı

Çıkmak için "Q" ya basınız.
**********
""")

while True:
    sayi = input("Sayı:")
    if(sayi == "Q"):
        print("Program sonlandırıldı.")
        break
    else:
        sayi = int(sayi)
        faktoriyel = 1
        for i in range(2, sayi + 1):
            faktoriyel *= i
        print("Faktöriyel: {}".format(faktoriyel))