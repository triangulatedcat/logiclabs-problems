n=int(input())
a=[]
b=[]
c=[]
for i in range(n):
    x,y,z=map(int,input().split())
    a.append(x)
    b.append(y)
    c.append(z)
dpa=[]
dpb=[]
dpc=[]
for i in range(n):
    if i==0:
        dpa.append(a[0])
        dpb.append(b[0])
        dpc.append(c[0])
    else:
        dpa.append(max(dpb[i-1],dpc[i-1]) + a[i])
        dpb.append(max(dpa[i-1],dpc[i-1]) + b[i])
        dpc.append(max(dpa[i-1],dpb[i-1]) + c[i])

print(max(dpa[n-1],dpb[n-1],dpc[n-1]))