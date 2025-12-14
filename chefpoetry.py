# cook your dish here
t = int(input())
outputlist=[]
for i in range(t):
    outputlist.append("UnluckyChef")
    pagelist=[]
    costlist=[]
    x,y,k,n = map(int,input().split())
    for u in range(n):
        p,c = map(int,input().split())
        pagelist.append(p)
        costlist.append(c)
    #print(i,outputlist)
    for v in range(n):
        if (0 >= x-y-pagelist[v]) and (0 <= k - costlist[v]):
            outputlist[i]="LuckyChef"
            break
    #print(i,outputlist)
            
for r in range(t):
    print(outputlist[r])
    