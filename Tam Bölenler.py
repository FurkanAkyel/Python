# Tam Bölenleri Bulan Program

sayi = int(input("Sayıyı Giriniz = "))

def TamBolenleriBul(n):
    tamBolenler = []
    sayac = 0
    
    for i in range(1, sayi+1):
        if sayi%i == 0:
            tamBolenler.append(i)
            sayac += 1

    return tamBolenler, sayac

print(TamBolenleriBul(sayi))