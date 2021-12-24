# VKİ

print("VKİ Hesaplama Robotu")

boy = float(input("Boy(m) = "))
kilo = float(input("Kilo(kg) = "))

vki = kilo/(boy**boy)

if vki<18.5:
    print("Zayıf =",vki)
elif 18.5<=vki<25:
    print("Normal =",vki)
else:
    print("Kilolu =",vki)