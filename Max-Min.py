x = int(input("Gireceğiniz değer sayısı = "))
maks=int(0)
for i in range(x):
    sayi = int(input("Değer giriniz="))
    if maks<sayi:
        maks=sayi
print(maks)