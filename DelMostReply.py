#Girilecek Değer Sayısını Öğrenip Döngüyle list1ye Ekleme
number = int(input("Kaç Değer Gireceksiniz? = "))
list1 = []
list2 = []

for i in range(number):
    ekle = input("Her Defasında Bir Değer Giriniz = ")
    list1 += (ekle)

print(list1)

#En Çok Tekrar Eden Değeri Tespit Etme
element = list1[0]
counter = 0
for i in range(number):
    if element == list1[i]:
        counter += 1

for i in range(1,number):
    element1 = list1[i]
    counter1 = 0
    for j in range(number):
        if element1 == list1[j]:
            counter1 += 1
            if counter < counter1:
                counter = counter1
                element = element1

#elementı Siliyoruz
for i in range(len(list1)):
    if list1[i] != element:
        list2t2 += list1[i]
print(list2)