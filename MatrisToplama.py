m1 = [[1,2,3],
      [4,5,6],
      [1,1,1]]

m2 = [[3,2,1],
      [6,5,4],
      [2,2,2]]

mToplam = [[0,0,0],
      [0,0,0],
      [0,0,0]]

for i in range(3):
    for j in range(3):
        mToplam[i][j] = m1[i][j] + m2[i][j]

print("Toplam")

for i in range(3):
    print(mToplam[i])