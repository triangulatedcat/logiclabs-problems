def  isarraygood(a):
    n=len(a)
    b=0
    c=0
    for _ in range(n):
        if a[_]%2 == 0 and _%2 ==1:
             b+=1
        elif a[_]%2 == 1 and _%2 ==0:
             c+=1
    if b==c:
         return b
    else:
        return -1

t=int(input())
ans=[]
for _ in range(t):
    m=int(input())
    givenlist = list(map(int, input().split()))
    ans.append(isarraygood(givenlist))
print(*ans, sep='\n')
