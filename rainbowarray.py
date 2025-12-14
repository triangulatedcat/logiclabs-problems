t = int(input())
arrays=[]
verdict=[]

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    arrays.append(a)
    verdict.append("yes")
    
for r in range(t):
    for i in range (1,8):
        if (len(arrays[r])>1 and i == arrays[r][0] and arrays[r][0] == arrays[r][-1] ):
            while (len(arrays[r])>1 and arrays[r][0] == arrays[r][-1] and i==arrays[r][0] ):
                del arrays[r][0]
                del arrays[r][-1]
            continue
        elif ( i==7 and len(arrays[r])==1 and arrays[r][0]==7 ):
            verdict[r]="yes"
        else:
            verdict[r] = "no"
            break
       
for r in range(t):
    print(verdict[r])