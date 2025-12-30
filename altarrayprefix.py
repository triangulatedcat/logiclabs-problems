# cook your dish here
t=int(input())
b=[]
a=[]
for i in range(t):
    n=int(input())
    b= list(map(int,input().split()))
    a.append(b)
def mydpfunct(A,x):
    if x==len(A):
        return 1
    elif A[x]*A[x+1] < 0:
        return 1+mydpfunct(A,x+1)
    else:
        return 1
dp=[]

for i in range(t):
    dpa=[]
    for j in range(len(a[i])-1,-1,-1):
        if j==len(a[i])-1:
            dpa.append(1)
        elif a[i][j]*a[i][j+1] > 0:
            dpa.append(1)
        else:
            dpa.append(1+dpa[len(a[i])-j-2])
    dpa.reverse()
    #print(dpa)
    dp.append(dpa)
for i in range(t):
    print(*dp[i])

