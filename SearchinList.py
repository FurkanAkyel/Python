urunler = ['iphone 8','samsung s21','htc one','iphone x','samsung s22','lenovo p1','redmi note 10s']
n = 0
arananMarka = 'iphone'

for urun in urunler:
    if urun[0:len(arananMarka)] == arananMarka:
        n += 1
print(n)