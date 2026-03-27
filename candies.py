def canwesplitfairly(candyweights):
    n=len(candyweights)
    a=0
    b=0
    for item in candyweights:
        if item==1:
            a+=1
        else:
            b+=1
    if a%2 != 0:
        return -1
    elif a>1:
        return 1
    elif b%2 != 0:
        return -1
    else:
        return 1


t=int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print("YES" if canwesplitfairly(l) == 1 else "NO")

