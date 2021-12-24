a = float(input("İlk Sayıyı Giriniz = "))
b = float(input("İkinci Sayıyı Giriniz = "))

def ebob(x,y):
    if y==0:
        return x
    else:
        return ebob(y,x%y)

print(ebob(a,b))