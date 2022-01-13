# Paint Nesne Boyama

global A
A = [[0,1,1,1,1],[0,1,0,0,0],[0,1,0,0,0],[1,0,0,0,0],[1,0,0,0,0]];

def MatrisYaz(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end=" ")
        print()

def Boya(y,x):
    A[y][x]=2
    if x>0:
        if A[y][x-1]!=2 and A[y][x-1]==1: Boya(y,x-1);
    if x<4:
        if A[y][x+1]!=2 and A[y][x+1]==1: Boya(y,x+1);
    if y>0:
        if A[y-1][x]!=2 and A[y-1][x]==1: Boya(y-1,x);
    if y<4:
        if A[y+1][x]!=2 and A[y+1][x]==1: Boya(y+1,x);

MatrisYaz(A)
print("===========")
Boya(0,2);
MatrisYaz(A)