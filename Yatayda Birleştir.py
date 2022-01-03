m1 = [[22, 7, 3, 55],
[55, 57, 44, 34],
[23, 56, 5, 4]]
m2 = [[3, 8, 17, 20],
[21, 67, 107, 205]
[13, 207, 506, 509]]

def birlestir(m,n):
    result = []
    for i in range(len(m)):
        result.append(m[i]+n[i])
    return result

m3 = birlestir(m1, m2)
print(list(m3))
