# Binary'e Çevirme

x = int(input("Sayıyı Giriniz = "))

def binary(n):
    if(n==0):
        return;
    bin(int(n/2));
    print(n%2,end="")
binary(x)