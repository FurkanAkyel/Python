# Binary'e Çevirme

x = int(input("Sayıyı Giriniz = "))

def binary(n):
    if n>1:
        binary(n//2)
    print(n%2, end = "")

binary(x)