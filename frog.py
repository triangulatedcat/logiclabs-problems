n=int(input())
h=list(map(int,input().split()))
dp=[]
for i in range(0,n):
    if i==0:
        dp.append(0)
    elif i==1:
        dp.append(abs(h[1]-h[0]))
    else:
        dp.append(min(dp[i-1]+abs(h[i]-h[i-1]),dp[i-2]+abs(h[i]-h[i-2])))

print(dp[n-1])