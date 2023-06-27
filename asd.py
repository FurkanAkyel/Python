n = int(input("Size of array:"))
k = int(input("Rotate:"))
array1 = []
for i in range(1,n+1):
    array1.append(i)
for i in range(k):
    a = array1.pop(n-1)
    array1.insert(0, a)

print(array1)