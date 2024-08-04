def isArmstrong(sayi):
    armstrong = 0
    for basamak in str(sayi):
        armstrong += int(basamak) ** len(str(sayi))
    if armstrong == sayi:
        print("Girdiğiniz değer Armstong sayıdır!")
    else:
        print("Girdiğiniz değer Armstrong sayı değildir!")

isArmstrong(371)