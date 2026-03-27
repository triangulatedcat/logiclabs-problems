n=int(input())
skills = list(map(int, input().split()))
a=[]
b=[]
c=[]
for i in range(n):
    if skills[i] == 1:
        a.append(i)
    elif skills[i] == 2:
        b.append(i)
    else:
        c.append(i)
j=min(len(a),len(b),len(c))
print(j)
for i in range(j):
        print(a[i]+1, b[i]+1, c[i]+1)