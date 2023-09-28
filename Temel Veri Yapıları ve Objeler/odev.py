"""
Problem 1: Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
 Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.
"""

a = int(input("Birinci sayıyı giriniz:"))
b = int(input("İkinci sayıyı giriniz:"))
c = int(input("Üçüncü sayıyı giriniz:"))

print("{}*{}*{} sonucu {} olur.".format(a,b,c,a*b*c))
