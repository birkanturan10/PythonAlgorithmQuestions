"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) * Boy(m)
"""

kilo = int(input("Kilonuzu giriniz:"))
boy = float(input("Boyunuzu giriniz:"))

print("Beden kitle endeksiniz {} olur.".format(kilo/(boy*boy)))