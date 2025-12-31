h,w = map(int,input().split())
m=[]
       

for i in range(h):
    m.append(list(input().strip()))
dp= [[0 for i in range(w)] for j in range(h)]

#dp[k][r]= dp[k-1][r] + dp[k][r-1]

#Base-case- the first row:
for j in range(w):
    if j==0:
        dp[0][0]=1
    elif m[0][j]==".":
        dp[0][j]=1
    else:
        break

#Base-Case- The first column:
for i in range(1,h):
    if m[i][0]==".":
        dp[i][0]= 1
    else:
        break
#Base-case done. Do recursion now.    
for i in range(1,h):
    for j in range(1,w):
        if m[i][j] == ".":
            dp[i][j]= dp[i-1][j] + dp[i][j-1]

print(dp[h-1][w-1] % ((10**9)+7))
#print(dp)