n,m = map(int, input().split())
pieces= list(map(int, input().split()))
pieces.sort()
i=0
ans=pieces[m-1] - pieces[m-n]
while (i + n - 1 < m):
    if ans > pieces[i+n-1] - pieces[i]:
        ans = pieces[i+n-1] - pieces[i]
    i+=1
print(ans)