# Öğrenci Bilgileri

ogrenciler = {}

numara = input("Öğrenci Numarası = ")
ad = input("Öğrenci Adı = ")
soyad = input("Öğrenci Soyadı = ")
telefon = input("Öğrenci Telefonu = ")

ogrenciler[numara] = {
    "Ad": ad,
    "Soyad": soyad,
    "Telefon": telefon
}

print(ogrenciler)

ogrNO = input("Öğrenci Numarası = ")
ogrenci = ogrenciler[numara]
print(ogrenci)