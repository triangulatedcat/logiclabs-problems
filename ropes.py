def mybinsearch2(f,l,r,x):
        ans=-1
        while l<=r:
                m = l + ((r-l)//2)
                #print(l,m,r,n*w*h,l**2)
                if f(l)==x:
                    ans=l
                    break
                elif f(m) >=  x:
                    r=m
                else:
                    l=m+1
        return ans

def canwecut(x):
    if x<0:
        x = x*(-1)
    pieces=0
    for i in range(n):
        pieces+= (a[i]//x)
    if pieces >= k:
         return 1
    else:
         return 0
a=[]
ubound=0
#lbound=0
n,k = map(int,input().split())
for i in range(n):
    a.append((10**7)*int(input()))
#    lbound=a[0]
    if a[i] > ubound:
         ubound=a[i]
#    if a[i] < lbound:
#         lbound=a[i]
firstans= mybinsearch2(canwecut,-ubound-1,0,1) * (-1)
secans= str(firstans)
theans= f"{secans[0:-7]}.{secans[-7:]}"
print(theans)