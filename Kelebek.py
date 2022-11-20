kelebek = int(input("Sayıyı Giriniz = "))
orta = 2*kelebek+1

for i in range(1,kelebek+1):
    print(i*"*",(orta-(2*i))*" ",i*"*",sep="")

print(orta*"*")

for i in range(kelebek,0,-1):
    print(i*"*",(orta-(2*i))*" ",i*"*",sep="")