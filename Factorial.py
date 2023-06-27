def factorial(x):
    fac=1
    for f in range(1,x+1):
        fac*=f   
    return fac
    
for i in range(1,10):
    print(i,"!=",factorial(i))