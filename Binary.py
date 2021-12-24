# Binary'e Çevirme

x = int(input("Sayıyı Giriniz = "))

def bin(n):
    if(n==0):
        return;
    bin(int(n/2));
    print(n%2,end="")
bin(x)