import math
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
def ballonnumb(x):
    sum=0
    for i in range(n):
          p=T[i]
          q=Z[i]
          r=Y[i]
          sum = sum + (x//(p*q+r))*q + min(((x%(p*q+r))//p), q)
    if sum >= m:
        return 1
    else:
        return 0


m,n = map(int,input().split())
T=[]
Z=[]
Y=[]
for i in range(n):
    thesum=0
    thesum_=0
    t,z,y = map(int,input().split())
    T.append(t)
    Z.append(z)
    Y.append(y)
    thesum+= (t*z + y)
    thesum_+= z
ubound= ((m//thesum_) +1)*thesum      
theans= mybinsearch2(ballonnumb,0,ubound,1)
print(theans)
i=0
j=0
while j<=m and i<n:
    p=T[i]
    q=Z[i]
    r=Y[i]
    x=theans
    s = min((x//(p*q+r))*q + min(((x%(p*q+r))//p), q), m - j)
    j+=s
    print(s,end=' ')
    i+=1