n=int(input())
dp=[]
for i in range(n):
    if i==0:
        dp.append(1)
    elif i==1:
        dp.append(2)
    else:
        dp.append(dp[i-2]+dp[i-1])
print(dp[n-1])