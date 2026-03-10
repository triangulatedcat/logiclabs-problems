# cook your dish here
def findansforasingletestcase():
    n,k = map(int,input().split())
    cardval= list(map(int,input().split()))
    cardnum= list(map(int,input().split()))
    turns= list(map(int,input().split()))
    totalcards= sum(cardnum)
    finalvaluelist= list(zip(cardval,cardnum))
    finalvaluelist.sort()
    totalsum = sum(item[0]*item[1] for item in finalvaluelist)
    #print(finalvaluelist)
    prev = totalcards
    left = 0
    right = 0

    for j in range(len(turns)):
        removed = prev - turns[j]
        prev = turns[j]

        if j % 2 == 0:
            left += removed
        else:
            right += removed
    l=0
    r=len(finalvaluelist)
    while (left > 0):
        if left > finalvaluelist[l][1]:
            left-=finalvaluelist[l][1]
            totalsum-= (finalvaluelist[l][1]*finalvaluelist[l][0])
            l+=1
        else:
            totalsum-= (left*finalvaluelist[l][0])
            break
    while (right > 0):
        if right > finalvaluelist[r-1][1]:
            right-=finalvaluelist[r-1][1]
            totalsum-= (finalvaluelist[r-1][1]*finalvaluelist[r-1][0])
            r-=1
        else:
            totalsum-= (right*finalvaluelist[r-1][0])
            break
                    
    
    return (totalsum)
        
ans=[]
t=int(input())
for _ in range(t):
    ans.append(findansforasingletestcase())
print(*ans, sep='\n')