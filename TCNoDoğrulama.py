# TC Kimlik No Doğrulama

TCNo = input("TC NO Giriniz = ")

a = list(TCNo)

b = 0
for i in range(10):
    b+=int(a[i])

c = int(a[10])
d = b%10
e = ((int(a[0]) + int(a[2]) + int(a[4]) + int(a[6]) + int(a[8]))*8)%10
f = (((int(a[0]) + int(a[2]) + int(a[4]) + int(a[6]) + int(a[8]))*7) - (int(a[1]) + int(a[3]) + int(a[5]) + int(a[7])))%10
g = int(a[9])
h = (((int(a[0]) + int(a[2]) + int(a[4]) + int(a[6]) + int(a[8]))*7) + ((int(a[1]) + int(a[3]) + int(a[5]) + int(a[7]))*9))%10

if c == d and e == c and g == f:
    print("Girdiğiniz TCNO doğrudur.")
else:
    print("Girdiğiniz TCNO yanlıştır.")