a = float(input("Topun bırakıldığı yükseklik = "))

def topyol(x,yol,y):
    if x <= 10:
        return x,yol+y
    else:
        x = x*0.9
        yol = yol+x
        return topyol(x,yol,y)

print(topyol(a,0,a))