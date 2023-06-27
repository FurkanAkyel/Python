s = "Programlamada uzmanlaşmak isteyen bir kişinin çok sayida soru çözmesi gerekir! Bu aşamayi sadece sebatkâr öğrenciler geçer? İkinci problem sorunun anlaşilmasidir, Dikkatini verenler bu aşamayi rahatlikla geçer. Üçüncü aşamada anlaşilan sorunun çözüm basamaklarinin ortaya çikarilmasidir. Bir kâğit ve bir kalem bu güçlüğü aşmak için yeterlidir; Belirlenen çözüm basamaklarinin kod bloklarina dönüşümü en kolay aşama olarak görülür."

print("SORU 1 - Noktalama Kaldırma--------------------------------------------------------------------------------------")
noktalama = ["!","?",",",".",";"]
ys = ""

for i in range(len(s)-1):
    if not s[i] in noktalama:
        ys += s[i]
print(ys)

print("SORU 2 - Kelime Ekle---------------------------------------------------------------------------------------------")
kelimeListe = []
kelimeBas=0
for i in range(len(ys)-1):
    if ys[i]==" " and ys[i+1]!=" ":
        kelimeBas=i+1       
    if ys[i]!=" " and ys[i+1]==" ":
        kelime = ys[kelimeBas:i+1]
        kelimeListe.append(kelime)
print(kelimeListe)

print("SORU 3 - Ascii Hesabı--------------------------------------------------------------------------------------------")
asciiListe = kelimeListe
asciiYedek = []
c = 0
for i in range(len(kelimeListe)):
    asciiYedek = kelimeListe[i]
    topla = 0
    for j in range(len(asciiYedek)):
        asciiListe[c] = 0
        topla += ord(asciiYedek[j])
        asciiListe[c] = topla
    c += 1
print(asciiListe)

print("SORU 4 - Tek Rakamlı Basamak Sayısı------------------------------------------------------------------------------")
tekSayiListe = asciiListe
for i in range(len(asciiListe)):
    asciiToplam = []
    asciiToplam += str(asciiListe[i])
    tekSayiListe[i] = 0
    for j in range(len(asciiToplam)):
        sayi = float(asciiToplam[j])
        if sayi%2 == 1:
            tekSayiListe[i] += 1
print(asciiToplam)
print(tekSayiListe)