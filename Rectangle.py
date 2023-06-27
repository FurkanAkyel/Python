# Dikdörtgen Formülü

side1 = float(input("İlk Kenar = "))
side2 = float(input("İkinci Kenar = "))

area = side1*side2
perimeter = (side1*2)+(side2*2)
diagonal = ((side1**2)+(side2**2))**0.5

print("Çevre =",perimeter)
print("Alan =",area)
print("Köşegen = ",diagonal)