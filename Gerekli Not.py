#Sınavdan Geçmek İçin Alınması Gereken Not

gecmeNotu = float(input("Geçme Notu = "))
ilkSinav = float(input("Vize Notunuz = "))
etki = float(input("Vizenin Yüzdelik Etkisi = "))

gerekliNot = gecmeNotu-(ilkSinav*etki/100)
final = gerekliNot*(100/(100-etki))

print(final)
print("Sistem notunuzu geçme notuna tamamlamaktadır. Kurumunuzun final notu için belirlediği alt sınır varsa dikkate almayı unutmayınız!!!")