sayi = int(input('3 basamaklı sayıyı giriniz = '))
sayiUzunluk = str(sayi)

if len(sayiUzunluk) == 3:
    yuzler = sayi//100
    onlar = (sayi-(yuzler*100))//10
    birler = (sayi-(yuzler*100)-(onlar*10))
    sor = int(input("Sayıyı basamaklara ayırmak için 1, ters çevirmek için 2 yazınız = "))
    if sor == 1:
        print(f"Yüzler basamağı {yuzler}, onlar basamağı {onlar}, birler basamağı {birler}")
    elif sor == 2:
        print(birler,onlar,yuzler, sep="")
    else:
        print("Lütfen 1 veya 2 seçiniz!")
else:
    print("Lütfen 3 basamaklı sayı giriniz!")