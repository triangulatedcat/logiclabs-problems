# cook your dish here
t = int(input())
cats=[]
dogs=[]
counts=[]
verdict=[]

for i in range(t):
    c,d,l = map(int, input().split())
    cats.append(c)
    dogs.append(d)
    counts.append(l)

for i in range(t):
    c,d,l = cats[i],dogs[i],counts[i]
    verdict.append("no")
    r = l-(4*d) 
    if ( r%4 == 0 and r >=0 and r <= 4*c and  c-(r/4) <= 2*d):
        verdict[i]="yes"
    else:
        continue

for i in range(t):
    print(verdict[i])

