number = int(input('3 basamaklı sayıyı giriniz = '))
numberLen = str(number)

if len(numberLen) == 3:
    hundred = number//100
    ten = (number-(hundred*100))//10
    one = (number-(hundred*100)-(ten*10))
    ask = int(input("Sayıyı basamaklara ayırmak için 1, ters çevirmek için 2 yazınız = "))
    if ask == 1:
        print(f"Yüzler basamağı {hundred}, onlar basamağı {ten}, birler basamağı {one}")
    elif ask == 2:
        print(one,ten,hundred, sep="")
    else:
        print("Lütfen 1 veya 2 seçiniz!")
else:
    print("Lütfen 3 basamaklı sayı giriniz!")