# Girilen Sayının Asal Olup Olmadığını Bulan Uygulama

number = int(input("Sayıyı Giriniz = "))
isprime = True

if number == 1 or number == 0: 
    isprime = False

for i in range(2, number):
    if (number % i) == 0:
        isprime = False
    
if isprime:
    print(f'{number} Asaldır.')
else:
    print(f'{number} Asal Değildir!')