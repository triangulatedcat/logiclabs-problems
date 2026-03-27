t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    if n%3==0:
        ans.append((n//3 , n//3))
    elif n%3 == 1:
        ans.append(((n//3) + 1, n//3))
    else:
        ans.append((n//3, (n//3) + 1))
for _ in range(t):
    print(ans[_][0], ans[_][1])