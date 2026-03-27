def numberofmoves(a,b):
    c=b-a
    if c<0:
        c=-c
    r= c%10
    if r==0:
        return (c//10)
    else:
        return ((c//10) + 1)

t= int(input())
ans=[]
for _ in range(t):
    x,y = map(int, input().split())
    ans.append(numberofmoves(x,y))
print(*ans, sep='\n')