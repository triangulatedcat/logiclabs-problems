# cook your dish here
t = int(input())
coins=[]
ppl=[]
maxrem=[]

for i in range(t):
    n,k = map(int, input().split())
    coins.append(n)
    ppl.append(k)

for i in range(t):
    maxrem.append(0)
    print(maxrem)
    for j in range(1,ppl[i]+1):
        if coins[i]%j > maxrem[i]:
            maxrem[i]= coins[i]%j
        else:
            continue
for i in range(t):
    print(maxrem[i])

    