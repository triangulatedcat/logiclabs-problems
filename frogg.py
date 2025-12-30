n,k=map(int,input().split())
h=list(map(int,input().split()))
dp=[]
for i in range(0,n):
    if i==0:
        dp.append(0)
    else:
        dp.append(0)
        for j in range(i-1,max(i-k-1,-1),-1):
            if j==i-1:
                dp[i]= abs(h[i] - h[i-1]) + dp[i-1]
            elif abs(h[j] - h[i]) + dp[j] < dp[i]:
                dp[i] = abs(h[j] - h[i]) + dp[j]
    
print(dp[n-1])