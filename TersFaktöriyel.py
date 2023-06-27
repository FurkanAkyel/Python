sayi = int(input("Faktöriyeli Bulunacak Sayı = "))

def faktor(x,bas):
    if x == bas:
        return x
    else:
        x /= bas
        bas += 1
        return faktor(x,bas)
print(faktor(sayi,2))