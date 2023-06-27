N=int(input())
A=list(map(int,input().split(" ")))
B=list(map(int,input().split(" ")))

a=sum(A)
b=sum(B)

if(-1 in A)and(-1 in B):
    print("Infinite")
elif(-1 in A)and(-1 not in B):
    if(a>b):
        print("0") 
    else:
        print((b-a-A.count(-1))*(A.count(-1)-1)+1)
elif(-1 in B)and(-1 not in A):
    if(b>a):
        print("0")
    else:
        print((a-b-B.count(-1))*(B.count(-1)-1)+1)