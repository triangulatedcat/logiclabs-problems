# Painting table
n,m,h = map(int,input().split())
TC=[]
cost=0
j=0
for r in range(h):
    t,c = map(int,input().split())
    TC.append((c,t))
NewTC = sorted(TC, key=lambda x : (x[0], -x[1]))
#print(NewTC)
if (sum(item[1] for item in NewTC) < (n*m)):
#    print(sum(item[1] for item in NewTC))
    print("Impossible")
else:
    remainingcells=n*m   
    for r in range(len(NewTC)):
        j = min(NewTC[r][1], remainingcells)
        cost+= NewTC[r][0]*j
        remainingcells-=j
    print(cost)
