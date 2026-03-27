# cook your dish here
def howmuchwire(l,s):
    n=len(s)
    if n==1:
        return 0
    j=0
    curr=0
    i=0
    v=0
    while (i<n-1):
        delta= l[i+1] - l[i]
        if s[i] == s[i+1] and s[i]=='0' :
            curr+=delta
            v=max(v,delta)
        elif s[i] == s[i+1] and s[i]=='1' :
            j=1
        elif s[i] != s[i+1] and s[i]=='0' :
            if j==0:
                curr+=delta
                j=1
                v=0
            else:
                v=max(delta,v)
                curr+=delta
                curr-=v
                v=0
        elif s[i] != s[i+1] and s[i]=='1' :
            curr+=delta
            v=max(delta,v)
            j=1
        i+=1
    return curr

t=int(input())
ans=[]
for _ in range(t):
    p=int(input())
    q=str(input())
    r=list(map(int,input().split()))
    ans.append(howmuchwire(r,q))

print(*ans, sep='\n')
