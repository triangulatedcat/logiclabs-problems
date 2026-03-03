def findbinarylikerep (p,a,k):
    i=k
    j=0
    q=p
    while (q>=1 and i>=0):
        if q>=a**i :
            q= q-(a**i)
            j+=1
        else:
            i=i-1
    return j

t=int(input())
l=[]
for r in range(t):
    p=int(input())
    l.append(findbinarylikerep(p,2,11))
for r in range(t):
    print(l[r])

    


    
