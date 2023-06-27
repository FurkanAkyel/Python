sayi = int(input("Sayıyı Giriniz="))

def Asallar(x):
    for sayi in range(x+1):
        asalmi = True

        if sayi == 1 or sayi == 0: 
            asalmi = False

        for i in range(2, sayi):
            if (sayi % i) == 0:
                asalmi = False
            
        if asalmi:
            print(f'{sayi} Asaldır.')
        else:
            continue

Asallar(sayi)