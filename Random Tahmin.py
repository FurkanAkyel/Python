# Rastgele Sayıyı Tahmin Etme Oyunu

import random

sayi = random.randint(1,100)
hak = int(input("Tahmin Hakkı = "))
sayac = 0
puan = 100
tahmingider = puan/hak
puan += tahmingider

while hak > 0:
    
    hak-=1
    sayac += 1
    puan -= tahmingider
    tahmin = int(input("Sayı Kaç? = "))

    if tahmin == sayi:
        print(f'Tebrikler! {sayac}. defada bildiniz. Puanınız = {puan}')
        break
    elif tahmin < sayi:
        print("Yukarı")
    else:
        print("Aşağı")
    if hak == 0:
        print("Hakkınız Bitti! Sayı =", sayi)