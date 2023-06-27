sayi = int(input("Sayıyı Giriniz = "))

def asal(x,y,z):
    if x == 1 or x == 0:
        z = False
        return z
    elif x != y and x%y != 0:
        return(asal(x,y+1,z))
    elif x == y and x%y == 0:
        z = True
        return z 
    else:
        z = False
        return z

print(asal(sayi,2,True))