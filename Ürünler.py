# Ürünlerin Ad ve Fiyat Bilgisini Tutar

urunler = []

adet = int(input("Eklemek İstediğiniz Ürün Sayısı ="))
i=0 

while(i<adet):
    urunAd = input("Ürün Adı = ")
    urunUcret = input("Ürün Fiyatı = ")
    urunler.append({
        "Ürün Adı" : urunAd,
        "Ürün Fiyatı" : urunUcret
    })
    i += 1

for urun in urunler:
    print(f'Ürün Adı = {urun["Ürün Adı"]} Ürün Fiyatı = {urun["Ürün Fiyatı"]}')