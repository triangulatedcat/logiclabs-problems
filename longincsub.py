def findaLIS(a):
    dp=[]
    for i in range(len(a)):
        m=1
        if i == 0:
            dp.append(1)
        else:
            dp.append(1)
            for j in range(0,i):
                if a[j] < a[i] and dp[i] < 1+dp[j]:
                    dp[i] = 1 + dp[j]
                elif a[j] == a[i] and dp[i] < dp[j]:
                    dp[i] = dp[j]
        if m<dp[i]:
            m=dp[i]
    return m

s=str(input())
a=[ord(char) for char in s]
print(findaLIS(a))