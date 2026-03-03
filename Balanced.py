def findmaxbalancedsubset(l,k):
    n=len(l)
    l.sort()
    count=1
    max=1
    if n==1 or n==0:
        return n
    else:
        for r in range(n-1):
            if abs(l[r]-l[r+1]) <= k:
                count+=1
                continue
            elif max<=count:
                max=count
                count=1
            else:
                count=1
    if max<=count:
        max=count            
    return max

t = int(input())
ans=[]
for r in range(t):
    f,g = map(int,input().split())
    h=list(map(int,input().split()))
    ans.append(len(h) - findmaxbalancedsubset(h,g))
for r in range(t):
    print(ans[r])
