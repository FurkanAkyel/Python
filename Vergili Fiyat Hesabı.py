price = float(input('Vergisiz fiyatı giriniz = '))
tax = float(input('Vergi oranını giriniz = '))

newprice = price+(price*(tax/100))

print(f' Ürünün vergili fiyatı = {newprice}₺')