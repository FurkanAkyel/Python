yukseklik = float(input("Topun bırakıldığı yüksekliği giriniz = "))
#kayip = float(0.2)
toplamYol = yukseklik
sicramaSayisi = 0

while yukseklik >= 1:
    yukseklik = yukseklik*0.8
    toplamYol += yukseklik
    sicramaSayisi += 1

toplamYol += yukseklik

print(f'Sıçrama Sayısı = {sicramaSayisi}, Aldığı Yol = {toplamYol}')