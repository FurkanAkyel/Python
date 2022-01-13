# İki Matrisi Dikey Eksen Boyunca Toplayıp Yeni Matris Dön

m1 = [[-1 , -2, -3, -4],
[-1 , -1, 55, -3],
[-2 , -2, -4, -4],
[9, 9, -57, 9],
[9, 2, 9, 9]]
m2 = [[-1 , -2, -3, -4],
[-1 , -1, 55, -3],
[-2 , -2, -4, -4],
[9, 9, -57, 9],
[9, 2, 9, 9]]

def dikeyEksenTopla1(a, b):
    k = a + b
    sutunSayisi = len(k[0])
    sonuc = [0] * sutunSayisi
    for c in range(sutunSayisi):
        for r in range(len(k)):
            sonuc[c] += k[r][c]
    return sonuc
   
n = m1+m2

def dikeyEksenTopla2(m):
    a = 0
    for j in range(len(m[0])):
        for i in range(len(m)):
            a += m[i][j]
        print(a)
        a=0

dikeyEksenTopla1(m1, m2))
print(dikeyEksenTopla2(n)