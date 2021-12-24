n = int(input("Sayıyı Giriniz = "))

def fibonacci(x):
    if x==0:
        return x
    else:
        return 1
    return fibonacci(x-1)+fibonacci(x-2)

print(fibonacci(n))