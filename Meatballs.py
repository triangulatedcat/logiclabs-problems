t = int(input())
v=[]
for i in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    # your code goes here
    s=0
    q=sorted(p,reverse=True)
    v.append(-1)
    for j in range(len(p)):
        #print(s)
        s+=q[j]
        if s>=m:
            v[i]=j+1
            break
for i in range(t):
    print(v[i])