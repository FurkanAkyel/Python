# Verilen Değere Kadar Toplama İşlemi Yapar

sayi = int(input("Son Sayıyı Giriniz = "))

i = 1
sonuc = 0

while i <= sayi:
    sonuc += i
    i += 1

print(f'Toplam : {sonuc}')