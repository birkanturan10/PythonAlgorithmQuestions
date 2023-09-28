"""
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""

a = int(input("a: "))
b = int(input("b: "))

a,b=b,a

print("Sayılarınız a: {}, b: {} olarak değiştirilmiştir.".format(a,b))