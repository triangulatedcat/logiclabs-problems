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
def powerfunction(i):
    return (soldierpower[i])

n=int(input())
soldierpower=[]
for _ in range(n):
    soldierpower.append(int(input()))

soldierpower.sort()
cumulativesums=[]
s=0
for _ in range(len(soldierpower)):
    s+=soldierpower[_]
    cumulativesums.append(s)

totalrounds=int(input())
bishupower=[]
defeated=[]
cumulativedefeated=[]
currcumulativesum=0

for _ in range(totalrounds):
    x=int(input())
    bishupower.append(x)
    defeated.append(mybinsearch3(powerfunction,0,n-1,x) + 1)
    if defeated[-1]==0:
        cumulativedefeated.append(0)
    else:
        cumulativedefeated.append(cumulativesums[defeated[-1]-1])
 
for _ in range(totalrounds):
    print(defeated[_], cumulativedefeated[_])


      