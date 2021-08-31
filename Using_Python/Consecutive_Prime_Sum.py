import math

def prime(n):
    count=0
    d={2:True,3:True}
    for i in range(4,n):
        d[i]=True
    l=int(math.sqrt(n))
    m=int(n/2)
    for i in range(2,l+1):
        if d[i]==True:
            for p in range (2,m):
                if i*p<n:
                    d[i*p]=False
    for i in d.keys():
        if d[i]==True:
            count=count+1
    print(count)
            
prime(1000)