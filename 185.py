import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
def input(): return sys.stdin.readline()
def mapi(): return map(int,input().split())
 
n = int(input())
edges = [list(mapi()) for i in range(n-1)]
c = [0]+list(mapi())
d = list(mapi())

par = [i for i in range(n+1)]
cnt = [{c[i]:1} for i in range(n+1)]
def bul(x):
    if x == par[x]: return x
    par[x] = bul(par[x])
    return par[x]
def union(x,y):
    x = bul(x)
    y = bul(y)
    if len(cnt[x])<len(cnt[y]): x,y = y,x
    par[y] = x
    res = 0
    for i,val in cnt[y].items():
        if i in cnt[x]:
            res += cnt[x][i]*val
            cnt[x][i]+=val
        else:
            cnt[x][i] = val
    return res
res = []
d = d[::-1]
for i in d:
    res.append(union(edges[i-1][0],edges[i-1][1]))
res = reversed(res)
print(*res,sep="\n")