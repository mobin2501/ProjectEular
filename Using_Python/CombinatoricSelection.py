def ncr(n,r):
    i=n
    numerator=1
    denominator=1
    while  i>n-r:
        numerator=numerator*i
        i=i-1
    while r>1:
        denominator=denominator*r
        r=r-1
    return int(numerator/denominator)
print(ncr(100,49))
count=0

f=open('output53.txt','w')
for i in range(1,101):
    for r in range (1,i+1): #not necessarily distict if distinct use int(i/2)
        c=ncr(i,r)
        if(c>1000000):
            count=count+1
            f.write(str(i)+'c'+str(r)+' '+str(c)+'\n')

print(count)