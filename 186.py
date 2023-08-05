def sorgu(ind, x):
    top = 0
    while ind > 0:
        top += x[ind]
        ind -= ind&(-ind)
    return top
 
def guncel(ind, x):
    while ind<len(x):
        x[ind] += 1
        ind+=ind&(-ind)
n = int(input())
s = input()
mp = {"a":1,"b":0, "c":-1}
arr = [0]*n
for i in range(n):
    arr[i]= arr[i-1]+mp[s[i]]
cevap = 0
st = n+1
x = [0]*(2*n+4)
guncel(st, x)
mod = 10**9+7
for i in range(n):
    ind = st + arr[i]
    guncel(ind, x)
    
    tmp = sorgu(ind-1, x)
    cevap +=tmp
    cevap%=mod
print(cevap)