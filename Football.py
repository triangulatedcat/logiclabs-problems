n=int(input())
h=[]
a=[]
c=0
for i in range(n):
    x,y = map(int,input().split())
    h.append(x)
    a.append(y)
for i in range(n):
    for j in range(n):
        if (h[i]==a[j]): 
            c+=1
print(c)