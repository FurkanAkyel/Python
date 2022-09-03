# Girilen Sayının Asal Olup Olmadığını Bulan Uygulama

sayi = int(input("Sayıyı Giriniz = "))
asalmi = True

if sayi == 1 or sayi == 0: 
    asalmi = False

for i in range(2, sayi):
    if (sayi % i) == 0:
        asalmi = False
    
if asalmi:
    print(f'{sayi} Asaldır.')
else:
    print(f'{sayi} Asal Değildir!')