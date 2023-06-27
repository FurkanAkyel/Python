sayi = int(input("Sayıyı giriniz = "))

for satir in range(1,sayi+1):
    for sutun in range(1,sayi+1):
        tablo=satir*sutun
        print("{0:4}".format(tablo), end="")
    print()