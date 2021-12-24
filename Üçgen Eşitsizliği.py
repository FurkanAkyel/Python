#Üçgen Eşitsizliği

import math

x = float(input("İlk Kenar = "))
y = float(input("İkinci Kenar = "))
z = float(input("Üçüncü Kenar = "))

cevre = x+y+z
u = cevre/2
alan = math.sqrt(u*(u-x)*(u-y)*(u-z))

if x-y<z<x+y and x-z<y<x+z and y-z<x<y+z:
    print("Üçgen Çizilebilir")
    if x==y==z:
        print("Eşkenar Üçgen")
    elif x==y or x==z or y==z:
        print("İkizkenar Üçgen")
    elif x!=y and x!=z and y!=z:
        print("Çeşitkenar Üçgen")
    print("Çevre =",cevre)
    print("Alan =",alan)
else:
    print("Üçgen Çizilemez")