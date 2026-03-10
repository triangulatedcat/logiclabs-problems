from decimal import Decimal, getcontext, ROUND_HALF_UP
getcontext().prec = 10
#this outputs the max possible
#index i such that x is >= f(i) or -1 if there is no such index 
# f is a non-decreasing function on integers 
def mybinsearch3(f,l,r,x): 
    ans=-1
    if f(l) > x:
        ans = -1
    elif l==r:
        ans=r
    else:
        while (l<r):
            m = (l+r)//2
            if f(m) > x:
                r=m
            elif f(m+1)<=x:
                l=m+1
            else:
                r=m
        ans=r        
    return (ans)

def canwecut(x):
    pieces=0
    canwe=2
    for _ in range(n):
        pieces+= (a[_]//x)
        if pieces >= k :
            canwe=1
            break
    return (canwe)

a=[]
ubound=0
n,k = map(int,input().split())
for i in range(n):
    a.append((10**7)*int(input()))
    if a[i] > ubound:
         ubound=a[i] + 1

firstans= mybinsearch3(canwecut,1000,ubound,1)
theans = Decimal(firstans) / Decimal(10**7)
print(theans)