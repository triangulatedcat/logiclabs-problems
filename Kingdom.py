# cook your dish here
def howmanybombs(intervals):
    intervalsS = sorted(intervals, key= lambda x:x[1])
    lastelement= intervalsS[0][1]
    s=1 
    for item in intervalsS:
        if lastelement < item[0]:
            s+=1
            lastelement = item[1]
    return s

t=int(input())
answer=[]
for item in range(t):
    n= int(input())
    currintervals=[]
    for item1 in range(n):
        a,b= map(int, input().split())
        currintervals.append((a,b))
    answer.append(howmanybombs(currintervals))
for item2 in range(t):
    print(answer[item2])
    