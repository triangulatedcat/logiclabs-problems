
def converttobinary(aa):
    for i in range(len(aa)):
        if aa[i]==".":
            aa[i]=0
        elif aa[i]=="#":
            aa[i]=1
    return aa

h,w = map(int,input().split())
m=[]
a=[]        

for i in range(h):
    a=list(map(str,input().split()))
    m.append(converttobinary(a))
dp=m
dpq=[]
#dp[k][r]= dp[k-1][r] + dp[k][r-1]

#Base-case- the first row:
for j in range(w):
    if j==0:
        dpq.append(1)
    elif dpq[j-1] == 1 and m[0][j]==0:
        dpq.append(1)
    else:
        dpq.append(0)
    dp[0][j]=dpq[j]
dpv=[]
#Base-Case- The first column:
for j in range(h):
    if j==0:
        dpv.append(1)
    elif dpv[j-1] == 1 and m[j][0]==0:
        dpv.append(1)
    else:
        dpv.append(0)
    dp[j][0] = dpv[j]
#Base-case done. Do recursion now.    
for i in range(1,h):
    for j in range(1,w):
        dp[i][j]= dp[i-1][j] + dp[i][j-1]

print(dp[h-1][w-1] % ((10**9)+7))
