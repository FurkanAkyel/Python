import math

n = int(input())

for i in range(n-2,0,-1):
    a = math.gcd(i,n)
    
    if a == 1 :
        print(i)

        break