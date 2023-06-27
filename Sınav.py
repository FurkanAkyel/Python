#Sorular

#Çevreden Alana - Sayfa 3
"""
dikdortgen = int(input("Dikdörtgen Çevre Uzunluğu Giriniz="))
kare = int(input("Karenin kenar Uzunluğu="))

dduzun = (dikdortgen-(kare*2))/2
ddalan = dduzun*kare
print(ddalan)
"""
#Denge-1 - Sayfa 4
"""
a = int(input("A Değeri = "))
b = int(input("B Değeri = "))
c = int(input("C Değeri = "))

x = ((b+c)-a)/3

print(f"x'in değer aralığı 0 <= x < {x}")
"""
#Denge-2 - Sayfa 5
"""
import random
solkefe = 0
sagkefe = 0
sayac = 0

solkefe += random.randint(0,50)
print("Sol Kefe Ağırlığı",solkefe)

while sayac <= 10:
    if sagkefe < solkefe:
        sagkefe += random.randint(0,50)
        sayac += 1
        print("Sağ Kefe Ağırlığı",sagkefe)
    elif solkefe < sagkefe:
        solkefe += random.randint(0,50)
        print("Sol Kefe Ağırlığı",solkefe)
    else:
        print("İki Kefe Eşitlendi")
        break
"""

#Alan - Sayfa 10
c = int(input("Kenarı Giriniz = "))
b = int(input("Kağıt Sayısını Giriniz = "))
a = c+2
ty = 0

def alan(x,n,top):
    kisa = c
    toplamAlan = 0
    if n == 0:
        return top
    else:
        print("X Sayısı = ",x,"N Sayısı = ",n)
        toplamAlan += (x*kisa)
        print(toplamAlan)
        return alan(x+2,n-1,top+toplamAlan)

print("Alan = ",alan(a,b,ty))